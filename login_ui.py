# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(600, 400))
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"background-color: rgb(52, 54, 68);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.signUpBtn = QPushButton(self.frame)
        self.signUpBtn.setObjectName(u"signUpBtn")
        self.signUpBtn.setGeometry(QRect(510, 0, 40, 40))
        self.signUpBtn.setMinimumSize(QSize(40, 40))
        self.signUpBtn.setMaximumSize(QSize(40, 40))
        self.signUpBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"background-colour: transparent;\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 100), stop:0.984012 rgba(98, 114, 164, 100));\n"
"border-style: inset;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/20x20/icons/20x20/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signUpBtn.setIcon(icon)
        self.signUpBtn.setIconSize(QSize(56, 56))
        self.logOffBtn = QPushButton(self.frame)
        self.logOffBtn.setObjectName(u"logOffBtn")
        self.logOffBtn.setGeometry(QRect(550, 0, 40, 40))
        self.logOffBtn.setMinimumSize(QSize(40, 40))
        self.logOffBtn.setMaximumSize(QSize(40, 40))
        self.logOffBtn.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"background-colour: transparent;\n"
"border-left: 2px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 100), stop:0.984012 rgba(98, 114, 164, 100));\n"
"border-style: inset;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/20x20/icons/20x20/cil-power-standby.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logOffBtn.setIcon(icon1)
        self.logOffBtn.setIconSize(QSize(32, 32))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 11, 141, 16))
        font = QFont()
        font.setFamily(u"Montserrat SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 6, 40, 31))
        self.frame_3.setMaximumSize(QSize(40, 40))
        self.frame_3.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/logo.png);\n"
"image: url(:/20x20/icons/20x20/cil-library.png);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{background-color: qlineargradient(spread:pad, x1:0.148, y1:0.0738636, x2:0.983, y2:0.33, stop:0 rgba(33, 35, 45, 255), stop:1 rgba(68, 71, 90, 255));}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 20, 151, 31))
        font1 = QFont()
        font1.setFamily(u"Montserrat Medium")
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(260, 70, 75, 41))
        self.pushButton.setStyleSheet(u"border: none;\n"
"background-colour: transparent;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"icons/16x16/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(230, 260, 131, 30))
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        self.pushButton_4.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Montserrat Light")
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 100), stop:0.984012 rgba(98, 114, 164, 100));\n"
"border-style: inset;\n"
"}")
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 130, 342, 42))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"background-colour: transparent;\n"
"border-right:none;\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.usernameLEdit = QLineEdit(self.layoutWidget)
        self.usernameLEdit.setObjectName(u"usernameLEdit")
        self.usernameLEdit.setMinimumSize(QSize(300, 40))
        self.usernameLEdit.setMaximumSize(QSize(300, 40))
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        font3.setPointSize(10)
        self.usernameLEdit.setFont(font3)
        self.usernameLEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background-color:rgb(40, 42, 54);\n"
"color: white;\n"
"border-left:none;\n"
"}")

        self.gridLayout.addWidget(self.usernameLEdit, 0, 1, 1, 1)

        self.error_label = QLabel(self.frame_2)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(170, 300, 241, 31))
        self.error_label.setStyleSheet(u"background:none;\n"
"color: rgb(255, 85, 255);\n"
"font: 25 8pt \"Mulish Light\";")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(130, 191, 40, 40))
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setStyleSheet(u"border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"background-colour: transparent;\n"
"border-right:none;\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-lock-locked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(32, 32))
        self.passwordLEdit = QLineEdit(self.frame_2)
        self.passwordLEdit.setObjectName(u"passwordLEdit")
        self.passwordLEdit.setGeometry(QRect(170, 191, 280, 40))
        self.passwordLEdit.setMinimumSize(QSize(280, 40))
        self.passwordLEdit.setMaximumSize(QSize(280, 40))
        self.passwordLEdit.setFont(font3)
        self.passwordLEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background-color:rgb(40, 42, 54);\n"
"	color: white;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"}")
        self.passwordLEdit.setEchoMode(QLineEdit.Password)
        self.viewPasswordBtn = QPushButton(self.frame_2)
        self.viewPasswordBtn.setObjectName(u"viewPasswordBtn")
        self.viewPasswordBtn.setGeometry(QRect(450, 191, 20, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewPasswordBtn.sizePolicy().hasHeightForWidth())
        self.viewPasswordBtn.setSizePolicy(sizePolicy1)
        self.viewPasswordBtn.setMinimumSize(QSize(20, 40))
        self.viewPasswordBtn.setMaximumSize(QSize(20, 40))
        self.viewPasswordBtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"background-color: rgb(40, 42, 54);\n"
"border-left:none;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(178, 138, 236, 150);\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-watch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewPasswordBtn.setIcon(icon5)
        self.viewPasswordBtn.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
#if QT_CONFIG(tooltip)
        self.signUpBtn.setToolTip(QCoreApplication.translate("Dialog", u"Add New User", None))
#endif // QT_CONFIG(tooltip)
        self.signUpBtn.setText("")
#if QT_CONFIG(tooltip)
        self.logOffBtn.setToolTip(QCoreApplication.translate("Dialog", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.logOffBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Mobingo Library v 1.0.0", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"WELCOME", None))
        self.pushButton.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"LOGIN", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_2.setText("")
        self.usernameLEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.error_label.setText("")
        self.pushButton_5.setText("")
        self.passwordLEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.viewPasswordBtn.setText("")
    # retranslateUi

