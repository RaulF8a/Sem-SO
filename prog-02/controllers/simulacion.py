from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QEventLoop, QThread, QObject, Signal, QTime, QCoreApplication
from views.simulacion import Simulacion
from api import *
from time import sleep
import threading

tiempoEstimado = 0
tiempoTranscurrido = 0

class SimulacionForm(QWidget, Simulacion):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        QWidget.setFocus(self)

        # Crear los estados y el bucle.
        self.estados = ['RUNNING', 'PAUSED']
        self.estado = self.estados[0]
        self.bucle = QEventLoop()

        # Obtener los datos de la API.
        self.lotes = obtener_lotes()
        self.n_lotes_pendientes = len(self.lotes)
        self.n_lote_actual = 0
        self.lotes_terminados = []
        self.n_lotes_terminados = 0
        self.contador_global = 0
        self.contador_lotes = 0

        self.set_up_tables(self.n_lotes_pendientes, self.n_lote_actual, self.contador_global, self.n_lotes_terminados)

        self.simularButton.clicked.connect(self.simular)

    def delay(self) -> None:
        delayTime = QTime.currentTime().addSecs(1)

        while QTime.currentTime() < delayTime:
            QCoreApplication.processEvents(QEventLoop.AllEvents, 100)

    def simular(self):
        self.simularButton.setDisabled(True)
        #Iniciar la simulacion.
        for lote in self.lotes:
            # En cada iteracion, se aumenta el contador de lotes, se reduce el contador de lotes pendientes
            # y se reinicia el contador de procesos.
            self.contador_lotes += 1
            self.n_lotes_pendientes -= 1
            contador_procesos = 0
            
            # Cargamos los procesos pendientes a la lista.
            self.loteActualCountLabel.setText(str(self.contador_lotes))
            self.lotesPendientesCountLabel.setText(str(self.n_lotes_pendientes))
            self.lotesPendientesTable.setRowCount(len(lote))
            
            self.actualizarProcesosPendientes(lote)

            self.repaint ()

            # Iteramos sobre la lista de procesos.
            for proceso in lote:
                contador_procesos += 1

                # Quitar el proceso de la lista de pendientes.
                self.lotesPendientesTable.removeRow(0)

                # Iniciar los cronometros.
                tiempo_transcurrido = 0
                tiempo_restante = int(proceso.tiempo) - tiempo_transcurrido

                # Mover el proceso a la tabla de proceso actual.
                self.loteActualTable.setItem (0, 2, QTableWidgetItem(proceso.idp))
                self.loteActualTable.setItem (1, 2, QTableWidgetItem(proceso.operacion))
                self.loteActualTable.setItem (2, 2, QTableWidgetItem(proceso.tiempo))
                self.loteActualTable.setItem (3, 2, QTableWidgetItem(tiempo_transcurrido))
                self.loteActualTable.setItem (4, 2, QTableWidgetItem(tiempo_restante))

                # Simular el reloj.
                while (tiempo_transcurrido < int(proceso.tiempo)):
                    tiempo_transcurrido += 1
                    tiempo_restante -= 1
                    self.contador_global += 1

                    self.contadorGlobalCountLabel.setText (str(self.contador_global))
                    self.loteActualTable.setItem (4, 2, QTableWidgetItem(str(tiempo_transcurrido)))
                    self.loteActualTable.setItem (5, 2, QTableWidgetItem(str(tiempo_restante)))

                    self.delay()
                    self.repaint ()

                # Realizar la operacion.
                resultado = self.realizarOperacion(proceso.operacion)

                # Mover el proceso actual a la lista de terminados.
                filasTerminadas = self.lotesTerminadosTable.rowCount()
                self.lotesTerminadosTable.insertRow(filasTerminadas)

                self.lotesTerminadosTable.setItem(filasTerminadas, 1, QTableWidgetItem(proceso.idp))
                self.lotesTerminadosTable.setItem(filasTerminadas, 2, QTableWidgetItem(proceso.operacion))
                self.lotesTerminadosTable.setItem(filasTerminadas, 3, QTableWidgetItem(str(resultado)))
                # self.repaint ()
                
                # Limpiar la tabla de proceso actual.
                self.loteActualTable.setItem (0, 2, QTableWidgetItem(""))
                self.loteActualTable.setItem (1, 2, QTableWidgetItem(""))
                self.loteActualTable.setItem (2, 2, QTableWidgetItem(""))
                self.loteActualTable.setItem (3, 2, QTableWidgetItem(""))
                self.loteActualTable.setItem (4, 2, QTableWidgetItem(""))
                self.loteActualTable.setItem (5, 2, QTableWidgetItem(""))
                # self.repaint ()

            self.lotes_terminados.append(lote)
            self.repaint ()

    def set_up_tables(self, n_lotes: int, lote_actual: int, contador: int, lotes_terminados: int) -> None:
        self.lotesPendientesCountLabel.setText(str(n_lotes))
        self.loteActualCountLabel.setText(str(lote_actual))
        self.contadorGlobalCountLabel.setText(str(contador))

        column_labels_pendientes = ("", "ID", "T.M.E.", "T.T.")
        self.lotesPendientesTable.setColumnCount(len(column_labels_pendientes))
        self.lotesPendientesTable.setHorizontalHeaderLabels(column_labels_pendientes)
        self.lotesPendientesTable.setColumnHidden(0, True)
        self.lotesPendientesTable.setColumnWidth (2, 59)
        self.lotesPendientesTable.setColumnWidth (3, 59)

        column_labels_actual = ("ID", "", "Datos")
        self.loteActualTable.setColumnCount(len(column_labels_actual))
        self.loteActualTable.setHorizontalHeaderLabels(column_labels_actual)
        self.loteActualTable.setColumnHidden(0, True)
        self.loteActualTable.setRowCount(6)
        self.loteActualTable.setItem(0, 1, QTableWidgetItem("ID"))
        self.loteActualTable.setItem(1, 1, QTableWidgetItem("Operacion"))
        self.loteActualTable.setItem(2, 1, QTableWidgetItem("Tiempo"))
        self.loteActualTable.setItem(3, 1, QTableWidgetItem("T. Transcurrido"))
        self.loteActualTable.setItem(4, 1, QTableWidgetItem("T. Restante"))

        column_labels_pendientes = ("", "ID", "Operacion", "Resultado")
        self.lotesTerminadosTable.setColumnCount(len(column_labels_pendientes))
        self.lotesTerminadosTable.setHorizontalHeaderLabels(column_labels_pendientes)
        self.lotesTerminadosTable.setColumnHidden(0, True)
        self.lotesTerminadosTable.setColumnWidth (3, 59)
    
        # self.repaint ()

    def actualizarProcesosPendientes (self, lote) -> None:
        self.lotesPendientesTable.setRowCount(len(lote))
        for fila in range(len(lote)):
            self.lotesPendientesTable.setItem (fila, 1, QTableWidgetItem(lote[fila].idp))
            self.lotesPendientesTable.setItem (fila, 2, QTableWidgetItem(lote[fila].tiempo))
            self.lotesPendientesTable.setItem (fila, 3, QTableWidgetItem(lote[fila].tiempo_transcurrido))

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

        if event.key() == Qt.Key_I and self.estado == "RUNNING":
            print("Interrupcion")

        elif event.key() == Qt.Key_P and self.estado == "RUNNING":
            print("Pausa")
            self.estado = self.estados[1]
            self.bucle.exec()
            
        elif event.key() == Qt.Key_C and self.estado == "PAUSED":
            print("Continuar")
            self.estado = self.estados[0]
            self.bucle.quit()

        elif event.key() == Qt.Key_E and self.estado == "RUNNING":
            print("Error")

        else:
            print("Otro")
