from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QEventLoop, QTime, QCoreApplication
from views.mainwindow import MainWindow
from controllers.tabla_procesos import Tabla_Procesos_Form
from time import sleep
from api import *

class MainWindowForm(QWidget, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.bucle = QEventLoop()
        self.estadoPrograma = "RUNNING"

        # Variables
        self.MAXIMA_CANTIDAD_PROCESOS : int = 4
        self.MAXIMO_TIEMPO_BLOQUEADO : int = 8
        self.PROCESO_NULO : Proceso = Proceso ("0+0", "0", "0")

        self.procesosEnMemoria : list = []

        self.procesosBloqueados : list = []
        self.procesosTerminados : list = []
        self.procesosListos: list = []
        self.procesosNuevos : list = []
        
        self.procesoActual: Proceso
        self.contadorGlobal : int = 0

        self.banderaError = False
        self.banderaInterrupcion = False

        self.setFocus()

        self.poblarTablas()
        
        self.simularButton.clicked.connect(self.simular)

    def delay(self) -> None:
        delayTime = QTime.currentTime().addSecs(1)

        while QTime.currentTime() < delayTime:
            QCoreApplication.processEvents(QEventLoop.AllEvents, 100)

    def generarProcesos(self) -> None:
        self.simularButton.setDisabled(True)
        self.cantidadProcesosLineEdit.setDisabled(True)

        cantidad = self.cantidadProcesosLineEdit.text()

        generar_lista_procesos(int(cantidad))

        self.procesosNuevos = obtener_lista_procesos()

    def simular(self) -> None:
        self.setFocus()
        self.generarProcesos()

        # Cargamos los primeros cuatro procesos a la memoria.
        self.procesosEnMemoria = self.procesosNuevos[:4]
        self.procesosNuevos = self.procesosNuevos[4:]

        self.procesosListos = self.procesosEnMemoria.copy()


        while True:
            self.banderaError = False
            self.banderaInterrupcion = False
            self.procesoActual = self.PROCESO_NULO

            # Si ya no quedan procesos en la memoria, entonces terminamos el bucle.
            if not self.procesosNuevos and not self.procesosEnMemoria:
                break
            
            # Cargamos el procesos actual y lo eliminamos de los listos.
            if len(self.procesosListos) > 0:
                self.procesoActual: Proceso = self.procesosListos[0]
                self.procesosListos.pop(0)
            
            self.mostrarProcesosListos()
            self.mostrarProcesosBloqueados()
    
            # Mostramos los procesos nuevos que quedan.
            self.procesosNuevosCountLabel.setText(str(len(self.procesosNuevos)))

            while self.procesoActual.tiempoTranscurrido < int(self.procesoActual.tiempo):
                self.mostrarProcesoEjecucion()
                self.mostrarProcesosBloqueados()

                # Verificamos si el tiempo de respuesta ya ha sido calculado para el proceso actual.
                if not self.procesoActual.tiempo_respuesta_calculado:
                    self.procesoActual.tiempo_respuesta = self.contadorGlobal - self.procesoActual.tiempo_llegada
                    self.procesoActual.tiempo_respuesta_calculado = True
                
                self.procesoActual.tiempoTranscurrido += 1
                self.contadorGlobal += 1
                self.contadorGlobalCountLabel.setText(str(self.contadorGlobal))

                self.incrementarTiempoBloqueados()

                # Si las teclas activaron alguna de las banderas, terminamos el bucle de ejecucion.
                if self.banderaInterrupcion or self.banderaError:
                    break
                
                self.delay()

            if self.procesosBloqueados and self.procesoActual == self.PROCESO_NULO:
                self.incrementarTiempoBloqueados()
                self.mostrarProcesosBloqueados()

                self.contadorGlobal += 1
                self.contadorGlobalCountLabel.setText(str(self.contadorGlobal))

                self.delay()

                continue

            if not self.banderaInterrupcion:
                # Si el tiempo transcurrido es igual al estimado, entonces el proceso ya termino su ejecucion.
                if self.procesoActual.tiempoTranscurrido == int(self.procesoActual.tiempoMaximoEstimado):
                    # Evaluamos si se termino normalmente o fue por un error.
                    if not self.banderaError:
                        self.procesoActual.resultado = str(self.realizarOperacion(self.procesoActual.operacion))
                        # Asignamos el tiempo de servicio.
                        self.procesoActual.tiempo_servicio = self.procesoActual.tiempoMaximoEstimado
                    else:
                        self.procesoActual.tiempo_servicio = self.procesoActual.aux_tiempo_servicio

                    # Asignamos el tiempo de finalizacion.
                    self.procesoActual.tiempo_finalizacion = self.contadorGlobal
                    # Asignamos el tiempo de retorno del proceso actual.
                    self.procesoActual.tiempo_retorno = self.contadorGlobal - self.procesoActual.tiempo_llegada
                    self.procesoActual.tiempo_espera = int(self.procesoActual.tiempo_retorno) - int(self.procesoActual.tiempo_servicio)
                    
                    self.procesosTerminados.append(self.procesoActual)
                    
                    # Eliminamos el proceso actual de la memoria.
                    self.procesosEnMemoria.remove(self.procesoActual)

                    # Ponemos su estado en Terminado.
                    self.procesoActual.estado = "Terminado"

            self.mostrarProcesosTerminados()
            
            if len(self.procesosEnMemoria) < self.MAXIMA_CANTIDAD_PROCESOS and self.procesosNuevos:
                for i in range(len(self.procesosEnMemoria), self.MAXIMA_CANTIDAD_PROCESOS):
                    # Se asigna el tiempo de llegada al proceso que entro al sistema.
                    self.procesosNuevos[0].tiempo_llegada = self.contadorGlobal
                    self.procesosEnMemoria.append(self.procesosNuevos[0])
                    self.procesosListos.append(self.procesosNuevos[0])

                    self.procesosNuevos.pop(0)

        self.estadoPrograma = "FINISHED"
        self.limpiar()

        crearProcesosTabla(self.procesosTerminados)
        self.abrirTabla()

    def incrementarTiempoBloqueados(self) -> None:
        for bloqueado in self.procesosBloqueados:
            bloqueado.tiempo_bloqueado += 1

            if bloqueado.tiempo_bloqueado % self.MAXIMO_TIEMPO_BLOQUEADO == 0:
                self.procesosListos.append(bloqueado)
                self.procesosBloqueados.remove(bloqueado)

                self.mostrarProcesosListos()
                self.mostrarProcesosBloqueados()

    def mostrarProcesosListos(self) -> None:
        self.procesosListosTable.setRowCount(len(self.procesosListos))

        for fila in range(len(self.procesosListos)):
            self.procesosListosTable.setItem(fila, 1, QTableWidgetItem(self.procesosListos[fila].idp))
            self.procesosListosTable.setItem(fila, 2, QTableWidgetItem(self.procesosListos[fila].tiempoMaximoEstimado))
            self.procesosListosTable.setItem(fila, 3, QTableWidgetItem(str(self.procesosListos[fila].tiempoTranscurrido)))
            self.procesosListosTable.setItem(fila, 4, QTableWidgetItem(str(int(self.procesosListos[fila].tiempoMaximoEstimado )- self.procesosListos[fila].tiempoTranscurrido)))

    def mostrarProcesoEjecucion(self) -> None:
        self.procesoActualTable.setItem(0, 2, QTableWidgetItem(str(self.procesoActual.idp)))
        self.procesoActualTable.setItem(1, 2, QTableWidgetItem(str(self.procesoActual.operacion)))
        self.procesoActualTable.setItem(2, 2, QTableWidgetItem(str(self.procesoActual.tiempoMaximoEstimado)))
        self.procesoActualTable.setItem(3, 2, QTableWidgetItem(str(self.procesoActual.tiempoTranscurrido)))
        self.procesoActualTable.setItem(4, 2, QTableWidgetItem(str(int(self.procesoActual.tiempoMaximoEstimado) - int(self.procesoActual.tiempoTranscurrido))))

    def mostrarProcesosTerminados(self) -> None:
        self.procesosTerminadosTable.setRowCount(len(self.procesosTerminados))

        for fila in range(len(self.procesosTerminados)):
            self.procesosTerminadosTable.setItem(fila, 1, QTableWidgetItem(str(self.procesosTerminados[fila].idp)))
            self.procesosTerminadosTable.setItem(fila, 2, QTableWidgetItem(str(self.procesosTerminados[fila].operacion)))
            self.procesosTerminadosTable.setItem(fila, 3, QTableWidgetItem(str(self.procesosTerminados[fila].resultado)))

    def mostrarProcesosBloqueados(self) -> None:
        self.procesosBloqueadosTable.setRowCount(len(self.procesosBloqueados))

        for fila in range(len(self.procesosBloqueados)):
            self.procesosBloqueadosTable.setItem(fila, 1, QTableWidgetItem(self.procesosBloqueados[fila].idp))
            self.procesosBloqueadosTable.setItem(fila, 2, QTableWidgetItem(str(self.procesosBloqueados[fila].tiempo_bloqueado)))

    def poblarTablas(self) -> None:
        self.contadorGlobalCountLabel.setText("0")
        self.procesosNuevosCountLabel.setText("0")

        column_labels_listos = ("", "ID", "T.M.E.", "T.T.", "T.R.")
        self.procesosListosTable.setColumnCount(len(column_labels_listos))
        self.procesosListosTable.setHorizontalHeaderLabels(column_labels_listos)
        self.procesosListosTable.setColumnHidden(0, True)
        self.procesosListosTable.setColumnWidth (1, 49)
        self.procesosListosTable.setColumnWidth (2, 50)
        self.procesosListosTable.setColumnWidth (3, 50)
        self.procesosListosTable.setColumnWidth (4, 50)
        self.procesosListosTable.verticalHeader().setVisible(False)
        self.procesosListosTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.procesosListosTable.setFocusPolicy(Qt.NoFocus)
        
        column_labels_ejecucion = ("ID", "", "Datos")
        self.procesoActualTable.setColumnCount(len(column_labels_ejecucion))
        self.procesoActualTable.setHorizontalHeaderLabels(column_labels_ejecucion)
        self.procesoActualTable.setColumnHidden(0, True)
        self.procesoActualTable.setRowCount(6)
        self.procesoActualTable.setItem(0, 1, QTableWidgetItem("ID"))
        self.procesoActualTable.setItem(1, 1, QTableWidgetItem("Operacion"))
        self.procesoActualTable.setItem(2, 1, QTableWidgetItem("Tiempo"))
        self.procesoActualTable.setItem(3, 1, QTableWidgetItem("T. Transcurrido"))
        self.procesoActualTable.setItem(4, 1, QTableWidgetItem("T. Restante"))
        self.procesoActualTable.verticalHeader().setVisible(False)
        self.procesoActualTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.procesoActualTable.setFocusPolicy(Qt.NoFocus)

        column_labels_bloqueados = ("", "ID", "T. Bloqueado")
        self.procesosBloqueadosTable.setColumnCount(len(column_labels_bloqueados))
        self.procesosBloqueadosTable.setHorizontalHeaderLabels(column_labels_bloqueados)
        self.procesosBloqueadosTable.setColumnHidden(0, True)
        self.procesosBloqueadosTable.setColumnWidth (1, 39)
        self.procesosBloqueadosTable.setColumnWidth (2, 79)
        self.procesosBloqueadosTable.verticalHeader().setVisible(False)
        self.procesosBloqueadosTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.procesosBloqueadosTable.setFocusPolicy(Qt.NoFocus)

        column_labels_terminados = ("", "ID", "Operacion", "Resultado")
        self.procesosTerminadosTable.setColumnCount(len(column_labels_terminados))
        self.procesosTerminadosTable.setHorizontalHeaderLabels(column_labels_terminados)
        self.procesosTerminadosTable.setColumnHidden(0, True)
        self.procesosTerminadosTable.setColumnWidth (1, 59)
        self.procesosTerminadosTable.setColumnWidth (3, 59)
        self.procesosTerminadosTable.verticalHeader().setVisible(False)
        self.procesosTerminadosTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.procesosTerminadosTable.setFocusPolicy(Qt.NoFocus)
        
    def limpiar(self) -> None:
        self.procesoActualTable.setItem (0, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (1, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (2, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (3, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (4, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (5, 2, QTableWidgetItem(""))

    def realizarOperacion(self, operacion: str) -> float:
        # Separamos lo que hay antes y despues del operador para obtener los valores.
        for i in range(len(operacion)):
            if operacion[i] == '+' or operacion[i] == '-' or operacion[i] == '*' or operacion[i] == '/' or operacion[i] == '%':
                operador = operacion[i]
                valor1 = float(operacion[:i])
                valor2 = float(operacion[i+1:])

        # Retornamos el resultado de la operacion.
        if operador == "+":
            return valor1 + valor2
        elif operador == "-":
            return valor1 - valor2
        elif operador == "*":
            return valor1 * valor2
        elif operador == "/":
            return round(valor1 / valor2, 2)
        else:
            return valor1 % valor2

    def keyPressEvent(self, event) -> None:
        # Evaluamos el estado actual del programa, 
        if event.key() == Qt.Key_I and self.estadoPrograma == "RUNNING" and self.procesoActual != self.PROCESO_NULO:
            self.banderaInterrupcion = True

            self.procesosBloqueados.append(self.procesoActual)

            self.mostrarProcesosBloqueados()

            print("Interrupcion")

        elif event.key() == Qt.Key_P and self.estadoPrograma == "RUNNING":

            print("Pausa")
            self.estadoPrograma = "PAUSED"

            self.bucle.exec()
            
        elif event.key() == Qt.Key_C and self.estadoPrograma == "PAUSED":
            self.bucle.exit()

            self.estadoPrograma = "RUNNING"
            print("Continuar")

        elif event.key() == Qt.Key_E and self.estadoPrograma == "RUNNING":
            self.banderaError = True
            self.procesoActual.resultado = "Error"
            self.procesoActual.aux_tiempo_servicio = self.procesoActual.tiempoTranscurrido
            self.procesoActual.tiempoTranscurrido = int(self.procesoActual.tiempoMaximoEstimado)

            print("Error")

        else:
            print("Otro")

    def abrirTabla(self) -> None:
        window = Tabla_Procesos_Form(self)

        window.show()