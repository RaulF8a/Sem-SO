from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class MainWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 286)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 401, 291))
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
        self.agregarProcesoButton_2 = QPushButton(self.frame)
        self.agregarProcesoButton_2.setObjectName(u"agregarProcesoButton_2")
        self.agregarProcesoButton_2.setGeometry(QRect(50, 130, 131, 51))
        self.agregarProcesoButton_2.setStyleSheet(u"background-color: rgb(216, 216, 216);\n"
"font: 600 11pt \"Segoe UI Semibold\";")
        self.iniciarButton = QPushButton(self.frame)
        self.iniciarButton.setObjectName(u"iniciarButton")
        self.iniciarButton.setGeometry(QRect(230, 130, 131, 51))
        self.iniciarButton.setStyleSheet(u"background-color: rgb(216, 216, 216);\n"
"font: 600 11pt \"Segoe UI Semibold\";")
        self.limpiarButton = QPushButton(self.frame)
        self.limpiarButton.setObjectName(u"limpiarButton")
        self.limpiarButton.setGeometry(QRect(110, 220, 191, 41))
        self.limpiarButton.setAutoFillBackground(False)
        self.limpiarButton.setStyleSheet(u"background-color: rgb(198, 198, 198);\n"
"font: 600 11pt \"Segoe UI Semibold\";")

        self.retranslateUi(Form)

        self.limpiarButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tituloLabel.setText(QCoreApplication.translate("Form", u"Simular Procesamiento por Lotes", None))
        self.agregarProcesoButton_2.setText(QCoreApplication.translate("Form", u"Agregar Proceso", None))
        self.iniciarButton.setText(QCoreApplication.translate("Form", u"Iniciar Simulaci\u00f3n", None))
        self.limpiarButton.setText(QCoreApplication.translate("Form", u"Limpiar Lista de Procesos", None))
    # retranslateUi

