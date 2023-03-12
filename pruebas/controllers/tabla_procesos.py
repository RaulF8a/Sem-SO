from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Qt
from Proceso import Proceso
from views.tabla_procesos import Tabla_Procesos
from api import obtenerProcesosTabla

class Tabla_Procesos_Form(QWidget, Tabla_Procesos):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setupUi(self)

        self.listaProcesos: list[Proceso] = obtenerProcesosTabla()
        print(self.listaProcesos)

        self.poblarTabla()

    def inicializarTabla(self) -> None:
        column_labels_tiempos = ("", "ID", "Operacion", "Resultado", "T.M.E.", "T. Llegada", "T. Finalizacion", "T. Retorno", "T. Respuesta", "T. Espera", "T. Servicio")
        self.tablaProcesosTable.setColumnCount(len(column_labels_tiempos))
        self.tablaProcesosTable.setHorizontalHeaderLabels(column_labels_tiempos)
        self.tablaProcesosTable.setColumnHidden(0, True)

        self.tablaProcesosTable.setEditTriggers(self.tablaProcesosTable.NoEditTriggers)
        self.tablaProcesosTable.verticalHeader().setVisible(False)
        
 
    def poblarTabla(self) -> None:
        self.inicializarTabla()

        self.tablaProcesosTable.setRowCount(len(self.listaProcesos))

        for fila in range(len(self.listaProcesos)):
            self.tablaProcesosTable.setItem(fila, 1, QTableWidgetItem(str(self.listaProcesos[fila].idp)))
            self.tablaProcesosTable.setItem(fila, 2, QTableWidgetItem(str(self.listaProcesos[fila].operacion)))
            self.tablaProcesosTable.setItem(fila, 3, QTableWidgetItem(str(self.listaProcesos[fila].resultado)))
            self.tablaProcesosTable.setItem(fila, 4, QTableWidgetItem(str(self.listaProcesos[fila].tiempoMaximoEstimado)))
            self.tablaProcesosTable.setItem(fila, 5, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_llegada)))
            self.tablaProcesosTable.setItem(fila, 6, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_finalizacion)))
            self.tablaProcesosTable.setItem(fila, 7, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_retorno)))
            self.tablaProcesosTable.setItem(fila, 8, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_respuesta)))
            self.tablaProcesosTable.setItem(fila, 9, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_espera)))
            self.tablaProcesosTable.setItem(fila, 10, QTableWidgetItem(str(self.listaProcesos[fila].tiempo_servicio)))
