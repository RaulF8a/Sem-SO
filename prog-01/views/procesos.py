# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'procesosqihVzS.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Procesos(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(574, 429)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 581, 431))
        self.frame.setStyleSheet(u"background-color: #0A2647;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nombreLabel = QLabel(self.frame)
        self.nombreLabel.setObjectName(u"nombreLabel")
        self.nombreLabel.setGeometry(QRect(70, 40, 131, 31))
        self.nombreLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.nombreLabel.setAlignment(Qt.AlignCenter)
        self.operacionLabel = QLabel(self.frame)
        self.operacionLabel.setObjectName(u"operacionLabel")
        self.operacionLabel.setGeometry(QRect(70, 100, 131, 31))
        self.operacionLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.operacionLabel.setAlignment(Qt.AlignCenter)
        self.tiempoLabel = QLabel(self.frame)
        self.tiempoLabel.setObjectName(u"tiempoLabel")
        self.tiempoLabel.setGeometry(QRect(20, 160, 231, 31))
        self.tiempoLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.tiempoLabel.setAlignment(Qt.AlignCenter)
        self.idLabel = QLabel(self.frame)
        self.idLabel.setObjectName(u"idLabel")
        self.idLabel.setGeometry(QRect(60, 220, 151, 31))
        self.idLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: white;")
        self.idLabel.setAlignment(Qt.AlignCenter)
        self.nombreLineEdit = QLineEdit(self.frame)
        self.nombreLineEdit.setObjectName(u"nombreLineEdit")
        self.nombreLineEdit.setGeometry(QRect(320, 40, 211, 31))
        self.nombreLineEdit.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Segoe UI Historic\";")
        self.operacionLineEdit = QLineEdit(self.frame)
        self.operacionLineEdit.setObjectName(u"operacionLineEdit")
        self.operacionLineEdit.setGeometry(QRect(320, 100, 211, 31))
        self.operacionLineEdit.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Segoe UI Historic\";")
        self.tiempoLineEdit = QLineEdit(self.frame)
        self.tiempoLineEdit.setObjectName(u"tiempoLineEdit")
        self.tiempoLineEdit.setGeometry(QRect(320, 160, 211, 31))
        self.tiempoLineEdit.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Segoe UI Historic\";")
        self.identificadorLineEdit = QLineEdit(self.frame)
        self.identificadorLineEdit.setObjectName(u"identificadorLineEdit")
        self.identificadorLineEdit.setGeometry(QRect(320, 220, 211, 31))
        self.identificadorLineEdit.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Segoe UI Historic\";")
        self.agregarButton = QPushButton(self.frame)
        self.agregarButton.setObjectName(u"agregarButton")
        self.agregarButton.setGeometry(QRect(220, 290, 141, 31))
        self.agregarButton.setStyleSheet(u"background-color: rgb(189, 189, 189);\n"
"font: 600 11pt \"Segoe UI Semibold\";")
        self.errorLabel = QLabel(self.frame)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(110, 340, 361, 61))
        self.errorLabel.setStyleSheet(u"background-color: white;\n"
"font: 600 11pt \"Segoe UI Semibold\";")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nombreLabel.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.operacionLabel.setText(QCoreApplication.translate("Form", u"Operaci\u00f3n", None))
        self.tiempoLabel.setText(QCoreApplication.translate("Form", u"Tiempo M\u00e1ximo Estimado", None))
        self.idLabel.setText(QCoreApplication.translate("Form", u"Identificador", None))
        self.agregarButton.setText(QCoreApplication.translate("Form", u"Agregar", None))
        self.errorLabel.setText("")
    # retranslateUi