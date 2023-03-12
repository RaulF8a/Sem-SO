from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.procesos import Procesos
from views.mainwindow import MainWindow
from api import *


class ProcesosForm(QWidget, Procesos):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.agregarButton.clicked.connect(self.crear_proceso)

    def crear_proceso(self):
        nombre = self.nombreLineEdit.text()
        operacion = self.operacionLineEdit.text()
        tiempo = self.tiempoLineEdit.text()
        idp = self.identificadorLineEdit.text()

        resultado = agregar_proceso(nombre, operacion, tiempo, idp)

        # Si se retorno el codigo de error 0, entonces el proceso se agrego exitosamente.
        # Caso contrario, mostramos el mensaje de error.
        if resultado[0] != 0:
            self.errorLabel.setText(resultado[1])
        else:
            self.close()
