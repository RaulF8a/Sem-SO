from PySide6.QtWidgets import QWidget
from views.mainwindow import MainWindow
from controllers.procesos import ProcesosForm
from controllers.procesamientoLotes import ProcesamientoLotesForm
from api import *


class MainWindowForm(QWidget, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.agregarProcesoButton_2.clicked.connect(self.agregar_proceso)
        self.iniciarButton.clicked.connect(self.iniciar_simulacion)
        self.limpiarButton.clicked.connect(self.limpiarLista)

    def agregar_proceso(self) -> None:
        window = ProcesosForm(self)
        window.show()

    def iniciar_simulacion(self) -> None:
        # Solo se puede iniciar la simulacion si hay al menos un proceso en la lista.
        if procesos_count() != "0":
            window = ProcesamientoLotesForm(self)
            window.show()

    def limpiarLista(self) -> None:
        limpiar()