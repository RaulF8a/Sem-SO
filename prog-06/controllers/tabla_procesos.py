from PySide6.QtWidgets import QTableWidgetItem, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from Proceso import Proceso
from views.tabla_procesos import TablaProcesos
from api import obtenerProcesosTabla
import os.path

class Tabla_Procesos_Form(QDialog, TablaProcesos):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowIcon(QPixmap(os.path.dirname(__file__)+"/../icon.png"))
        self.setWindowTitle("Tabla de Procesos")
        self.setupUi(self)
        QDialog.setFocus(self)

        a, b = obtenerProcesosTabla()

        self.listaProcesos: list[Proceso] = a
        self.contadorAlMomento: int = b

        # print(self.listaProcesos)

        self.poblarTabla()

    def inicializarTabla(self) -> None:
        column_labels_tiempos = ("", "ID", "Operacion", "Resultado", "Estado", "T.M.E.", "T. Llegada", "T. Finalizacion", "T. Retorno", "T. Respuesta", "T. Espera", "T. Servicio", "Tamaño", "T. Restante Bloqueado", "T. Restante en CPU")
        self.tablaProcesosTable.setColumnCount(len(column_labels_tiempos))
        self.tablaProcesosTable.setHorizontalHeaderLabels(column_labels_tiempos)
        self.tablaProcesosTable.setColumnHidden(0, True)
        self.tablaProcesosTable.setColumnWidth(13, 140)
        self.tablaProcesosTable.setColumnWidth(14, 140)

        self.tablaProcesosTable.setEditTriggers(self.tablaProcesosTable.NoEditTriggers)
        self.tablaProcesosTable.verticalHeader().setVisible(False)     
 
    def calcularTiemposAlMomento(self) -> None:
        for proceso in self.listaProcesos:
            if proceso.estado == "Listo" or proceso.estado == "Ejecucion" or proceso.estado == "Bloqueado":
                proceso.tiempo_espera = str(self.contadorAlMomento - int(proceso.tiempo_llegada) - int(proceso.tiempo_transcurrido))
                proceso.tiempo_servicio = proceso.tiempo_transcurrido

                # print (f"Contador: {self.contadorAlMomento} E + S: {proceso.tiempo_espera + proceso.tiempo_servicio}")

    def poblarTabla(self) -> None:
        self.inicializarTabla()
        self.calcularTiemposAlMomento()

        self.tablaProcesosTable.setRowCount(len(self.listaProcesos))

        for fila in range(len(self.listaProcesos)):
            self.tablaProcesosTable.setItem(fila, 1, QTableWidgetItem(str(self.listaProcesos[fila].idp)))
            self.tablaProcesosTable.setItem(fila, 2, QTableWidgetItem(str(self.listaProcesos[fila].operacion)))
            self.tablaProcesosTable.setItem(fila, 3, QTableWidgetItem(str(self.listaProcesos[fila].resultado)))
            self.tablaProcesosTable.setItem(fila, 4, QTableWidgetItem(str(self.listaProcesos[fila].estado)))
            self.tablaProcesosTable.setItem(fila, 5, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_maximo_estimado)))
            self.tablaProcesosTable.setItem(fila, 6, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_llegada)))
            self.tablaProcesosTable.setItem(fila, 7, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_finalizacion)))
            self.tablaProcesosTable.setItem(fila, 8, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_retorno)))
            self.tablaProcesosTable.setItem(fila, 9, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_respuesta)))
            self.tablaProcesosTable.setItem(fila, 10, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_espera)))
            self.tablaProcesosTable.setItem(fila, 11, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_servicio)))
            self.tablaProcesosTable.setItem(fila, 12, QTableWidgetItem(str(self.listaProcesos[fila].tamanio)))
            
            if self.listaProcesos[fila].estado == "Bloqueado":
                self.tablaProcesosTable.setItem(fila, 13, QTableWidgetItem(str(8 - int(self.listaProcesos[fila].tiempo_bloqueado))))
            else:
                self.tablaProcesosTable.setItem(fila, 13, QTableWidgetItem("N/A"))
            
            self.tablaProcesosTable.setItem(fila, 14, QTableWidgetItem(self.listaProcesos[fila].tiempo_restante))

            self.tablaProcesosTable.setEditTriggers(self.tablaProcesosTable.NoEditTriggers)
            self.tablaProcesosTable.setFocusPolicy(Qt.NoFocus)
            self.tablaProcesosTable.horizontalScrollBar().setStyleSheet("background: lightGray")
            self.tablaProcesosTable.verticalScrollBar().setStyleSheet("background: lightGray")

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_C:
            self.accept()

            print("Continuar BCP")
