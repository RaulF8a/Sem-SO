from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QEventLoop, QTime, QCoreApplication, QRegularExpression, qDebug
from PySide6.QtGui import QRegularExpressionValidator, QPixmap
from types import SimpleNamespace
from views.mainwindow import MainWindow
from controllers.tabla_procesos import Tabla_Procesos_Form
from api import *
from Frame import *
import os.path
import json

class MainWindowForm(QWidget, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QPixmap(os.path.dirname(__file__)+"/../icon.png"))

        regEx = QRegularExpression("[1-9]+")
        input_validator = QRegularExpressionValidator(regEx)
        self.cantidadProcesosLineEdit.setValidator(input_validator)
        self.quantumLineEdit.setValidator(input_validator)

        self.bucle: QEventLoop = QEventLoop()
        self.estadoPrograma: str = "RUNNING"

        # Constantes
        self.MAXIMO_TIEMPO_BLOQUEADO : int = 8
        self.PROCESO_NULO : Proceso = Proceso ("0+0", "0", "0")
        self.PROCESO_NULO.tiempo_transcurrido = "0"
        self.QUANTUM: int = 0
        self.PAGINAS_POR_FRAME = 5
        self.CANTIDAD_TOTAL_FRAMES = 40

        self.procesosBloqueados : list[Proceso] = []
        self.procesosTerminados : list[Proceso] = []
        self.procesosListos: list[Proceso] = []
        self.procesosNuevos : list[Proceso] = []

        self.procesosSuspendidos: list[Proceso] = []
        self.limpiarArchivo()

        self.procesoActual: Proceso
        self.contadorGlobal : int = 0
        self.memoria: list[Frame] = []
        self.inicializarMemoria()

        self.banderaError = False
        self.banderaInterrupcion = False
        self.banderaNuevo = False
        self.banderaTerminadoQuantum = False
        self.banderaSuspendido = False
        self.banderaRegresoSuspendido = False

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
        self.QUANTUM = int(self.quantumLineEdit.text())

        generar_lista_procesos(int(cantidad))

        self.procesosNuevos = obtener_lista_procesos().copy()

    def simular(self) -> None:
        if not self.cantidadProcesosLineEdit.text() or not self.quantumLineEdit.text():
            return
        
        self.setFocus()
        self.generarProcesos()

        if self.QUANTUM > 16:
            return
        
        self.mostrarMemoria()
        self.cargarMemoria()
        
        while True:
            self.setFocus()

            self.procesoActual = self.PROCESO_NULO

            if not self.procesosNuevos and self.cantidadFramesDisponibles() == 38 and not self.procesosSuspendidos:
                break

            if len(self.procesosListos) > 0:
                self.procesoActual: Proceso = self.procesosListos[0]
                self.procesosListos.pop(0)
            
            qDebug(f"ProcesoActual: {str(self.procesoActual)}")
            self.mostrarProcesosListos()
            self.mostrarProcesosBloqueados()

            self.procesosNuevosCountLabel.setText(str(len(self.procesosNuevos)))

            self.suspendidosCountLabel.setText(str(len(self.procesosSuspendidos)))

            while True:
                self.cargarMemoria()

                if self.procesosNuevos:
                    self.sizeSiguienteLabel.setText(f"ID: {self.procesosNuevos[0].idp}\nSiguiente: {self.procesosNuevos[0].frames} frames")

                if self.procesoActual == self.PROCESO_NULO:
                    # Ya no hay procesos en memoria. Solo quedan los suspendidos.
                    if self.procesosSuspendidos and (not self.procesosNuevos and self.cantidadFramesDisponibles() == 38):
                        self.mostrarProcesosListos()
                        self.mostrarProcesosBloqueados()
                        self.mostrarProcesoEjecucion()

                        if self.banderaNuevo:
                            self.banderaNuevo = False

                            self.cargarMemoria()
                            self.procesosNuevosCountLabel.setText(str(len(self.procesosNuevos)))
                            if self.procesosNuevos:
                                self.sizeSiguienteLabel.setText(f"ID: {self.procesosNuevos[0].idp}\nSiguiente: {self.procesosNuevos[0].frames} frames")
                            self.mostrarProcesosListos()
                            
                            self.estadoPrograma = "RUNNING"

                        self.contadorGlobal += 1
                        self.contadorGlobalCountLabel.setText(str(self.contadorGlobal))
                        self.incrementarTiempoEsperaSuspendidos()

                        self.delay()
                        continue
                    else:
                        break
                
                if int(self.procesoActual.tiempo_transcurrido) == int(self.procesoActual.tiempo_maximo_estimado):
                    break

                if int(self.procesoActual.quantum_transcurrido) == self.QUANTUM:
                    self.banderaTerminadoQuantum = True
                    self.procesoActual.quantum_transcurrido = "0"
                    break
                
                self.procesoActual.estado = "Ejecucion"
                self.cambiarEstadoProceso(self.procesoActual.idp, "Ejecucion")
                
                self.mostrarProcesoEjecucion()
                self.mostrarProcesosBloqueados()
                self.contadorGlobalCountLabel.setText(str(self.contadorGlobal))

                if not self.procesoActual.tiempo_respuesta_calculado:
                    self.procesoActual.tiempo_respuesta = str(self.contadorGlobal - int(self.procesoActual.tiempo_llegada))
                    self.procesoActual.tiempo_respuesta_calculado = True
                
                if self.procesosBloqueados:
                    self.incrementarTiempoBloqueados()

                if self.banderaInterrupcion or self.banderaError:
                    self.limpiar()
                    break

                if self.banderaNuevo:
                    self.banderaNuevo = False

                    self.cargarMemoria()
                    self.procesosNuevosCountLabel.setText(str(len(self.procesosNuevos)))
                    if self.procesosNuevos:
                        self.sizeSiguienteLabel.setText(f"ID: {self.procesosNuevos[0].idp}\nSiguiente: {self.procesosNuevos[0].frames} frames")
                    self.mostrarProcesosListos()
                    
                    self.estadoPrograma = "RUNNING"
                
                self.procesoActual.tiempo_transcurrido = str(int(self.procesoActual.tiempo_transcurrido) + 1)
                self.procesoActual.tiempo_restante = str(int(self.procesoActual.tiempo_restante) - 1)

                self.procesoActual.quantum_transcurrido = str(int(self.procesoActual.quantum_transcurrido) + 1)
                self.contadorGlobal += 1
                self.incrementarTiempoEsperaSuspendidos()

                self.delay()

            if self.banderaRegresoSuspendido:
                self.banderaRegresoSuspendido = False
                self.mostrarProcesosBloqueados()
                continue

            if self.procesosBloqueados and self.procesoActual == self.PROCESO_NULO:
                self.incrementarTiempoBloqueados()

                self.mostrarProcesoEjecucion()
                self.mostrarProcesosBloqueados()

                if self.banderaNuevo:
                    self.banderaNuevo = False

                    self.cargarMemoria()
                    self.procesosNuevosCountLabel.setText(str(len(self.procesosNuevos)))
                    if self.procesosNuevos:
                        self.sizeSiguienteLabel.setText(f"ID: {self.procesosNuevos[0].idp}\nSiguiente: {self.procesosNuevos[0].frames} frames")
                    self.mostrarProcesosListos()
                    
                    self.estadoPrograma = "RUNNING"

                self.contadorGlobal += 1
                self.contadorGlobalCountLabel.setText(str(self.contadorGlobal))
                self.incrementarTiempoEsperaSuspendidos()

                self.delay()
                continue

            if self.procesoActual == self.PROCESO_NULO:
                continue
            
            if not self.banderaInterrupcion:
                if int(self.procesoActual.tiempo_transcurrido) == int(self.procesoActual.tiempo_maximo_estimado):
                    if not self.banderaError:
                        self.procesoActual.resultado = self.realizarOperacion(self.procesoActual.operacion)
                        self.procesoActual.tiempo_servicio = self.procesoActual.tiempo_maximo_estimado
                    else:
                        self.banderaError = False
                        self.procesoActual.tiempo_servicio = self.procesoActual.aux_tiempo_servicio

                    self.procesoActual.tiempo_finalizacion = str(self.contadorGlobal)
                    self.procesoActual.tiempo_retorno = str(self.contadorGlobal - int(self.procesoActual.tiempo_llegada))
                    self.procesoActual.tiempo_espera = str(int(self.procesoActual.tiempo_retorno) - int(self.procesoActual.tiempo_servicio))
                    
                    self.procesosTerminados.append(self.procesoActual)
                    
                    self.liberarFrames(self.procesoActual.idp)

                    self.procesoActual.estado = "Terminado"
            else:
                self.banderaInterrupcion = False
                self.cambiarEstadoProceso(self.procesoActual.idp, "Bloqueado")
                self.procesoActual.estado = "Bloqueado"

            if self.banderaTerminadoQuantum:
                self.banderaTerminadoQuantum = False

                self.procesoActual.estado = "Listo"
                self.cambiarEstadoProceso(self.procesoActual.idp, "Listo")
                self.procesosListos.append(self.procesoActual)

            self.mostrarProcesosTerminados()
            
            self.cargarMemoria()
            self.estadoPrograma = "RUNNING"

        self.estadoPrograma = "FINISHED"
        self.limpiar()

        # crearProcesosTabla()
        crearProcesosTabla(self.contadorGlobal)

        self.abrirTabla()

    def memoriaLlena(self) -> bool:
        framesLlenos = 0

        for i in range(self.CANTIDAD_TOTAL_FRAMES - 2):
            if self.memoria[i].espacioDisponible < self.PAGINAS_POR_FRAME:
                framesLlenos += 1
        
        return framesLlenos == self.CANTIDAD_TOTAL_FRAMES - 2

    def incrementarTiempoEsperaSuspendidos(self) -> None:
        if self.procesosSuspendidos:
            for suspendido in self.procesosSuspendidos:
                suspendido.tiempo_espera = str(self.contadorGlobal - int(suspendido.tiempo_llegada) - int(suspendido.tiempo_transcurrido))

    def cantidadFramesDisponibles(self) -> int:
        framesDisponibles: int = 0

        for i in range(self.CANTIDAD_TOTAL_FRAMES - 2):
            # Solo si un frame tiene todas sus paginas sin usar, estara disponible.
            if self.memoria[i].espacioDisponible == self.PAGINAS_POR_FRAME:
                framesDisponibles += 1

        return framesDisponibles

    def llenarFrames(self, tamanio: int, frames: int, id: str, estado: str) -> None:
        framesLlenados = 0
        
        for i in range(self.CANTIDAD_TOTAL_FRAMES - 2):
            # Validamos si el frame actual de la memoria tiene espacio y si el proceso aun requiere frames.
            if (self.memoria[i].espacioDisponible == self.PAGINAS_POR_FRAME and framesLlenados < frames):
                if (framesLlenados == frames - 1):
                    if (tamanio % self.PAGINAS_POR_FRAME != 0):
                        self.memoria[i].espacioDisponible -= (tamanio % self.PAGINAS_POR_FRAME)
                    else:
                        self.memoria[i].espacioDisponible = 0
                else:
                    self.memoria[i].espacioDisponible = 0

                # print(f"frame {i+1} tiene {self.memoria[i].espacioDisponible} paginas libres.")

                self.memoria[i].procesoQueUsaElEspacio = id
                self.memoria[i].estadoDelProceso = estado
                framesLlenados += 1

            # print(f"Frame {i+1} tiene {self.memoria[i].espacioDisponible} paginas libres.")

    def cambiarEstadoProceso(self, id: str, estado: str) -> None:
        for i in range(self.CANTIDAD_TOTAL_FRAMES - 2):
            if self.memoria[i].procesoQueUsaElEspacio == id:
                self.memoria[i].estadoDelProceso = estado

    def liberarFrames(self, id: str) -> None:
        for i in range(self.CANTIDAD_TOTAL_FRAMES - 2):
            if self.memoria[i].procesoQueUsaElEspacio == id:
                self.memoria[i].procesoQueUsaElEspacio = ""
                self.memoria[i].estadoDelProceso = ""
                self.memoria[i].espacioDisponible = self.PAGINAS_POR_FRAME

    def inicializarMemoria(self) -> None:
        for i in range(self.CANTIDAD_TOTAL_FRAMES):
            self.memoria.append(Frame())

    def cargarMemoria(self) -> None:
        contador = len(self.procesosNuevos)
        
        if self.banderaSuspendido and (int(self.procesosSuspendidos[0].frames) <= self.cantidadFramesDisponibles()):
            qDebug("Regresar suspendido desde cargar memoria")
            auxProceso = self.procesosSuspendidos[0]
            self.procesosSuspendidos.remove(auxProceso)

            auxProceso.estado = "Bloqueado"
            self.llenarFrames(int(auxProceso.tamanio), int(auxProceso.frames), auxProceso.idp, auxProceso.estado)
            self.procesosBloqueados.append(auxProceso)

            self.banderaSuspendido = False

            self.suspendidosCountLabel.setText(str(len(self.procesosSuspendidos)))
            
            if not self.procesosSuspendidos:
                self.siguienteSuspendidoLabel.setText("")
            else:
                self.siguienteSuspendidoLabel.setText(f"ID: {self.procesosSuspendidos[0].idp}\nTamaño: {self.procesosSuspendidos[0].frames} frames")

        if not self.memoriaLlena() and self.procesosNuevos:
            while True:
                auxProceso: Proceso = self.procesosNuevos[0]
                # Se asigna el tiempo de llegada al proceso que entro al sistema.
                auxProceso.tiempo_llegada = str(self.contadorGlobal)
                auxProceso.tiempo_transcurrido = "0"
                auxProceso.tiempo_restante = self.procesosNuevos[0].tiempo_maximo_estimado

                if (int(auxProceso.frames) <= self.cantidadFramesDisponibles()):
                    auxProceso.estado = "Listo"

                    self.llenarFrames(int(auxProceso.tamanio), int(auxProceso.frames), auxProceso.idp, auxProceso.estado)
                    self.procesosListos.append(auxProceso)

                    self.procesosNuevos.pop(0)

                if not self.procesosNuevos or self.memoriaLlena():
                    break

                if contador == 0:
                    break
                
                contador -= 1
        
        self.mostrarMemoria()
        self.sizeSiguienteLabel.setText("")

    def incrementarTiempoBloqueados(self) -> None:
        for bloqueado in self.procesosBloqueados:
            bloqueado.tiempo_bloqueado = str(int(bloqueado.tiempo_bloqueado) + 1)

            if int(bloqueado.tiempo_bloqueado) % self.MAXIMO_TIEMPO_BLOQUEADO == 0:
                bloqueado.estado = "Listo"
                bloqueado.tiempo_bloqueado = "0"
                self.cambiarEstadoProceso(bloqueado.idp, "Listo")
                self.procesosListos.append(bloqueado)
                self.procesosBloqueados.remove(bloqueado)

        self.mostrarProcesosListos()
        self.mostrarProcesosBloqueados()

    def mostrarProcesosListos(self) -> None:
        self.procesosListosTable.setRowCount(len(self.procesosListos))

        for fila in range(len(self.procesosListos)):
            self.procesosListosTable.setItem(fila, 1, QTableWidgetItem(self.procesosListos[fila].idp))
            self.procesosListosTable.setItem(fila, 2, QTableWidgetItem(self.procesosListos[fila].tiempo_maximo_estimado))
            self.procesosListosTable.setItem(fila, 3, QTableWidgetItem(str(self.procesosListos[fila].tiempo_transcurrido)))
            self.procesosListosTable.setItem(fila, 4, QTableWidgetItem(str(int(self.procesosListos[fila].tiempo_maximo_estimado) - int(self.procesosListos[fila].tiempo_transcurrido))))

    def mostrarProcesoEjecucion(self) -> None:
        self.procesoActualTable.setItem(0, 2, QTableWidgetItem(str(self.procesoActual.idp)))
        self.procesoActualTable.setItem(1, 2, QTableWidgetItem(str(self.procesoActual.operacion)))
        self.procesoActualTable.setItem(2, 2, QTableWidgetItem(str(self.procesoActual.tiempo_maximo_estimado)))
        self.procesoActualTable.setItem(3, 2, QTableWidgetItem(str(self.procesoActual.tiempo_transcurrido)))
        self.procesoActualTable.setItem(4, 2, QTableWidgetItem(str(int(self.procesoActual.tiempo_maximo_estimado) - int(self.procesoActual.tiempo_transcurrido))))
        self.procesoActualTable.setItem(5, 2, QTableWidgetItem(self.procesoActual.quantum_transcurrido))

    def mostrarProcesosTerminados(self) -> None:
        self.procesosTerminadosTable.setRowCount(len(self.procesosTerminados))

        for fila in range(len(self.procesosTerminados)):
            self.procesosTerminadosTable.setItem(fila, 1, QTableWidgetItem(str(self.procesosTerminados[fila].idp)))
            self.procesosTerminadosTable.setItem(fila, 2, QTableWidgetItem(str(self.procesosTerminados[fila].operacion)))
            self.procesosTerminadosTable.setItem(fila, 3, QTableWidgetItem(str(self.procesosTerminados[fila].resultado)))

    def mostrarMemoria(self) -> None:
        self.memoriaTable.setRowCount(40)

        for fila in range(len(self.memoria) - 2):
            self.memoriaTable.setItem(fila, 1, QTableWidgetItem(str(fila + 1)))
            self.memoriaTable.setItem(fila, 2, QTableWidgetItem(f"{self.memoria[fila].espacioDisponible}/5"))
            self.memoriaTable.setItem(fila, 3, QTableWidgetItem(str("N/A" if not self.memoria[fila].procesoQueUsaElEspacio else self.memoria[fila].procesoQueUsaElEspacio)))
            self.memoriaTable.setItem(fila, 4, QTableWidgetItem("-" if not self.memoria[fila].procesoQueUsaElEspacio else self.memoria[fila].estadoDelProceso))
        
        self.memoriaTable.setItem(38, 1, QTableWidgetItem("39"))
        self.memoriaTable.setItem(38, 2, QTableWidgetItem("0/5"))
        self.memoriaTable.setItem(38, 3, QTableWidgetItem("S.O."))
        self.memoriaTable.setItem(38, 4, QTableWidgetItem("-"))

        self.memoriaTable.setItem(39, 1, QTableWidgetItem("40"))
        self.memoriaTable.setItem(39, 2, QTableWidgetItem("0/5"))
        self.memoriaTable.setItem(39, 3, QTableWidgetItem("S.O."))
        self.memoriaTable.setItem(39, 4, QTableWidgetItem("-"))

    def mostrarProcesosBloqueados(self) -> None:
        self.procesosBloqueadosTable.setRowCount(len(self.procesosBloqueados))

        for fila in range(len(self.procesosBloqueados)):
            self.procesosBloqueadosTable.setItem(fila, 1, QTableWidgetItem(self.procesosBloqueados[fila].idp))
            self.procesosBloqueadosTable.setItem(fila, 2, QTableWidgetItem(str(self.procesosBloqueados[fila].tiempo_bloqueado)))

    def poblarTablas(self) -> None:
        self.contadorGlobalCountLabel.setText("0")
        self.procesosNuevosCountLabel.setText("0")
        self.suspendidosCountLabel.setText("0")

        column_labels_listos = ("", "ID", "T.M.E.", "T.T.", "T.R.")
        self.procesosListosTable.setColumnCount(len(column_labels_listos))
        self.procesosListosTable.setHorizontalHeaderLabels(column_labels_listos)
        self.procesosListosTable.setColumnHidden(0, True)
        self.procesosListosTable.setColumnWidth (1, 52)
        self.procesosListosTable.setColumnWidth (2, 59)
        self.procesosListosTable.setColumnWidth (3, 59)
        self.procesosListosTable.setColumnWidth (4, 67)
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
        self.procesoActualTable.setItem(5, 1, QTableWidgetItem("Quantum R."))
        self.procesoActualTable.setColumnWidth(2, 127)
        self.procesoActualTable.verticalHeader().setVisible(False)
        self.procesoActualTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.procesoActualTable.setFocusPolicy(Qt.NoFocus)

        column_labels_bloqueados = ("", "ID", "T. Bloqueado")
        self.procesosBloqueadosTable.setColumnCount(len(column_labels_bloqueados))
        self.procesosBloqueadosTable.setHorizontalHeaderLabels(column_labels_bloqueados)
        self.procesosBloqueadosTable.setColumnHidden(0, True)
        self.procesosBloqueadosTable.setColumnWidth (1, 39)
        self.procesosBloqueadosTable.setColumnWidth (2, 189)
        self.procesosBloqueadosTable.verticalHeader().setVisible(False)
        self.procesosBloqueadosTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.procesosBloqueadosTable.setFocusPolicy(Qt.NoFocus)

        column_labels_terminados = ("", "ID", "Operacion", "Resultado")
        self.procesosTerminadosTable.setColumnCount(len(column_labels_terminados))
        self.procesosTerminadosTable.setHorizontalHeaderLabels(column_labels_terminados)
        self.procesosTerminadosTable.setColumnHidden(0, True)
        self.procesosTerminadosTable.setColumnWidth (1, 39)
        self.procesosTerminadosTable.setColumnWidth (2, 103)
        self.procesosTerminadosTable.setColumnWidth (3, 103)
        self.procesosTerminadosTable.verticalHeader().setVisible(False)
        self.procesosTerminadosTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.procesosTerminadosTable.setFocusPolicy(Qt.NoFocus)

        column_labels_memoria = ("", "Marco", "Espacio", "Proceso", "Estado")
        self.memoriaTable.setColumnCount(len(column_labels_memoria))
        self.memoriaTable.setHorizontalHeaderLabels(column_labels_memoria)
        self.memoriaTable.setColumnHidden(0, True)
        self.memoriaTable.setColumnWidth (1, 49)
        self.memoriaTable.setColumnWidth (2, 59)
        self.memoriaTable.setColumnWidth (3, 53)
        self.memoriaTable.setColumnWidth (4, 82)
        self.memoriaTable.verticalHeader().setVisible(False)
        self.memoriaTable.setEditTriggers(self.procesosListosTable.NoEditTriggers)
        self.memoriaTable.setFocusPolicy(Qt.NoFocus)

        self.mostrarMemoria()
        
    def limpiar(self) -> None:
        self.procesoActualTable.setItem (0, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (1, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (2, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (3, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (4, 2, QTableWidgetItem(""))
        self.procesoActualTable.setItem (5, 2, QTableWidgetItem(""))

    def realizarOperacion(self, operacion: str) -> str:
        # Separamos lo que hay antes y despues del operador para obtener los valores.
        for i in range(len(operacion)):
            if operacion[i] == '+' or operacion[i] == '-' or operacion[i] == '*' or operacion[i] == '/' or operacion[i] == '%':
                operador = operacion[i]
                valor1 = float(operacion[:i])
                valor2 = float(operacion[i+1:])

        # Retornamos el resultado de la operacion.
        if operador == "+":
            return str(valor1 + valor2)
        elif operador == "-":
            return str(valor1 - valor2)
        elif operador == "*":
            return str(valor1 * valor2)
        elif operador == "/":
            return str(round(valor1 / valor2, 2))
        else:
            return str(valor1 % valor2)

    def keyPressEvent(self, event) -> None:
        # Evaluamos el estado actual del programa, 
        if event.key() == Qt.Key_I and self.estadoPrograma == "RUNNING" and self.procesoActual != self.PROCESO_NULO:
            self.banderaInterrupcion = True
            self.estadoPrograma = "KEY_PRESSED"

            # self.procesosListos.remove(self.procesoActual)
            self.procesoActual.tiempo_bloqueado = "0"
            self.procesosBloqueados.append(self.procesoActual)
            self.cambiarEstadoProceso(self.procesoActual.idp, "Bloqueado")
            self.limpiar()

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
            self.estadoPrograma = "KEY_PRESSED"

            self.procesoActual.resultado = "Error"
            self.procesoActual.aux_tiempo_servicio = self.procesoActual.tiempo_transcurrido
            self.procesoActual.tiempo_transcurrido = self.procesoActual.tiempo_maximo_estimado

            print("Error")

        elif event.key() == Qt.Key_N and self.estadoPrograma == "RUNNING":
            self.estadoPrograma = "KEY_PRESSED"
            procesoNuevo: Proceso = crear_proceso()
            self.procesosNuevos.append(procesoNuevo)

            self.banderaNuevo = True

            print("Proceso Nuevo")

        elif event.key() == Qt.Key_T and self.estadoPrograma == "RUNNING":
            print("BCP")

            crearProcesosTabla(self.contadorGlobal)
            self.contadorGlobalCountLabel.setText(str(self.contadorGlobal))
            self.abrirTabla()

            self.setFocus()

        elif event.key() == Qt.Key_A and self.estadoPrograma == "RUNNING":
            print("Memoria")

            self.estadoPrograma = "PAUSED"

            self.bucle.exec()

        elif event.key() == Qt.Key_S and self.estadoPrograma == "RUNNING":
            print("Suspender")

            if self.procesosBloqueados:
                self.cargarArchivo()

                self.suspendidosCountLabel.setText(str(len(self.procesosSuspendidos)))
                self.siguienteSuspendidoLabel.setText(f"ID: {self.procesosSuspendidos[0].idp}\nTamaño: {self.procesosSuspendidos[0].frames} frames")

        elif event.key() == Qt.Key_R and self.estadoPrograma == "RUNNING" and self.procesosSuspendidos:
            print("Regresar Suspendido")

            self.recuperarArchivo()

            self.suspendidosCountLabel.setText(str(len(self.procesosSuspendidos)))
            self.mostrarProcesosListos()
            
            if not self.procesosSuspendidos:
                self.siguienteSuspendidoLabel.setText("")
            else:
                self.siguienteSuspendidoLabel.setText(f"ID: {self.procesosSuspendidos[0].idp}\nTamaño: {self.procesosSuspendidos[0].frames} frames")

        else:
            print("Otro")

    def cargarArchivo(self) -> None:
        self.procesosBloqueados[0].estado = "Suspendido"
        self.procesosBloqueados[0].tiempo_espera = str(self.contadorGlobal - int(self.procesosBloqueados[0].tiempo_llegada) - int(self.procesosBloqueados[0].tiempo_transcurrido))
        self.procesosBloqueados[0].tiempo_servicio = self.procesosBloqueados[0].tiempo_transcurrido

        auxProcesoSuspendido: dict = vars(self.procesosBloqueados[0])
        banderaContenido = False

        with open("suspendidos.json", "r") as file:
            file.seek(0, os.SEEK_END)

            if file.tell():
                file.seek(0)
                banderaContenido = True
                d = json.load(file)

        if banderaContenido:
            with open("suspendidos.json", "w") as file:
                lista = [auxProcesoSuspendido]
                d.extend(lista)

                json.dump(d, file, indent=4)
        else:
            with open("suspendidos.json", "w") as file:
                lista = [auxProcesoSuspendido]
                json.dump(lista, file, indent=4)

        # Falta sacar de la memoria los procesos.
        self.liberarFrames(self.procesosBloqueados[0].idp)
        self.procesosSuspendidos.append(self.procesosBloqueados[0])

        self.procesosBloqueados.remove(self.procesosBloqueados[0])

    def recuperarArchivo(self) -> None:
        with open("suspendidos.json", "r") as file:
            procesos: list[dict] = json.load(file)
        
        procesos.pop(0)

        # Si aun quedan procesos, los volvemos a poner en el archivo.
        if procesos:
            with open("suspendidos.json", "w") as file:
                json.dump(procesos, file, indent=4)
        else:
            self.limpiarArchivo()
        
        if self.cantidadFramesDisponibles() < int(self.procesosSuspendidos[0].frames):
            self.banderaSuspendido = True
            qDebug("No hay espacio para que el proceso regrese. Colocado al tope de la cola.")
            return
        
        auxProceso: Proceso = self.procesosSuspendidos[0]
        self.procesosSuspendidos.remove(auxProceso)

        if not self.procesosNuevos and self.cantidadFramesDisponibles() == 38:
            self.banderaRegresoSuspendido = True

        auxProceso.estado = "Bloqueado"
        self.llenarFrames(int(auxProceso.tamanio), int(auxProceso.frames), auxProceso.idp, auxProceso.estado)
        self.procesosBloqueados.append(auxProceso)

    def limpiarArchivo(self) -> None:
        with open("suspendidos.json", "w") as file:
            file.write("")

    def abrirTabla(self) -> None:
        self.dialog = Tabla_Procesos_Form()

        self.dialog.exec_()
