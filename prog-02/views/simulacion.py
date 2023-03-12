from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Simulacion(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1054, 605)
        icon = QIcon()
        icon.addFile(u"../300px-Icon-round-Question_mark.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 1061, 651))
        self.frame.setStyleSheet(u"background-color: #0A2647;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.contadorGlobalLabel = QLabel(self.frame)
        self.contadorGlobalLabel.setObjectName(u"contadorGlobalLabel")
        self.contadorGlobalLabel.setGeometry(QRect(310, 530, 241, 51))
        self.contadorGlobalLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.contadorGlobalLabel.setAlignment(Qt.AlignCenter)
        self.lotesPendientesLabel = QLabel(self.frame)
        self.lotesPendientesLabel.setObjectName(u"lotesPendientesLabel")
        self.lotesPendientesLabel.setGeometry(QRect(60, 50, 301, 71))
        self.lotesPendientesLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.lotesPendientesLabel.setAlignment(Qt.AlignCenter)
        self.loteActualLabel = QLabel(self.frame)
        self.loteActualLabel.setObjectName(u"loteActualLabel")
        self.loteActualLabel.setGeometry(QRect(110, 140, 201, 51))
        self.loteActualLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.loteActualLabel.setAlignment(Qt.AlignCenter)
        self.lotesPendientesCountLabel = QLabel(self.frame)
        self.lotesPendientesCountLabel.setObjectName(u"lotesPendientesCountLabel")
        self.lotesPendientesCountLabel.setGeometry(QRect(370, 60, 131, 51))
        self.lotesPendientesCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 18pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.lotesPendientesCountLabel.setAlignment(Qt.AlignCenter)
        self.loteActualCountLabel = QLabel(self.frame)
        self.loteActualCountLabel.setObjectName(u"loteActualCountLabel")
        self.loteActualCountLabel.setGeometry(QRect(370, 140, 131, 51))
        self.loteActualCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 18pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.loteActualCountLabel.setAlignment(Qt.AlignCenter)
        self.contadorGlobalCountLabel = QLabel(self.frame)
        self.contadorGlobalCountLabel.setObjectName(u"contadorGlobalCountLabel")
        self.contadorGlobalCountLabel.setGeometry(QRect(580, 530, 131, 51))
        self.contadorGlobalCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 11pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.contadorGlobalCountLabel.setAlignment(Qt.AlignCenter)
        self.lotesPendientesTable = QTableWidget(self.frame)
        self.lotesPendientesTable.setObjectName(u"lotesPendientesTable")
        self.lotesPendientesTable.setGeometry(QRect(30, 300, 231, 131))
        self.lotesPendientesTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(16, 159, 0);")
        self.loteActualTable = QTableWidget(self.frame)
        self.loteActualTable.setObjectName(u"loteActualTable")
        self.loteActualTable.setGeometry(QRect(360, 260, 221, 211))
        self.loteActualTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(228, 231, 30);")
        self.lotesTerminadosTable = QTableWidget(self.frame)
        self.lotesTerminadosTable.setObjectName(u"lotesTerminadosTable")
        self.lotesTerminadosTable.setGeometry(QRect(670, 60, 361, 411))
        self.lotesTerminadosTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(204, 6, 6);")
        self.decoracion = QLabel(self.frame)
        self.decoracion.setObjectName(u"decoracion")
        self.decoracion.setGeometry(QRect(110, 140, 201, 51))
        self.decoracion.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(103, 188, 171);\n"
"color: rgb(7, 184, 184);\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")
        self.decoracion_2 = QLabel(self.frame)
        self.decoracion_2.setObjectName(u"decoracion_2")
        self.decoracion_2.setGeometry(QRect(70, 60, 281, 51))
        self.decoracion_2.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(103, 188, 171);\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")
        self.decoracion_3 = QLabel(self.frame)
        self.decoracion_3.setObjectName(u"decoracion_3")
        self.decoracion_3.setGeometry(QRect(330, 530, 201, 51))
        self.decoracion_3.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(103, 188, 171);\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")
        self.lotesPendientesCountLabel_2 = QLabel(self.frame)
        self.lotesPendientesCountLabel_2.setObjectName(u"lotesPendientesCountLabel_2")
        self.lotesPendientesCountLabel_2.setGeometry(QRect(70, 500, 131, 91))
        self.lotesPendientesCountLabel_2.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 10pt \"Segoe UI\";\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: black;")
        self.lotesPendientesCountLabel_2.setAlignment(Qt.AlignCenter)
        self.simularButton = QPushButton(self.frame)
        self.simularButton.setObjectName(u"simularButton")
        self.simularButton.setGeometry(QRect(840, 540, 111, 31))
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
        self.loteActualLabel.raise_()
        self.contadorGlobalLabel.raise_()
        self.lotesPendientesLabel.raise_()
        self.lotesPendientesCountLabel.raise_()
        self.loteActualCountLabel.raise_()
        self.contadorGlobalCountLabel.raise_()
        self.lotesPendientesTable.raise_()
        self.loteActualTable.raise_()
        self.lotesTerminadosTable.raise_()
        self.decoracion_2.raise_()
        self.decoracion_3.raise_()
        self.decoracion.raise_()
        self.lotesPendientesCountLabel_2.raise_()
        self.simularButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simular", None))
        self.contadorGlobalLabel.setText(QCoreApplication.translate("Form", u"Contador Global", None))
        self.lotesPendientesLabel.setText(QCoreApplication.translate("Form", u"N\u00b0 de Lotes Pendientes", None))
        self.loteActualLabel.setText(QCoreApplication.translate("Form", u"N\u00b0 Lote Actual", None))
        self.lotesPendientesCountLabel.setText("")
        self.loteActualCountLabel.setText("")
        self.contadorGlobalCountLabel.setText("")
        self.decoracion.setText("")
        self.decoracion_2.setText("")
        self.decoracion_3.setText("")
        self.lotesPendientesCountLabel_2.setText(QCoreApplication.translate("Form", u"I - Interrumpir \n"
" P - Pausar \n"
" C - Continuar \n"
" E - Error", None))
        self.simularButton.setText(QCoreApplication.translate("Form", u"Iniciar", None))
    # retranslateUi
