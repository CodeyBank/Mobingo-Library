# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Dialog_register(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(595, 550)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 600, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"background-color: rgb(52, 54, 68);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.signUpBtn = QPushButton(self.frame)
        self.signUpBtn.setObjectName(u"signUpBtn")
        self.signUpBtn.setGeometry(QRect(510, 7, 40, 30))
        self.signUpBtn.setMinimumSize(QSize(40, 30))
        self.signUpBtn.setMaximumSize(QSize(40, 30))
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
        icon.addFile(u"icons/enter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signUpBtn.setIcon(icon)
        self.signUpBtn.setIconSize(QSize(16, 16))
        self.logOffBtn = QPushButton(self.frame)
        self.logOffBtn.setObjectName(u"logOffBtn")
        self.logOffBtn.setGeometry(QRect(550, 7, 40, 30))
        self.logOffBtn.setMinimumSize(QSize(40, 30))
        self.logOffBtn.setMaximumSize(QSize(40, 30))
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(4, 6, 40, 31))
        self.frame_3.setMaximumSize(QSize(40, 40))
        self.frame_3.setStyleSheet(u"background-image: url(:/20x20/icons/20x20/logo.png);\n"
"image: url(:/20x20/icons/20x20/cil-library.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 12, 141, 16))
        font = QFont()
        font.setFamily(u"Montserrat SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 40, 600, 511))
        self.frame_2.setStyleSheet(u"QFrame{background-color: qlineargradient(spread:pad, x1:0.148, y1:0.0738636, x2:0.983, y2:0.33, stop:0 rgba(33, 35, 45, 255), stop:1 rgba(68, 71, 90, 255));}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
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
        self.pushButton_4.setGeometry(QRect(230, 410, 131, 30))
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
        self.error_labelUN = QLabel(self.frame_2)
        self.error_labelUN.setObjectName(u"error_labelUN")
        self.error_labelUN.setGeometry(QRect(180, 170, 241, 31))
        self.error_labelUN.setStyleSheet(u"background:none;\n"
"color: rgb(255, 85, 255);\n"
"font: 25 8pt \"Mulish Light\";")
        self.error_labelUN.setAlignment(Qt.AlignCenter)
        self.error_labelEM = QLabel(self.frame_2)
        self.error_labelEM.setObjectName(u"error_labelEM")
        self.error_labelEM.setGeometry(QRect(180, 240, 241, 31))
        self.error_labelEM.setStyleSheet(u"background:none;\n"
"color: rgb(255, 85, 255);\n"
"font: 25 8pt \"Mulish Light\";")
        self.error_labelEM.setAlignment(Qt.AlignCenter)
        self.error_labelPW = QLabel(self.frame_2)
        self.error_labelPW.setObjectName(u"error_labelPW")
        self.error_labelPW.setGeometry(QRect(180, 310, 241, 31))
        self.error_labelPW.setStyleSheet(u"background:none;\n"
"color: rgb(255, 85, 255);\n"
"font: 25 8pt \"Mulish Light\";")
        self.error_labelPW.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 130, 40, 40))
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
        self.viewPasswordBtn = QPushButton(self.frame_2)
        self.viewPasswordBtn.setObjectName(u"viewPasswordBtn")
        self.viewPasswordBtn.setGeometry(QRect(450, 271, 20, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewPasswordBtn.sizePolicy().hasHeightForWidth())
        self.viewPasswordBtn.setSizePolicy(sizePolicy)
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
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-watch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewPasswordBtn.setIcon(icon4)
        self.viewPasswordBtn.setIconSize(QSize(32, 32))
        self.successLabel = QLabel(self.frame_2)
        self.successLabel.setObjectName(u"successLabel")
        self.successLabel.setGeometry(QRect(150, 460, 301, 20))
        self.successLabel.setStyleSheet(u"background:none;\n"
"color: rgb(255, 85, 255);\n"
"font: 25 8pt \"Mulish Light\";")
        self.successLabel.setAlignment(Qt.AlignCenter)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(130, 271, 40, 40))
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setStyleSheet(u"border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"background-colour: transparent;\n"
"border-right:none;\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-lock-locked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QSize(32, 32))
        self.passwordLEdit_2 = QLineEdit(self.frame_2)
        self.passwordLEdit_2.setObjectName(u"passwordLEdit_2")
        self.passwordLEdit_2.setGeometry(QRect(170, 271, 280, 40))
        self.passwordLEdit_2.setMinimumSize(QSize(280, 40))
        self.passwordLEdit_2.setMaximumSize(QSize(280, 40))
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        font3.setPointSize(10)
        self.passwordLEdit_2.setFont(font3)
        self.passwordLEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background-color:rgb(40, 42, 54);\n"
"	color: white;\n"
"	border-left:none;\n"
"	border-right:none;\n"
"}")
        self.passwordLEdit_2.setEchoMode(QLineEdit.Password)
        self.usernameLEdit = QLineEdit(self.frame_2)
        self.usernameLEdit.setObjectName(u"usernameLEdit")
        self.usernameLEdit.setGeometry(QRect(170, 130, 300, 40))
        self.usernameLEdit.setMinimumSize(QSize(300, 40))
        self.usernameLEdit.setMaximumSize(QSize(300, 40))
        self.usernameLEdit.setFont(font3)
        self.usernameLEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background-color:rgb(40, 42, 54);\n"
"color: white;\n"
"border-left:none;\n"
"}")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(131, 201, 40, 40))
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 40))
        self.pushButton_3.setStyleSheet(u"border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"background-colour: transparent;\n"
"border-right:none;\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-envelope-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(32, 32))
        self.emailLEdit = QLineEdit(self.frame_2)
        self.emailLEdit.setObjectName(u"emailLEdit")
        self.emailLEdit.setGeometry(QRect(170, 201, 300, 40))
        self.emailLEdit.setMinimumSize(QSize(300, 40))
        self.emailLEdit.setMaximumSize(QSize(300, 40))
        self.emailLEdit.setFont(font3)
        self.emailLEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background-color:rgb(40, 42, 54);\n"
"color: white;\n"
"border-left:none;\n"
"}")
        self.emailLEdit.setEchoMode(QLineEdit.Normal)
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(131, 341, 40, 40))
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setMaximumSize(QSize(40, 40))
        self.pushButton_6.setStyleSheet(u"border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"background-colour: transparent;\n"
"border-right:none;\n"
"\n"
"")
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(32, 32))
        self.repeatpasswordLEdit_3 = QLineEdit(self.frame_2)
        self.repeatpasswordLEdit_3.setObjectName(u"repeatpasswordLEdit_3")
        self.repeatpasswordLEdit_3.setGeometry(QRect(171, 341, 300, 40))
        self.repeatpasswordLEdit_3.setMinimumSize(QSize(300, 40))
        self.repeatpasswordLEdit_3.setMaximumSize(QSize(300, 40))
        self.repeatpasswordLEdit_3.setFont(font3)
        self.repeatpasswordLEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background-color:rgb(40, 42, 54);\n"
