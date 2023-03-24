from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class MainWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(939, 680)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 941, 681))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.productorLabel = QLabel(self.frame)
        self.productorLabel.setObjectName(u"productorLabel")
        self.productorLabel.setGeometry(QRect(200, 220, 111, 41))
        self.productorLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"")
        self.productorLabel.setAlignment(Qt.AlignCenter)
        self.consumidorLabel = QLabel(self.frame)
        self.consumidorLabel.setObjectName(u"consumidorLabel")
        self.consumidorLabel.setGeometry(QRect(630, 220, 131, 41))
        self.consumidorLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"")
        self.consumidorLabel.setAlignment(Qt.AlignCenter)
        self.imagenProductorLabel = QLabel(self.frame)
        self.imagenProductorLabel.setObjectName(u"imagenProductorLabel")
        self.imagenProductorLabel.setGeometry(QRect(140, 30, 231, 181))
        self.imagenProductorLabel.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.imagenProductorLabel.setAlignment(Qt.AlignCenter)
        self.imagenConsumidorLabel = QLabel(self.frame)
        self.imagenConsumidorLabel.setObjectName(u"imagenConsumidorLabel")
        self.imagenConsumidorLabel.setGeometry(QRect(580, 30, 231, 181))
        self.imagenConsumidorLabel.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.imagenConsumidorLabel.setAlignment(Qt.AlignCenter)
        self.estadoProductorLabel = QLabel(self.frame)
        self.estadoProductorLabel.setObjectName(u"estadoProductorLabel")
        self.estadoProductorLabel.setGeometry(QRect(190, 260, 131, 31))
        self.estadoProductorLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"")
        self.estadoProductorLabel.setAlignment(Qt.AlignCenter)
        self.estadoConsumidorLabel = QLabel(self.frame)
        self.estadoConsumidorLabel.setObjectName(u"estadoConsumidorLabel")
        self.estadoConsumidorLabel.setGeometry(QRect(630, 260, 131, 31))
        self.estadoConsumidorLabel.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"")
        self.estadoConsumidorLabel.setAlignment(Qt.AlignCenter)
        self.buffer1Label = QLabel(self.frame)
        self.buffer1Label.setObjectName(u"buffer1Label")
        self.buffer1Label.setGeometry(QRect(80, 330, 71, 71))
        self.buffer1Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer2Label = QLabel(self.frame)
        self.buffer2Label.setObjectName(u"buffer2Label")
        self.buffer2Label.setGeometry(QRect(170, 330, 71, 71))
        self.buffer2Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer3Label = QLabel(self.frame)
        self.buffer3Label.setObjectName(u"buffer3Label")
        self.buffer3Label.setGeometry(QRect(260, 330, 71, 71))
        self.buffer3Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer5Label = QLabel(self.frame)
        self.buffer5Label.setObjectName(u"buffer5Label")
        self.buffer5Label.setGeometry(QRect(440, 330, 71, 71))
        self.buffer5Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer4Label = QLabel(self.frame)
        self.buffer4Label.setObjectName(u"buffer4Label")
        self.buffer4Label.setGeometry(QRect(350, 330, 71, 71))
        self.buffer4Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer6Label = QLabel(self.frame)
        self.buffer6Label.setObjectName(u"buffer6Label")
        self.buffer6Label.setGeometry(QRect(530, 330, 71, 71))
        self.buffer6Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer7Label = QLabel(self.frame)
        self.buffer7Label.setObjectName(u"buffer7Label")
        self.buffer7Label.setGeometry(QRect(620, 330, 71, 71))
        self.buffer7Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer8Label = QLabel(self.frame)
        self.buffer8Label.setObjectName(u"buffer8Label")
        self.buffer8Label.setGeometry(QRect(710, 330, 71, 71))
        self.buffer8Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer9Label = QLabel(self.frame)
        self.buffer9Label.setObjectName(u"buffer9Label")
        self.buffer9Label.setGeometry(QRect(800, 330, 71, 71))
        self.buffer9Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer11Label = QLabel(self.frame)
        self.buffer11Label.setObjectName(u"buffer11Label")
        self.buffer11Label.setGeometry(QRect(170, 450, 71, 71))
        self.buffer11Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer10Label = QLabel(self.frame)
        self.buffer10Label.setObjectName(u"buffer10Label")
        self.buffer10Label.setGeometry(QRect(80, 450, 71, 71))
        self.buffer10Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer13Label = QLabel(self.frame)
        self.buffer13Label.setObjectName(u"buffer13Label")
        self.buffer13Label.setGeometry(QRect(350, 450, 71, 71))
        self.buffer13Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer17Label = QLabel(self.frame)
        self.buffer17Label.setObjectName(u"buffer17Label")
        self.buffer17Label.setGeometry(QRect(710, 450, 71, 71))
        self.buffer17Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer16Label = QLabel(self.frame)
        self.buffer16Label.setObjectName(u"buffer16Label")
        self.buffer16Label.setGeometry(QRect(620, 450, 71, 71))
        self.buffer16Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer12Label = QLabel(self.frame)
        self.buffer12Label.setObjectName(u"buffer12Label")
        self.buffer12Label.setGeometry(QRect(260, 450, 71, 71))
        self.buffer12Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer14Label = QLabel(self.frame)
        self.buffer14Label.setObjectName(u"buffer14Label")
        self.buffer14Label.setGeometry(QRect(440, 450, 71, 71))
        self.buffer14Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer18Label = QLabel(self.frame)
        self.buffer18Label.setObjectName(u"buffer18Label")
        self.buffer18Label.setGeometry(QRect(800, 450, 71, 71))
        self.buffer18Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer15Label = QLabel(self.frame)
        self.buffer15Label.setObjectName(u"buffer15Label")
        self.buffer15Label.setGeometry(QRect(530, 450, 71, 71))
        self.buffer15Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer20Label = QLabel(self.frame)
        self.buffer20Label.setObjectName(u"buffer20Label")
        self.buffer20Label.setGeometry(QRect(400, 570, 71, 71))
        self.buffer20Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer22Label = QLabel(self.frame)
        self.buffer22Label.setObjectName(u"buffer22Label")
        self.buffer22Label.setGeometry(QRect(580, 570, 71, 71))
        self.buffer22Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer21Label = QLabel(self.frame)
        self.buffer21Label.setObjectName(u"buffer21Label")
        self.buffer21Label.setGeometry(QRect(490, 570, 71, 71))
        self.buffer21Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.buffer19Label = QLabel(self.frame)
        self.buffer19Label.setObjectName(u"buffer19Label")
        self.buffer19Label.setGeometry(QRect(310, 570, 71, 71))
        self.buffer19Label.setStyleSheet(u"background-color: white;\n"
"border-style: outset;\n"
"border-width:2px;\n"
"border-color: black;")
        self.numeroBufferLabel = QLabel(self.frame)
        self.numeroBufferLabel.setObjectName(u"numeroBufferLabel")
        self.numeroBufferLabel.setGeometry(QRect(90, 410, 51, 21))
        self.numeroBufferLabel.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_2 = QLabel(self.frame)
        self.numeroBufferLabel_2.setObjectName(u"numeroBufferLabel_2")
        self.numeroBufferLabel_2.setGeometry(QRect(180, 410, 51, 21))
        self.numeroBufferLabel_2.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_2.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_3 = QLabel(self.frame)
        self.numeroBufferLabel_3.setObjectName(u"numeroBufferLabel_3")
        self.numeroBufferLabel_3.setGeometry(QRect(270, 410, 51, 21))
        self.numeroBufferLabel_3.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_3.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_4 = QLabel(self.frame)
        self.numeroBufferLabel_4.setObjectName(u"numeroBufferLabel_4")
        self.numeroBufferLabel_4.setGeometry(QRect(360, 410, 51, 21))
        self.numeroBufferLabel_4.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_4.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_5 = QLabel(self.frame)
        self.numeroBufferLabel_5.setObjectName(u"numeroBufferLabel_5")
        self.numeroBufferLabel_5.setGeometry(QRect(450, 410, 51, 21))
        self.numeroBufferLabel_5.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_5.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_6 = QLabel(self.frame)
        self.numeroBufferLabel_6.setObjectName(u"numeroBufferLabel_6")
        self.numeroBufferLabel_6.setGeometry(QRect(540, 410, 51, 21))
        self.numeroBufferLabel_6.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_6.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_7 = QLabel(self.frame)
        self.numeroBufferLabel_7.setObjectName(u"numeroBufferLabel_7")
        self.numeroBufferLabel_7.setGeometry(QRect(630, 410, 51, 21))
        self.numeroBufferLabel_7.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_7.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_8 = QLabel(self.frame)
        self.numeroBufferLabel_8.setObjectName(u"numeroBufferLabel_8")
        self.numeroBufferLabel_8.setGeometry(QRect(720, 410, 51, 21))
        self.numeroBufferLabel_8.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_8.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_9 = QLabel(self.frame)
        self.numeroBufferLabel_9.setObjectName(u"numeroBufferLabel_9")
        self.numeroBufferLabel_9.setGeometry(QRect(810, 410, 51, 21))
        self.numeroBufferLabel_9.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_9.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_10 = QLabel(self.frame)
        self.numeroBufferLabel_10.setObjectName(u"numeroBufferLabel_10")
        self.numeroBufferLabel_10.setGeometry(QRect(810, 530, 51, 21))
        self.numeroBufferLabel_10.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_10.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_11 = QLabel(self.frame)
        self.numeroBufferLabel_11.setObjectName(u"numeroBufferLabel_11")
        self.numeroBufferLabel_11.setGeometry(QRect(180, 530, 51, 21))
        self.numeroBufferLabel_11.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_11.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_12 = QLabel(self.frame)
        self.numeroBufferLabel_12.setObjectName(u"numeroBufferLabel_12")
        self.numeroBufferLabel_12.setGeometry(QRect(450, 530, 51, 21))
        self.numeroBufferLabel_12.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_12.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_13 = QLabel(self.frame)
        self.numeroBufferLabel_13.setObjectName(u"numeroBufferLabel_13")
        self.numeroBufferLabel_13.setGeometry(QRect(630, 530, 51, 21))
        self.numeroBufferLabel_13.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_13.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_14 = QLabel(self.frame)
        self.numeroBufferLabel_14.setObjectName(u"numeroBufferLabel_14")
        self.numeroBufferLabel_14.setGeometry(QRect(270, 530, 51, 21))
        self.numeroBufferLabel_14.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_14.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_15 = QLabel(self.frame)
        self.numeroBufferLabel_15.setObjectName(u"numeroBufferLabel_15")
        self.numeroBufferLabel_15.setGeometry(QRect(360, 530, 51, 21))
        self.numeroBufferLabel_15.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_15.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_16 = QLabel(self.frame)
        self.numeroBufferLabel_16.setObjectName(u"numeroBufferLabel_16")
        self.numeroBufferLabel_16.setGeometry(QRect(540, 530, 51, 21))
        self.numeroBufferLabel_16.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_16.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_17 = QLabel(self.frame)
        self.numeroBufferLabel_17.setObjectName(u"numeroBufferLabel_17")
        self.numeroBufferLabel_17.setGeometry(QRect(720, 530, 51, 21))
        self.numeroBufferLabel_17.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_17.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_18 = QLabel(self.frame)
        self.numeroBufferLabel_18.setObjectName(u"numeroBufferLabel_18")
        self.numeroBufferLabel_18.setGeometry(QRect(90, 530, 51, 21))
        self.numeroBufferLabel_18.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_18.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_19 = QLabel(self.frame)
        self.numeroBufferLabel_19.setObjectName(u"numeroBufferLabel_19")
        self.numeroBufferLabel_19.setGeometry(QRect(320, 650, 51, 21))
        self.numeroBufferLabel_19.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_19.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_20 = QLabel(self.frame)
        self.numeroBufferLabel_20.setObjectName(u"numeroBufferLabel_20")
        self.numeroBufferLabel_20.setGeometry(QRect(410, 650, 51, 21))
        self.numeroBufferLabel_20.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_20.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_21 = QLabel(self.frame)
        self.numeroBufferLabel_21.setObjectName(u"numeroBufferLabel_21")
        self.numeroBufferLabel_21.setGeometry(QRect(500, 650, 51, 21))
        self.numeroBufferLabel_21.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_21.setAlignment(Qt.AlignCenter)
        self.numeroBufferLabel_22 = QLabel(self.frame)
        self.numeroBufferLabel_22.setObjectName(u"numeroBufferLabel_22")
        self.numeroBufferLabel_22.setGeometry(QRect(590, 650, 51, 21))
        self.numeroBufferLabel_22.setStyleSheet(u"font: 700 10pt \"Segoe UI\";\n"
"")
        self.numeroBufferLabel_22.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.productorLabel.setText(QCoreApplication.translate("Form", u"Productor", None))
        self.consumidorLabel.setText(QCoreApplication.translate("Form", u"Consumidor", None))
        self.imagenProductorLabel.setText("")
        self.imagenConsumidorLabel.setText("")
        self.estadoProductorLabel.setText("")
        self.estadoConsumidorLabel.setText("")
        self.buffer1Label.setText("")
        self.buffer2Label.setText("")
        self.buffer3Label.setText("")
        self.buffer5Label.setText("")
        self.buffer4Label.setText("")
        self.buffer6Label.setText("")
        self.buffer7Label.setText("")
        self.buffer8Label.setText("")
        self.buffer9Label.setText("")
        self.buffer11Label.setText("")
        self.buffer10Label.setText("")
        self.buffer13Label.setText("")
        self.buffer17Label.setText("")
        self.buffer16Label.setText("")
        self.buffer12Label.setText("")
        self.buffer14Label.setText("")
        self.buffer18Label.setText("")
        self.buffer15Label.setText("")
        self.buffer20Label.setText("")
        self.buffer22Label.setText("")
        self.buffer21Label.setText("")
        self.buffer19Label.setText("")
        self.numeroBufferLabel.setText(QCoreApplication.translate("Form", u"1", None))
        self.numeroBufferLabel_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.numeroBufferLabel_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.numeroBufferLabel_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.numeroBufferLabel_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.numeroBufferLabel_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.numeroBufferLabel_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.numeroBufferLabel_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.numeroBufferLabel_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.numeroBufferLabel_10.setText(QCoreApplication.translate("Form", u"18", None))
        self.numeroBufferLabel_11.setText(QCoreApplication.translate("Form", u"11", None))
        self.numeroBufferLabel_12.setText(QCoreApplication.translate("Form", u"14", None))
        self.numeroBufferLabel_13.setText(QCoreApplication.translate("Form", u"16", None))
        self.numeroBufferLabel_14.setText(QCoreApplication.translate("Form", u"12", None))
        self.numeroBufferLabel_15.setText(QCoreApplication.translate("Form", u"13", None))
        self.numeroBufferLabel_16.setText(QCoreApplication.translate("Form", u"15", None))
        self.numeroBufferLabel_17.setText(QCoreApplication.translate("Form", u"17", None))
        self.numeroBufferLabel_18.setText(QCoreApplication.translate("Form", u"10", None))
        self.numeroBufferLabel_19.setText(QCoreApplication.translate("Form", u"19", None))
        self.numeroBufferLabel_20.setText(QCoreApplication.translate("Form", u"20", None))
        self.numeroBufferLabel_21.setText(QCoreApplication.translate("Form", u"21", None))
        self.numeroBufferLabel_22.setText(QCoreApplication.translate("Form", u"22", None))
    # retranslateUi

