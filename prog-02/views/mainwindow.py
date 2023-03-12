from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class MainWindow(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(400, 286)
        icon = QIcon()
        icon.addFile(u"./300px-Icon-round-Question_mark.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        widget.setWindowIcon(icon)
        self.frame = QFrame(widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 401, 291))
        self.frame.setStyleSheet(u"background-color: #0A2647;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tituloLabel = QLabel(self.frame)
        self.tituloLabel.setObjectName(u"tituloLabel")
        self.tituloLabel.setGeometry(QRect(50, 20, 321, 71))
        self.tituloLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white")
        self.tituloLabel.setAlignment(Qt.AlignCenter)
        self.tituloLabel.setWordWrap(True)
        self.contadorProcesosSpinBox = QSpinBox(self.frame)
        self.contadorProcesosSpinBox.setObjectName(u"contadorProcesosSpinBox")
        self.contadorProcesosSpinBox.setGeometry(QRect(250, 150, 81, 31))
        self.contadorProcesosSpinBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 600 14pt \"Segoe UI Semibold\";")
        self.contadorProcesosSpinBox.setAlignment(Qt.AlignCenter)
        self.contadorProcesosSpinBox.setMinimum(1)
        self.cantidadProcesosLabel = QLabel(self.frame)
        self.cantidadProcesosLabel.setObjectName(u"cantidadProcesosLabel")
        self.cantidadProcesosLabel.setGeometry(QRect(60, 150, 181, 31))
        self.cantidadProcesosLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: white")
        self.cantidadProcesosLabel.setAlignment(Qt.AlignCenter)
        self.cantidadProcesosLabel.setWordWrap(True)
        self.simularButton = QPushButton(self.frame)
        self.simularButton.setObjectName(u"simularButton")
        self.simularButton.setGeometry(QRect(150, 230, 111, 31))
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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 321, 71))
        self.label.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: white;\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")
        self.contadorProcesosSpinBox.raise_()
        self.cantidadProcesosLabel.raise_()
        self.simularButton.raise_()
        self.tituloLabel.raise_()
        self.label.raise_()

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Procesamiento por Lotes", None))
        self.tituloLabel.setText(QCoreApplication.translate("widget", u"Procesamiento por Lotes con Multiprogramaci\u00f3n", None))
        self.cantidadProcesosLabel.setText(QCoreApplication.translate("widget", u"Cantidad de Procesos", None))
        self.simularButton.setText(QCoreApplication.translate("widget", u"Simular", None))
        self.label.setText("")
    # retranslateUi