"color: white;\n"
"border-left:none;\n"
"}")
        self.repeatpasswordLEdit_3.setEchoMode(QLineEdit.Password)
        QWidget.setTabOrder(self.usernameLEdit, self.emailLEdit)
        QWidget.setTabOrder(self.emailLEdit, self.passwordLEdit_2)
        QWidget.setTabOrder(self.passwordLEdit_2, self.repeatpasswordLEdit_3)
        QWidget.setTabOrder(self.repeatpasswordLEdit_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.signUpBtn)
        QWidget.setTabOrder(self.signUpBtn, self.logOffBtn)
        QWidget.setTabOrder(self.logOffBtn, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.signUpBtn.setToolTip(QCoreApplication.translate("Dialog", u"Add New User", None))
#endif // QT_CONFIG(tooltip)
        self.signUpBtn.setText("")
        self.logOffBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Mobingo Library v 1.0.0", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.pushButton.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Create", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("Dialog", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.error_labelUN.setText("")
        self.error_labelEM.setText("")
        self.error_labelPW.setText("")
        self.pushButton_2.setText("")
        self.viewPasswordBtn.setText("")
        self.successLabel.setText("")
        self.pushButton_5.setText("")
        self.passwordLEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.usernameLEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.pushButton_3.setText("")
        self.emailLEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Valid email", None))
        self.pushButton_6.setText("")
        self.repeatpasswordLEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Repeat password", None))
    # retranslateUi

