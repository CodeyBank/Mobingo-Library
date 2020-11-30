# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newOperation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Dialog_newOperation(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(750, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(750, 600))
        Dialog.setMaximumSize(QSize(750, 600))
        Dialog.setStyleSheet(u"background-color: rgb(40, 41, 53)")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 751, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Montserrat Semibold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background:none;\n"
"font: 57 14pt \"Montserrat Semibold\";\n"
"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 50, 750, 461))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(430, 10, 282, 24))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.transactionID = QLabel(self.layoutWidget)
        self.transactionID.setObjectName(u"transactionID")
        self.transactionID.setMinimumSize(QSize(120, 0))
        font2 = QFont()
        font2.setFamily(u"Roboto Light")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.transactionID.setFont(font2)
        self.transactionID.setStyleSheet(u"background-color: transparent;\n"
"\n"
"color: white;")
        self.transactionID.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.transactionID, 0, 1, 1, 1)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 60, 471, 381))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setMaximumSize(QSize(470, 35))
        font3 = QFont()
        font3.setFamily(u"Montserrat Light")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(3)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"border: 0px; \n"
"border-radius: 9px;\n"
"color: white;\n"
"font: 25 10pt \"Montserrat Light\";")

        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 35))
        self.lineEdit_3.setMaximumSize(QSize(470, 35))
        self.lineEdit_3.setFont(font3)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"border: 0px; \n"
"border-radius: 9px;\n"
"color: white;\n"
"font: 25 10pt \"Montserrat Light\";")

        self.gridLayout_3.addWidget(self.lineEdit_3, 2, 0, 1, 2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 35))
        self.comboBox.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setFamily(u"Montserrat Light")
        font4.setPointSize(10)
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color:white;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 2)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 35))
        self.lineEdit_5.setMaximumSize(QSize(470, 35))
        self.lineEdit_5.setFont(font3)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"border: 0px; \n"
"border-radius: 9px;\n"
"color: white;\n"
"font: 25 10pt \"Montserrat Light\";")

        self.gridLayout_3.addWidget(self.lineEdit_5, 4, 0, 1, 2)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 35))
        self.spinBox.setMaximumSize(QSize(100, 35))
        self.spinBox.setStyleSheet(u"QSpinBox {\n"
"    border-width: 2;\n"
"	color: white;\n"
"	font: 25 10pt \"Montserrat Light\";\n"
"	border-color:rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"")
        self.spinBox.setMaximum(30)

        self.gridLayout_3.addWidget(self.spinBox, 3, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color:white;")

        self.gridLayout_3.addWidget(self.label_3, 3, 1, 1, 1)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 30))
        self.textEdit.setMaximumSize(QSize(16777215, 150))
        self.textEdit.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"border: 0px; \n"
"border-radius: 9px;\n"
"color: white;\n"
"font: 25 10pt \"Montserrat Light\";")
        self.textEdit.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.textEdit, 5, 0, 1, 2)

        self.addButton = QPushButton(Dialog)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(240, 540, 131, 30))
        self.addButton.setMinimumSize(QSize(0, 30))
        self.addButton.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamily(u"Montserrat Light")
        font5.setPointSize(12)
        self.addButton.setFont(font5)
        self.addButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 100), stop:0.984012 rgba(98, 114, 164, 100));\n"
"border-style: inset;\n"
"}")
        self.closeBtn = QPushButton(Dialog)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(400, 540, 131, 30))
        self.closeBtn.setMinimumSize(QSize(0, 30))
        self.closeBtn.setMaximumSize(QSize(16777215, 30))
        self.closeBtn.setFont(font5)
        self.closeBtn.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 100), stop:0.984012 rgba(98, 114, 164, 100));\n"
"border-style: inset;\n"
"}")
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.addButton)
        QWidget.setTabOrder(self.addButton, self.closeBtn)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"New Operation", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Transaction ID", None))
        self.transactionID.setText(QCoreApplication.translate("Dialog", u"##########", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Client ", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Book ID", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select operation type", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Burrow", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Return", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Use in Library", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Buy", None))

        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"Location", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Number of Days", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter relevant comments and remarks", None))
        self.addButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.closeBtn.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

