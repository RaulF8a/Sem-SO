from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Tabla_Procesos(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(910, 503)
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
        self.tablaProcesosTable = QTableWidget(self.frame)
        self.tablaProcesosTable.setObjectName(u"tablaProcesosTable")
        self.tablaProcesosTable.setGeometry(QRect(20, 90, 871, 381))
        self.tablaProcesosTable.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(255, 0, 221);")
        self.tablaProcesosLabel = QLabel(self.frame)
        self.tablaProcesosLabel.setObjectName(u"tablaProcesosLabel")
        self.tablaProcesosLabel.setGeometry(QRect(330, 20, 251, 51))
        self.tablaProcesosLabel.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: white;")
        self.tablaProcesosLabel.setAlignment(Qt.AlignCenter)
        self.decoracion = QLabel(self.frame)
        self.decoracion.setObjectName(u"decoracion")
        self.decoracion.setGeometry(QRect(320, 20, 271, 51))
        self.decoracion.setStyleSheet(u"border-style: outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color: rgb(156, 149, 255);\n"
"border-top:none;\n"
"background-color:rgba(255,255,255,0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Tabla de Procesos", None))
        self.tablaProcesosLabel.setText(QCoreApplication.translate("Form", u"Tabla de Procesos", None))
        self.decoracion.setText("")
    # retranslateUi

