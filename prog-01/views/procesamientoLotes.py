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

class ProcesamientoLotes(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1054, 644)
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
        self.loteActualLabel.setGeometry(QRect(100, 140, 201, 51))
        self.loteActualLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.loteActualLabel.setAlignment(Qt.AlignCenter)
        self.lotesPendientesCountLabel = QLabel(self.frame)
        self.lotesPendientesCountLabel.setObjectName(u"lotesPendientesCountLabel")
        self.lotesPendientesCountLabel.setGeometry(QRect(370, 60, 131, 51))
        self.lotesPendientesCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 18pt \"Segoe UI\";")
        self.lotesPendientesCountLabel.setAlignment(Qt.AlignCenter)
        self.loteActualCountLabel = QLabel(self.frame)
        self.loteActualCountLabel.setObjectName(u"loteActualCountLabel")
        self.loteActualCountLabel.setGeometry(QRect(370, 140, 131, 51))
        self.loteActualCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 18pt \"Segoe UI\";")
        self.loteActualCountLabel.setAlignment(Qt.AlignCenter)
        self.contadorGlobalCountLabel = QLabel(self.frame)
        self.contadorGlobalCountLabel.setObjectName(u"contadorGlobalCountLabel")
        self.contadorGlobalCountLabel.setGeometry(QRect(580, 530, 131, 51))
        self.contadorGlobalCountLabel.setStyleSheet(u"background-color: #EFF5F5;\n"
"font: 700 18pt \"Segoe UI\";")
        self.contadorGlobalCountLabel.setAlignment(Qt.AlignCenter)
        self.lotesPendientesTable = QTableWidget(self.frame)
        self.lotesPendientesTable.setObjectName(u"lotesPendientesTable")
        self.lotesPendientesTable.setGeometry(QRect(30, 300, 231, 131))
        self.lotesPendientesTable.setStyleSheet(u"background-color: white;")
        self.loteActualTable = QTableWidget(self.frame)
        self.loteActualTable.setObjectName(u"loteActualTable")
        self.loteActualTable.setGeometry(QRect(360, 260, 221, 211))
        self.loteActualTable.setStyleSheet(u"background-color: white;")
        self.lotesTerminadosTable = QTableWidget(self.frame)
        self.lotesTerminadosTable.setObjectName(u"lotesTerminadosTable")
        self.lotesTerminadosTable.setGeometry(QRect(670, 60, 361, 411))
        self.lotesTerminadosTable.setStyleSheet(u"background-color: white;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 530, 121, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(216, 216, 216);\n"
"font: 600 11pt \"Segoe UI Semibold\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.contadorGlobalLabel.setText(QCoreApplication.translate("Form", u"Contador Global", None))
        self.lotesPendientesLabel.setText(QCoreApplication.translate("Form", u"N\u00b0 de Lotes Pendientes", None))
        self.loteActualLabel.setText(QCoreApplication.translate("Form", u"N\u00b0 Lote Actual", None))
        self.lotesPendientesCountLabel.setText("")
        self.loteActualCountLabel.setText("")
        self.contadorGlobalCountLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Comenzar", None))
    # retranslateUi

