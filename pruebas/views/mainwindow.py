from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class MainWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1054, 714)
        icon = QIcon()
        icon.addFile(u"../300px-Icon-round-Question_mark.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 1061, 731))
        self.frame.setStyleSheet(u"background-color: #0A2647;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.contadorGlobalLabel = QLabel(self.frame)
        self.contadorGlobalLabel.setObjectName(u"contadorGlobalLabel")
        self.contadorGlobalLabel.setGeometry(QRect(590, 160, 241, 51))
        self.contadorGlobalLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.contadorGlobalLabel.setAlignment(Qt.AlignCenter)
        self.procesosNuevosLabel = QLabel(self.frame)
        self.procesosNuevosLabel.setObjectName(u"procesosNuevosLabel")
        self.procesosNuevosLabel.setGeometry(QRect(60, 150, 301, 71))
        self.procesosNuevosLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.procesosNuevosLabel.setAlignment(Qt.AlignCenter)
        self.procesosNuevosCountLabel = QLabel(self.frame)
        self.procesosNuevosCountLabel.setObjectName(u"procesosNuevosCountLabel")
        self.procesosNuevosCountLabel.setGeometry(QRect(370, 160, 131, 51))
        self.procesosNuevosCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 18pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.procesosNuevosCountLabel.setAlignment(Qt.AlignCenter)
        self.contadorGlobalCountLabel = QLabel(self.frame)
        self.contadorGlobalCountLabel.setObjectName(u"contadorGlobalCountLabel")
        self.contadorGlobalCountLabel.setGeometry(QRect(860, 160, 131, 51))
        self.contadorGlobalCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 18pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.contadorGlobalCountLabel.setAlignment(Qt.AlignCenter)
        self.procesosListosTable = QTableWidget(self.frame)
        self.procesosListosTable.setObjectName(u"procesosListosTable")
        self.procesosListosTable.setGeometry(QRect(40, 280, 231, 181))
        self.procesosListosTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(16, 159, 0);")
        self.procesoActualTable = QTableWidget(self.frame)
        self.procesoActualTable.setObjectName(u"procesoActualTable")
        self.procesoActualTable.setGeometry(QRect(350, 340, 231, 281))
        self.procesoActualTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(228, 231, 30);")
        self.procesosTerminadosTable = QTableWidget(self.frame)
        self.procesosTerminadosTable.setObjectName(u"procesosTerminadosTable")
        self.procesosTerminadosTable.setGeometry(QRect(670, 280, 351, 401))
        self.procesosTerminadosTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(204, 6, 6);")
        self.decoracion_2 = QLabel(self.frame)
        self.decoracion_2.setObjectName(u"decoracion_2")
        self.decoracion_2.setGeometry(QRect(70, 160, 281, 51))
        self.decoracion_2.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(103, 188, 171);\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")
        self.decoracion_3 = QLabel(self.frame)
        self.decoracion_3.setObjectName(u"decoracion_3")
        self.decoracion_3.setGeometry(QRect(610, 160, 201, 51))
        self.decoracion_3.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(103, 188, 171);\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")
        self.teclasLabel = QLabel(self.frame)
        self.teclasLabel.setObjectName(u"teclasLabel")
        self.teclasLabel.setGeometry(QRect(720, 20, 261, 91))
        self.teclasLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 10pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.teclasLabel.setAlignment(Qt.AlignCenter)
        self.simularButton = QPushButton(self.frame)
        self.simularButton.setObjectName(u"simularButton")
        self.simularButton.setGeometry(QRect(510, 40, 121, 51))
        self.simularButton.setMouseTracking(True)
        self.simularButton.setAcceptDrops(False)
        self.simularButton.setStyleSheet(u"QPushButton {background-color:red;\n"
"color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"padding :6px min-width;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(179, 46, 46);\n"
"}")
        self.decoracion_4 = QLabel(self.frame)
        self.decoracion_4.setObjectName(u"decoracion_4")
        self.decoracion_4.setGeometry(QRect(70, 40, 281, 51))
        self.decoracion_4.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(0, 187, 255);\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")
        self.cantidadProcesosLabel = QLabel(self.frame)
        self.cantidadProcesosLabel.setObjectName(u"cantidadProcesosLabel")
        self.cantidadProcesosLabel.setGeometry(QRect(90, 40, 241, 51))
        self.cantidadProcesosLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.cantidadProcesosLabel.setAlignment(Qt.AlignCenter)
        self.procesosBloqueadosTable = QTableWidget(self.frame)
        self.procesosBloqueadosTable.setObjectName(u"procesosBloqueadosTable")
        self.procesosBloqueadosTable.setGeometry(QRect(40, 510, 231, 181))
        self.procesosBloqueadosTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(254, 173, 32);")
        self.procesosListosTableLabel = QLabel(self.frame)
        self.procesosListosTableLabel.setObjectName(u"procesosListosTableLabel")
        self.procesosListosTableLabel.setGeometry(QRect(90, 240, 131, 31))
        self.procesosListosTableLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.procesosListosTableLabel.setAlignment(Qt.AlignCenter)
        self.procesosBloqueadosTableLabel = QLabel(self.frame)
        self.procesosBloqueadosTableLabel.setObjectName(u"procesosBloqueadosTableLabel")
        self.procesosBloqueadosTableLabel.setGeometry(QRect(90, 470, 131, 31))
        self.procesosBloqueadosTableLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.procesosBloqueadosTableLabel.setAlignment(Qt.AlignCenter)
        self.procesoActualTableLabel = QLabel(self.frame)
        self.procesoActualTableLabel.setObjectName(u"procesoActualTableLabel")
        self.procesoActualTableLabel.setGeometry(QRect(400, 300, 131, 31))
        self.procesoActualTableLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.procesoActualTableLabel.setAlignment(Qt.AlignCenter)
        self.procesosTerminadosTableLabel = QLabel(self.frame)
        self.procesosTerminadosTableLabel.setObjectName(u"procesosTerminadosTableLabel")
        self.procesosTerminadosTableLabel.setGeometry(QRect(780, 240, 131, 31))
        self.procesosTerminadosTableLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.procesosTerminadosTableLabel.setAlignment(Qt.AlignCenter)
        self.cantidadProcesosLineEdit = QLineEdit(self.frame)
        self.cantidadProcesosLineEdit.setObjectName(u"cantidadProcesosLineEdit")
        self.cantidadProcesosLineEdit.setGeometry(QRect(380, 40, 101, 51))
        self.cantidadProcesosLineEdit.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 12pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.cantidadProcesosLineEdit.setAlignment(Qt.AlignCenter)
        self.cantidadProcesosLabel.raise_()
        self.contadorGlobalLabel.raise_()
        self.procesosNuevosLabel.raise_()
        self.procesosNuevosCountLabel.raise_()
        self.contadorGlobalCountLabel.raise_()
        self.procesosListosTable.raise_()
        self.procesoActualTable.raise_()
        self.procesosTerminadosTable.raise_()
        self.decoracion_2.raise_()
        self.decoracion_3.raise_()
        self.teclasLabel.raise_()
        self.simularButton.raise_()
        self.decoracion_4.raise_()
        self.procesosBloqueadosTable.raise_()
        self.procesosListosTableLabel.raise_()
        self.procesosBloqueadosTableLabel.raise_()
        self.procesoActualTableLabel.raise_()
        self.procesosTerminadosTableLabel.raise_()
        self.cantidadProcesosLineEdit.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simular", None))
        self.contadorGlobalLabel.setText(QCoreApplication.translate("Form", u"Contador Global", None))
        self.procesosNuevosLabel.setText(QCoreApplication.translate("Form", u"N\u00b0 Procesos Nuevos", None))
        self.procesosNuevosCountLabel.setText("")
        self.contadorGlobalCountLabel.setText("")
        self.decoracion_2.setText("")
        self.decoracion_3.setText("")
        self.teclasLabel.setText(QCoreApplication.translate("Form", u"I - Interrumpir   P - Pausar \n"
"C - Continuar   E - Error", None))
        self.simularButton.setText(QCoreApplication.translate("Form", u"Iniciar", None))
        self.decoracion_4.setText("")
        self.cantidadProcesosLabel.setText(QCoreApplication.translate("Form", u"# de Procesos a Crear", None))
        self.procesosListosTableLabel.setText(QCoreApplication.translate("Form", u"Listos", None))
        self.procesosBloqueadosTableLabel.setText(QCoreApplication.translate("Form", u"Bloqueados", None))
        self.procesoActualTableLabel.setText(QCoreApplication.translate("Form", u"Ejecuci\u00f3n", None))
        self.procesosTerminadosTableLabel.setText(QCoreApplication.translate("Form", u"Terminados", None))
    # retranslateUi

