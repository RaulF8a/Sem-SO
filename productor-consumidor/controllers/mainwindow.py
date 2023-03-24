from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt, QEventLoop, QTime, QCoreApplication, qDebug
from PySide6.QtGui import QPixmap
from views.mainwindow import MainWindow
from Productor import Productor
from Consumidor import Consumidor
import os.path
import random as rd

class MainWindowForm(QWidget, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.cargarImagenesPC()

        self.setFocus()

        # Constantes.
        self.LEN_BUFFER: int = 22
        self.DURMIENDO: int = 0
        self.TRABAJANDO: int = 1
        self.INTENTANDO: int = 2
        self.TURNO_PRODUCTOR: int = 1
        self.TURNO_CONSUMIDOR: int = 2 

        # Variables.
        self.buffer: list[bool] = []
        self.productor: Productor = Productor()
        self.consumidor: Consumidor = Consumidor()
        self.turno: int = 0
        self.cantidadMovimientos: int = 0
        self.banderaCerrar: bool = False

        self.show()
        self.ejecutar()

    def delay(self) -> None:
        delayTime = QTime.currentTime().addSecs(1)

        while QTime.currentTime() < delayTime:
            QCoreApplication.processEvents(QEventLoop.AllEvents, 100)

    def inicializarArreglo(self) -> None:
        for i in range(self.LEN_BUFFER):
            self.buffer.append(False)

    def productosEnBuffer(self) -> int:
        contador: int = 0

        for elemento in self.buffer:
            if (elemento):
                contador += 1

        return contador

    def cargarImagenesPC(self) -> None:
        self.imagenConsumidorLabel.setPixmap(QPixmap(os.path.dirname(__file__)+"/../homero.png"))
        self.imagenConsumidorLabel.setScaledContents(True)
        self.imagenConsumidorLabel.setAlignment(Qt.AlignCenter)

        self.imagenProductorLabel.setPixmap(QPixmap(os.path.dirname(__file__)+"/../chef.png"))
        self.imagenProductorLabel.setScaledContents(True)
        self.imagenProductorLabel.setAlignment(Qt.AlignCenter)

    def realizarAccion(self, indice: int, accion: bool) -> bool:
        # Si la accion a realizar es la mimsma que tiene el espacio actual del buffer, entonces
        # no se puede realizar nada.
        if (accion == self.buffer[indice]):
            # Si la accion es colocar la casilla en verdadero, el productor esta intentando.
            if (accion):
                self.productor.estado = self.INTENTANDO
            else:
                self.consumidor.estado = self.INTENTANDO
            
            return False

        # Caso contrario, cambiamos el valor de la casilla por el nuevo.
        self.buffer[indice] = accion
        return True

    def siguientesMovimientos(self) -> None:
        turnoTemp = rd.randint(1, 11)
        self.turno = self.TURNO_PRODUCTOR if turnoTemp % 2 == 0 else self.TURNO_CONSUMIDOR
        self.cantidadMovimientos = rd.randint(3, 7)

        # Turno del productor.
        if self.turno == 1:
            # Verificamos si el buffer no esta lleno.
            if self.productosEnBuffer() != self.LEN_BUFFER:
                self.productor.estado = self.TRABAJANDO
                self.consumidor.estado = self.DURMIENDO
            else:
                self.productor.estado = self.INTENTANDO
                self.consumidor.estado = self.DURMIENDO
        # Turno del consumidor.
        else:
            # Verificamos que haya algo que consumir.
            if self.productosEnBuffer() > 0:
                self.productor.estado = self.DURMIENDO
                self.consumidor.estado = self.TRABAJANDO
            else:
                self.productor.estado = self.DURMIENDO
                self.consumidor.estado = self.INTENTANDO

    def setEtiqueta(self) -> None:
        # Evaluamos los estados del productor.
        if (self.productor.estado == self.TRABAJANDO):
            self.estadoProductorLabel.setText("TRABAJANDO")
            self.estadoProductorLabel.setStyleSheet(self.estadoProductorLabel.styleSheet() + "background-color:\"#3db83d\";")
            self.estadoProductorLabel.repaint()

        elif (self.productor.estado == self.INTENTANDO):
            self.estadoProductorLabel.setText("INTENTANDO")
            self.estadoProductorLabel.setStyleSheet(self.estadoProductorLabel.styleSheet() + "background-color:\"#ffb647\";")
            self.estadoProductorLabel.repaint()
        
        else:
            self.estadoProductorLabel.setText("DURMIENDO")
            self.estadoProductorLabel.setStyleSheet(self.estadoProductorLabel.styleSheet() + "background-color:\"#ff0000\";")
            self.estadoProductorLabel.repaint()
        
        # Evaluamos los estados del consumidor.
        if (self.consumidor.estado == self.TRABAJANDO):
            self.estadoConsumidorLabel.setText("TRABAJANDO")
            self.estadoConsumidorLabel.setStyleSheet(self.estadoConsumidorLabel.styleSheet() + "background-color:\"#3db83d\";")
            self.estadoConsumidorLabel.repaint()
        
        elif (self.consumidor.estado == self.INTENTANDO):
            self.estadoConsumidorLabel.setText("INTENTANDO")
            self.estadoConsumidorLabel.setStyleSheet(self.estadoConsumidorLabel.styleSheet() + "background-color:\"#ffb647\";")
            self.estadoConsumidorLabel.repaint()
        
        else:
            self.estadoConsumidorLabel.setText("DURMIENDO")
            self.estadoConsumidorLabel.setStyleSheet(self.estadoConsumidorLabel.styleSheet() + "background-color:\"#ff0000\";")
            self.estadoConsumidorLabel.repaint()

    def setImagen(self, indice: int) -> None:
        imagen = QPixmap(os.path.dirname(__file__)+"/../dona.png")

        if (indice == 0):
            auxLabel = self.buffer1Label
        elif (indice == 1):
            auxLabel = self.buffer2Label
        elif (indice == 2):
            auxLabel = self.buffer3Label
        elif (indice == 3):
            auxLabel = self.buffer4Label
        elif (indice == 4):
            auxLabel = self.buffer5Label
        elif (indice == 5):
            auxLabel = self.buffer6Label
        elif (indice == 6):
            auxLabel = self.buffer7Label
        elif (indice == 7):
            auxLabel = self.buffer8Label
        elif (indice == 8):
            auxLabel = self.buffer9Label
        elif (indice == 9):
            auxLabel = self.buffer10Label
        elif (indice == 10):
            auxLabel = self.buffer11Label
        elif (indice == 11):
            auxLabel = self.buffer12Label
        elif (indice == 12):
            auxLabel = self.buffer13Label
        elif (indice == 13):
            auxLabel = self.buffer14Label
        elif (indice == 14):
            auxLabel = self.buffer15Label
        elif (indice == 15):
            auxLabel = self.buffer16Label
        elif (indice == 16):
            auxLabel = self.buffer17Label
        elif (indice == 17):
            auxLabel = self.buffer18Label
        elif (indice == 18):
            auxLabel = self.buffer19Label
        elif (indice == 19):
            auxLabel = self.buffer20Label
        elif (indice == 20):
            auxLabel = self.buffer21Label
        elif (indice == 21):
            auxLabel = self.buffer22Label

        if (self.turno == self.TURNO_PRODUCTOR):
            auxLabel.setPixmap(imagen)
            auxLabel.setScaledContents(True)
            auxLabel.setAlignment(Qt.AlignCenter)
        else:
            auxLabel.setPixmap(QPixmap(""))

    def ejecutar(self) -> None:
        self.consumidor.posicionActual = 0
        self.productor.posicionActual = 0

        self.inicializarArreglo()

        qDebug(f"{self.buffer[21]}")

        while True:
            self.siguientesMovimientos()

            msg = "Turno Consumidor" if self.turno == self.TURNO_CONSUMIDOR else "Turno Productor"
            qDebug(f"{msg}")

            for i in range(self.cantidadMovimientos):
                self.delay()
                # Evaluamos de quien es turno.
                if (self.turno == self.TURNO_CONSUMIDOR):
                    if (self.consumidor.estado == self.TRABAJANDO):
                        # Intentamos realizar un consumo o una produccion. Si el metodo regresa
                        # verdadero, entonces se hizo con exito.
                        if (self.realizarAccion(self.consumidor.posicionActual, self.consumidor.consumir())):
                            self.setImagen(self.consumidor.posicionActual)
                            # Aumentamos la posicion actual del consumidor.
                            self.consumidor.posicionActual += 1

                            # qDebug(f"Consumidor: {self.consumidor.posicionActual}")
                            # Evaluamos si ya se llego al final del buffer, para reiniciar la pos.
                            if (self.consumidor.posicionActual == self.LEN_BUFFER):
                                self.consumidor.posicionActual = 0
                    
                    if (self.consumidor.estado == self.INTENTANDO):
                        self.setEtiqueta()
                        break
                
                else:
                    if (self.productor.estado == self.TRABAJANDO):
                        if (self.realizarAccion(self.productor.posicionActual, self.productor.producir())):
                            self.setImagen(self.productor.posicionActual)
                            # Aumentamos la posicion actual del consumidor.
                            self.productor.posicionActual += 1

                            # qDebug(f"Productor: {self.productor.posicionActual}")

                            if (self.productor.posicionActual == self.LEN_BUFFER):
                                self.productor.posicionActual = 0

                    if (self.productor.estado == self.INTENTANDO):
                        self.setEtiqueta()
                        break
                
                self.setEtiqueta()
                self.repaint()

    def keyPressEvent(self, event) -> None:
        if (event.key() == Qt.Key_Escape):
            qDebug("Terminar")

            self.deleteLater()
            