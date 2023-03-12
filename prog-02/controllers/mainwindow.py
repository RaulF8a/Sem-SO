from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QThread
from views.mainwindow import MainWindow
from controllers.simulacion import SimulacionForm
from api import *


class MainWindowForm(QWidget, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.simularButton.clicked.connect(self.crear_procesos)

    def crear_procesos(self) -> None:
        cantidad = int(self.contadorProcesosSpinBox.text())

        generar_lista_procesos(cantidad)

        self.iniciar_simulacion()

    def iniciar_simulacion(self) -> None:
        window = SimulacionForm(self)
        window.show()