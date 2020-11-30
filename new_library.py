# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1557, 1069)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"background-color: rgb(52, 54, 68);")
        MainWindow.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionPeople = QAction(MainWindow)
        self.actionPeople.setObjectName(u"actionPeople")
        self.actionBooks = QAction(MainWindow)
        self.actionBooks.setObjectName(u"actionBooks")
        self.actionClients = QAction(MainWindow)
        self.actionClients.setObjectName(u"actionClients")
        self.actionPlaces = QAction(MainWindow)
        self.actionPlaces.setObjectName(u"actionPlaces")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLog_off = QAction(MainWindow)
        self.actionLog_off.setObjectName(u"actionLog_off")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionPDF = QAction(MainWindow)
        self.actionPDF.setObjectName(u"actionPDF")
        self.actionExcell = QAction(MainWindow)
        self.actionExcell.setObjectName(u"actionExcell")
        self.actionCSV = QAction(MainWindow)
        self.actionCSV.setObjectName(u"actionCSV")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionLog_out = QAction(MainWindow)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        icon = QIcon()
        icon.addFile(u":/20x20/icons/20x20/cil-save.png", QSize(), QIcon.Normal, QIcon.On)
        self.actionSave_2.setIcon(icon)
        self.actionwidgetChange = QAction(MainWindow)
        self.actionwidgetChange.setObjectName(u"actionwidgetChange")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_29 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.baseFrame = QFrame(self.centralwidget)
        self.baseFrame.setObjectName(u"baseFrame")
        self.baseFrame.setStyleSheet(u"QMainWindow{background-color: transparent;}")
        self.baseFrame.setFrameShape(QFrame.NoFrame)
        self.baseFrame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.baseFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.baseFrame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 50))
        self.titleBar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 0, 0)
        self.toggleMenuBtn = QFrame(self.titleBar)
        self.toggleMenuBtn.setObjectName(u"toggleMenuBtn")
        self.toggleMenuBtn.setMaximumSize(QSize(50, 40))
        self.toggleMenuBtn.setFrameShape(QFrame.NoFrame)
        self.toggleMenuBtn.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_32 = QHBoxLayout(self.toggleMenuBtn)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.toggleMenuBtn)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(35, 30))
        self.pushButton.setMaximumSize(QSize(37, 45))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	border-bottom: 1px solid rgb(35, 35, 35)\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(52, 54, 68, 150);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/20x20/icons/20x20/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.toggleMenuBtn)

        self.topMenu = QFrame(self.titleBar)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 40))
        self.topMenu.setMaximumSize(QSize(16777215, 60))
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.topMenu)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 8, 0)
        self.frame_16 = QFrame(self.topMenu)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 40))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(40, 40))
        self.frame_23.setStyleSheet(u"background-image: url(:/24x24/icons/24x24/cil-library.png);\n"
"background-repeat:none;\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_23)

        self.label = QLabel(self.frame_16)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Montserrat SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;")

        self.horizontalLayout_6.addWidget(self.label)


        self.horizontalLayout_22.addWidget(self.frame_16)

        self.frame_2 = QFrame(self.topMenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(450, 40))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	font: 25 11pt \"Montserrat Light\";\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	border-bottom: 5px solid rgb(35, 35, 35);\n"
"	color:rgb(170, 85, 255)\n"
"}\n"
"QFrame{\n"
"background-color:none;\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.helpBtn = QPushButton(self.frame_2)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(30, 30))
        self.helpBtn.setMaximumSize(QSize(30, 30))
        self.helpBtn.setStyleSheet(u"QPushButton{\n"
"	font: 25 11pt \"Montserrat Bold\";\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	border-radius: 15px;\n"
"	background-color:rgb(57, 57, 57);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 1px solid white ;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.helpBtn)

        self.dateTime = QLabel(self.frame_2)
        self.dateTime.setObjectName(u"dateTime")
        self.dateTime.setMinimumSize(QSize(250, 40))
        self.dateTime.setStyleSheet(u"font: 25 11pt \"Montserrat Light\";\n"
"color:rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_4.addWidget(self.dateTime)

        self.hideBtn = QPushButton(self.frame_2)
        self.hideBtn.setObjectName(u"hideBtn")
        self.hideBtn.setMinimumSize(QSize(40, 40))
        self.hideBtn.setMaximumSize(QSize(40, 40))
        self.hideBtn.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgba(52, 54, 68, 150);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/20x20/icons/20x20/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hideBtn.setIcon(icon2)
        self.hideBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.hideBtn)

        self.maximizeRestoreBtn = QPushButton(self.frame_2)
        self.maximizeRestoreBtn.setObjectName(u"maximizeRestoreBtn")
        self.maximizeRestoreBtn.setMinimumSize(QSize(40, 40))
        self.maximizeRestoreBtn.setMaximumSize(QSize(40, 40))
        self.maximizeRestoreBtn.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgba(52, 54, 68, 150);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/24x24/icons/24x24/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreBtn.setIcon(icon3)
        self.maximizeRestoreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.maximizeRestoreBtn)

        self.closeWindowBtn = QPushButton(self.frame_2)
        self.closeWindowBtn.setObjectName(u"closeWindowBtn")
        self.closeWindowBtn.setMinimumSize(QSize(40, 40))
        self.closeWindowBtn.setMaximumSize(QSize(40, 40))
        self.closeWindowBtn.setStyleSheet(u"QPushButton:pressed{\n"
"background-color: rgba(52, 54, 68, 150);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/24x24/icons/24x24/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindowBtn.setIcon(icon4)
        self.closeWindowBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.closeWindowBtn)


        self.horizontalLayout_22.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.topMenu)


        self.verticalLayout.addWidget(self.titleBar)

        self.parentHolder = QFrame(self.baseFrame)
        self.parentHolder.setObjectName(u"parentHolder")
        self.parentHolder.setFrameShape(QFrame.NoFrame)
        self.parentHolder.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.parentHolder)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sideBar = QFrame(self.parentHolder)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setMinimumSize(QSize(60, 0))
        self.sideBar.setMaximumSize(QSize(16777215, 16777215))
        self.sideBar.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"")
        self.sideBar.setFrameShape(QFrame.NoFrame)
        self.sideBar.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.sideBar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.top_Buttons = QFrame(self.sideBar)
        self.top_Buttons.setObjectName(u"top_Buttons")
        self.top_Buttons.setStyleSheet(u"QPushButton{\n"
"	border:0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	border-left: 5px solid qlineargradient(spread:pad, x1:0.006, y1:0.699182, x2:0.993128, y2:0.325, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"")
        self.top_Buttons.setFrameShape(QFrame.NoFrame)
        self.top_Buttons.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.top_Buttons)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dashBoardBtn = QPushButton(self.top_Buttons)
        self.dashBoardBtn.setObjectName(u"dashBoardBtn")
        self.dashBoardBtn.setMinimumSize(QSize(50, 40))
        self.dashBoardBtn.setMaximumSize(QSize(1111111, 40))
        self.dashBoardBtn.setStyleSheet(u"QPushButton {\n"
"		background-image: url(:/20x20/icons/20x20/cil-home.png);\n"
"        background-position: center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 0px solid rgb(27, 29, 35);\n"
"        background-color: none;\n"
"        text-align: left;\n"
"        padding-left: 45px;\n"
"        color:white;\n"
"    }\n"
"")

        self.verticalLayout_3.addWidget(self.dashBoardBtn)

        self.booksButton = QPushButton(self.top_Buttons)
        self.booksButton.setObjectName(u"booksButton")
        self.booksButton.setMinimumSize(QSize(60, 40))
        self.booksButton.setMaximumSize(QSize(1111111, 40))
        self.booksButton.setToolTipDuration(3)
        self.booksButton.setStyleSheet(u"QPushButton {\n"
"		background-image: url(:/20x20/icons/20x20/cil-notes.png);\n"
"        background-position: center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 0px solid rgb(27, 29, 35);\n"
"        background-color: none;\n"
"        text-align: left;\n"
"        padding-left: 45px;\n"
"        color:white;\n"
"    }\n"
"")
        self.booksButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.booksButton)

        self.usersBtn = QPushButton(self.top_Buttons)
        self.usersBtn.setObjectName(u"usersBtn")
        self.usersBtn.setMinimumSize(QSize(60, 40))
        self.usersBtn.setMaximumSize(QSize(1111111, 40))
        self.usersBtn.setStyleSheet(u"QPushButton {\n"
"		background-image: url(:/20x20/icons/20x20/cil-user.png);\n"
"        background-position: center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 0px solid rgb(27, 29, 35);\n"
"        background-color: none;\n"
"        text-align: left;\n"
"        padding-left: 45px;\n"
"        color:white;\n"
"    }\n"
"")
        self.usersBtn.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.usersBtn)

        self.settingsBtn = QPushButton(self.top_Buttons)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(60, 40))
        self.settingsBtn.setMaximumSize(QSize(1111111, 40))
        self.settingsBtn.setStyleSheet(u"QPushButton {\n"
"		background-image: url(:/20x20/icons/20x20/cil-settings.png);\n"
"        background-position: center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 0px solid rgb(27, 29, 35);\n"
"        background-color: none;\n"
"        text-align: left;\n"
"        padding-left: 45px;\n"
"        color:white;\n"
"    }\n"
"")
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.settingsBtn)

        self.statisticsBtn = QPushButton(self.top_Buttons)
        self.statisticsBtn.setObjectName(u"statisticsBtn")
        self.statisticsBtn.setMinimumSize(QSize(60, 40))
        self.statisticsBtn.setMaximumSize(QSize(1111111, 40))
        self.statisticsBtn.setStyleSheet(u"QPushButton {\n"
"		background-image: url(:/20x20/icons/20x20/cil-chart-line.png);\n"
"        background-position: center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 0px solid rgb(27, 29, 35);\n"
"        background-color: none;\n"
"        text-align: left;\n"
"        padding-left: 45px;\n"
"        color:white;\n"
"    }\n"
"")
        self.statisticsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.statisticsBtn)


        self.verticalLayout_4.addWidget(self.top_Buttons, 0, Qt.AlignTop)

        self.bottomBtns = QFrame(self.sideBar)
        self.bottomBtns.setObjectName(u"bottomBtns")
        self.bottomBtns.setMaximumSize(QSize(16777215, 200))
        self.bottomBtns.setStyleSheet(u"QPushButton{\n"
"	border:0px solid\n"
"}\n"
"QPushButton:hover{\n"
"	border-left: 5px solid qlineargradient(spread:pad, x1:0.006, y1:0.699182, x2:0.993128, y2:0.325, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}")
        self.bottomBtns.setFrameShape(QFrame.NoFrame)
        self.bottomBtns.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.bottomBtns)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 0, 0, 0)
        self.user_initialsLabel = QLabel(self.bottomBtns)
        self.user_initialsLabel.setObjectName(u"user_initialsLabel")
        self.user_initialsLabel.setMinimumSize(QSize(50, 50))
        self.user_initialsLabel.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.user_initialsLabel.setFont(font1)
        self.user_initialsLabel.setFocusPolicy(Qt.ClickFocus)
        self.user_initialsLabel.setStyleSheet(u"QLabel {\n"
"	border-radius: 25px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(108, 117, 173);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	color: white;\n"
"	text-align:centre;\n"
"}\n"
"")
        self.user_initialsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.user_initialsLabel, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.bottomBtns)


        self.horizontalLayout_2.addWidget(self.sideBar)

        self.mainCanvas = QFrame(self.parentHolder)
        self.mainCanvas.setObjectName(u"mainCanvas")
        self.mainCanvas.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background:rgb(108, 117, 173);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin"
                        ": margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(108, 117, 173);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(108, 11"
                        "7, 173);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(108, 117, 173);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52,"
                        " 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
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
"	border-left-style"
                        ": solid;\n"
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
"\n"
"\n"
"*{ \n"
"	background-color: rgb(52, 54, 68);\n"
"}")
        self.mainCanvas.setFrameShape(QFrame.NoFrame)
        self.mainCanvas.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.mainCanvas)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.stackedWidget = QStackedWidget(self.mainCanvas)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dashBoardPage = QWidget()
        self.dashBoardPage.setObjectName(u"dashBoardPage")
        self.horizontalLayout = QHBoxLayout(self.dashBoardPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboardTools = QFrame(self.dashBoardPage)
        self.dashboardTools.setObjectName(u"dashboardTools")
        self.dashboardTools.setMinimumSize(QSize(70, 0))
        self.dashboardTools.setMaximumSize(QSize(70, 16777215))
        self.dashboardTools.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"	border: 2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(81, 81, 122);\n"
"}")
        self.dashboardTools.setFrameShape(QFrame.NoFrame)
        self.dashboardTools.setFrameShadow(QFrame.Plain)
        self.dashboardTools.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.dashboardTools)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.addNewOpBtn = QPushButton(self.dashboardTools)
        self.addNewOpBtn.setObjectName(u"addNewOpBtn")
        self.addNewOpBtn.setMinimumSize(QSize(40, 40))
        self.addNewOpBtn.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setFamily(u"Montserrat Light")
        font2.setPointSize(36)
        font2.setBold(False)
        font2.setWeight(50)
        self.addNewOpBtn.setFont(font2)
        self.addNewOpBtn.setToolTipDuration(3)
        self.addNewOpBtn.setLayoutDirection(Qt.LeftToRight)
        self.addNewOpBtn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/24x24/icons/24x24/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addNewOpBtn.setIcon(icon5)
        self.addNewOpBtn.setIconSize(QSize(24, 24))
        self.addNewOpBtn.setFlat(False)

        self.verticalLayout_7.addWidget(self.addNewOpBtn)

        self.editOpBtn = QPushButton(self.dashboardTools)
        self.editOpBtn.setObjectName(u"editOpBtn")
        self.editOpBtn.setMinimumSize(QSize(40, 40))
        self.editOpBtn.setMaximumSize(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u":/20x20/icons/20x20/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editOpBtn.setIcon(icon6)
        self.editOpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.editOpBtn)

        self.clearFilterBtn = QPushButton(self.dashboardTools)
        self.clearFilterBtn.setObjectName(u"clearFilterBtn")
        self.clearFilterBtn.setMinimumSize(QSize(40, 40))
        self.clearFilterBtn.setMaximumSize(QSize(40, 40))
        self.clearFilterBtn.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/24x24/icons/24x24/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearFilterBtn.setIcon(icon7)
        self.clearFilterBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.clearFilterBtn)

        self.deleteEntryBtn = QPushButton(self.dashboardTools)
        self.deleteEntryBtn.setObjectName(u"deleteEntryBtn")
        self.deleteEntryBtn.setMinimumSize(QSize(40, 40))
        self.deleteEntryBtn.setMaximumSize(QSize(40, 40))
        self.deleteEntryBtn.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/24x24/icons/24x24/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteEntryBtn.setIcon(icon8)
        self.deleteEntryBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.deleteEntryBtn)


        self.horizontalLayout.addWidget(self.dashboardTools, 0, Qt.AlignVCenter)

        self.mainDashboadParent = QFrame(self.dashBoardPage)
        self.mainDashboadParent.setObjectName(u"mainDashboadParent")
        self.mainDashboadParent.setFrameShape(QFrame.NoFrame)
        self.mainDashboadParent.setFrameShadow(QFrame.Plain)
        self.mainDashboadParent.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.mainDashboadParent)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.infoLableFrame = QFrame(self.mainDashboadParent)
        self.infoLableFrame.setObjectName(u"infoLableFrame")
        self.infoLableFrame.setMinimumSize(QSize(0, 120))
        self.infoLableFrame.setMaximumSize(QSize(16777215, 100))
        self.infoLableFrame.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Thin\";\n"
"	color: white;\n"
"}")
        self.infoLableFrame.setFrameShape(QFrame.StyledPanel)
        self.infoLableFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.infoLableFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.booksAvailLabel = QLabel(self.infoLableFrame)
        self.booksAvailLabel.setObjectName(u"booksAvailLabel")

        self.horizontalLayout_8.addWidget(self.booksAvailLabel)

        self.label_3 = QLabel(self.infoLableFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.label_4 = QLabel(self.infoLableFrame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.label_5 = QLabel(self.infoLableFrame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.label_6 = QLabel(self.infoLableFrame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)


        self.verticalLayout_8.addWidget(self.infoLableFrame)

        self.frame_4 = QFrame(self.mainDashboadParent)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 80))
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	color: white;\n"
"	font: 25 10pt \"Montserrat Light\";\n"
"}\n"
"QLineEdit:hover{\n"
" border: 1px solid white;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_13.setHorizontalSpacing(3)
        self.filterTransaction = QLineEdit(self.frame_4)
        self.filterTransaction.setObjectName(u"filterTransaction")
        self.filterTransaction.setMinimumSize(QSize(0, 35))
        self.filterTransaction.setMaximumSize(QSize(700, 16777215))
        font3 = QFont()
        font3.setFamily(u"Montserrat Light")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(3)
        self.filterTransaction.setFont(font3)

        self.gridLayout_13.addWidget(self.filterTransaction, 0, 0, 1, 1)

        self.transactionFilter = QPushButton(self.frame_4)
        self.transactionFilter.setObjectName(u"transactionFilter")
        self.transactionFilter.setMinimumSize(QSize(0, 30))
        self.transactionFilter.setMaximumSize(QSize(40, 30))
        self.transactionFilter.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.transactionFilter.setIcon(icon9)
        self.transactionFilter.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.transactionFilter, 0, 1, 1, 1)

        self.filterBookTitle = QLineEdit(self.frame_4)
        self.filterBookTitle.setObjectName(u"filterBookTitle")
        self.filterBookTitle.setMinimumSize(QSize(0, 35))
        self.filterBookTitle.setMaximumSize(QSize(700, 16777215))
        self.filterBookTitle.setFont(font3)

        self.gridLayout_13.addWidget(self.filterBookTitle, 0, 2, 1, 1)

        self.usernameFiler = QPushButton(self.frame_4)
        self.usernameFiler.setObjectName(u"usernameFiler")
        self.usernameFiler.setMinimumSize(QSize(0, 30))
        self.usernameFiler.setMaximumSize(QSize(40, 30))
        self.usernameFiler.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        self.usernameFiler.setIcon(icon9)
        self.usernameFiler.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.usernameFiler, 0, 3, 1, 1)

        self.filterClientName = QLineEdit(self.frame_4)
        self.filterClientName.setObjectName(u"filterClientName")
        self.filterClientName.setMinimumSize(QSize(0, 35))
        self.filterClientName.setMaximumSize(QSize(700, 16777215))
        self.filterClientName.setFont(font3)

        self.gridLayout_13.addWidget(self.filterClientName, 0, 4, 1, 1)

        self.bookTitleFIlter = QPushButton(self.frame_4)
        self.bookTitleFIlter.setObjectName(u"bookTitleFIlter")
        self.bookTitleFIlter.setMinimumSize(QSize(0, 30))
        self.bookTitleFIlter.setMaximumSize(QSize(40, 30))
        self.bookTitleFIlter.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        self.bookTitleFIlter.setIcon(icon9)
        self.bookTitleFIlter.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.bookTitleFIlter, 0, 5, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_13)

        self.exportBtn = QPushButton(self.frame_4)
        self.exportBtn.setObjectName(u"exportBtn")
        self.exportBtn.setMinimumSize(QSize(80, 30))
        self.exportBtn.setMaximumSize(QSize(80, 30))
        self.exportBtn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        self.exportBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.exportBtn)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.mainDashboadParent)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.frame_21)

        self.tableWidget_2 = QTableWidget(self.frame_5)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(39, 44, 54, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.tableWidget_2.setPalette(palette)
        self.tableWidget_2.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 10px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
" 	text-align:centre;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(72, 81, 100);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_27.addWidget(self.tableWidget_2)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.mainDashboadParent)

        self.stackedWidget.addWidget(self.dashBoardPage)
        self.booksPage = QWidget()
        self.booksPage.setObjectName(u"booksPage")
        self.horizontalLayout_10 = QHBoxLayout(self.booksPage)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.booksPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 0 solid;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"	min-height:20px;\n"
"    padding: 10px 2px;\n"
"	\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: rgb(88, 91, 115);\n"
"    border: 0px solid;\n"
"     /*border-bottom-color: #C2C7CB; same as the pane color */\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    min-width: 8ex;\n"
"	min-height:40px;\n"
"    padding: 20px 1px;\n"
"	font: 25 8pt \"Roboto Light\";\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    margin-top:-4px;\n"
"	margin-bottom:-4px;\n"
"}\n"
"\n"
"\n"
""
                        "QTabBar::tab:!selected {\n"
"    margin-right: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_12 = QHBoxLayout(self.tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(70, 0))
        self.frame.setMaximumSize(QSize(70, 16777215))
        self.frame.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"	border: 2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(81, 81, 122);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.editOpBtn_2 = QPushButton(self.frame)
        self.editOpBtn_2.setObjectName(u"editOpBtn_2")
        self.editOpBtn_2.setMinimumSize(QSize(40, 40))
        self.editOpBtn_2.setMaximumSize(QSize(40, 40))
        self.editOpBtn_2.setIcon(icon6)
        self.editOpBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.editOpBtn_2)

        self.searchOpBtn_2 = QPushButton(self.frame)
        self.searchOpBtn_2.setObjectName(u"searchOpBtn_2")
        self.searchOpBtn_2.setMinimumSize(QSize(40, 40))
        self.searchOpBtn_2.setMaximumSize(QSize(40, 40))
        self.searchOpBtn_2.setStyleSheet(u"")
        self.searchOpBtn_2.setIcon(icon9)
        self.searchOpBtn_2.setIconSize(QSize(24, 24))

        self.verticalLayout_10.addWidget(self.searchOpBtn_2)


        self.horizontalLayout_12.addWidget(self.frame, 0, Qt.AlignVCenter)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 100))
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(15, 15, 15, 15)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setFamily(u"Roboto Light")
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(3)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Light\";\n"
"	color: white;\n"
"}")

        self.horizontalLayout_14.addWidget(self.label_7)


        self.horizontalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 100, 0)
        self.allbooksLable = QLabel(self.frame_10)
        self.allbooksLable.setObjectName(u"allbooksLable")
        font5 = QFont()
        font5.setFamily(u"Roboto Light")
        font5.setPointSize(22)
        self.allbooksLable.setFont(font5)
        self.allbooksLable.setStyleSheet(u"color:white;")
        self.allbooksLable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.allbooksLable)


        self.horizontalLayout_13.addWidget(self.frame_10)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 80))
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	color: white;\n"
"	font: 25 10pt \"Montserrat Light\";\n"
"}\n"
"QLineEdit:hover{\n"
" border: 1px solid white;\n"
"}\n"
"QPushButton{\n"
" 	border: 0px solid;\n"
"	background-color: qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setSizeConstraint(QLayout.SetMaximumSize)
        self.gridLayout_15.setHorizontalSpacing(3)
        self.filterBookID = QLineEdit(self.frame_7)
        self.filterBookID.setObjectName(u"filterBookID")
        self.filterBookID.setMinimumSize(QSize(300, 35))
        self.filterBookID.setMaximumSize(QSize(700, 16777215))
        self.filterBookID.setFont(font3)

        self.gridLayout_15.addWidget(self.filterBookID, 0, 0, 1, 1)

        self.transactionFilter_3 = QPushButton(self.frame_7)
        self.transactionFilter_3.setObjectName(u"transactionFilter_3")
        self.transactionFilter_3.setMinimumSize(QSize(0, 30))
        self.transactionFilter_3.setMaximumSize(QSize(40, 30))
        self.transactionFilter_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        self.transactionFilter_3.setIcon(icon9)
        self.transactionFilter_3.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.transactionFilter_3, 0, 1, 1, 1)

        self.filterBookTitle_3 = QLineEdit(self.frame_7)
        self.filterBookTitle_3.setObjectName(u"filterBookTitle_3")
        self.filterBookTitle_3.setMinimumSize(QSize(300, 35))
        self.filterBookTitle_3.setMaximumSize(QSize(700, 16777215))
        self.filterBookTitle_3.setFont(font3)

        self.gridLayout_15.addWidget(self.filterBookTitle_3, 0, 2, 1, 1)

        self.usernameFiler_3 = QPushButton(self.frame_7)
        self.usernameFiler_3.setObjectName(u"usernameFiler_3")
        self.usernameFiler_3.setMinimumSize(QSize(0, 30))
        self.usernameFiler_3.setMaximumSize(QSize(40, 30))
        self.usernameFiler_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        self.usernameFiler_3.setIcon(icon9)
        self.usernameFiler_3.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.usernameFiler_3, 0, 3, 1, 1)

        self.filterAuthor = QLineEdit(self.frame_7)
        self.filterAuthor.setObjectName(u"filterAuthor")
        self.filterAuthor.setMinimumSize(QSize(300, 35))
        self.filterAuthor.setMaximumSize(QSize(700, 16777215))
        self.filterAuthor.setFont(font3)

        self.gridLayout_15.addWidget(self.filterAuthor, 0, 4, 1, 1)

        self.bookTitleFIlter_3 = QPushButton(self.frame_7)
        self.bookTitleFIlter_3.setObjectName(u"bookTitleFIlter_3")
        self.bookTitleFIlter_3.setMinimumSize(QSize(0, 30))
        self.bookTitleFIlter_3.setMaximumSize(QSize(40, 30))
        self.bookTitleFIlter_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        self.bookTitleFIlter_3.setIcon(icon9)
        self.bookTitleFIlter_3.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.bookTitleFIlter_3, 0, 5, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout_15)

        self.exportBtn_2 = QPushButton(self.frame_7)
        self.exportBtn_2.setObjectName(u"exportBtn_2")
        self.exportBtn_2.setMinimumSize(QSize(80, 30))
        self.exportBtn_2.setMaximumSize(QSize(80, 30))
        self.exportBtn_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")
        self.exportBtn_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.exportBtn_2)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.tableWidget = QTableWidget(self.frame_8)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush6 = QBrush(QColor(255, 255, 255, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 10px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
" 	text-align:centre;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QHeaderView::section{\n"
"	Background-color: rgb(72, 81, 100);\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_17.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_8)


        self.horizontalLayout_12.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_12 = QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_11 = QFrame(self.tab_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 45))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.allbooksLable_2 = QLabel(self.frame_11)
        self.allbooksLable_2.setObjectName(u"allbooksLable_2")
        self.allbooksLable_2.setFont(font5)
        self.allbooksLable_2.setStyleSheet(u"color:white;")
        self.allbooksLable_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.allbooksLable_2)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.tab_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QGroupBox{\n"
"background-color: rgb(35, 35, 35);\n"
"border-radius: 15px;\n"
"}\n"
"QLineEdit{\n"
"	border: 0px solid;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(200, 0, 200, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(500, 700))
        self.frame_13.setStyleSheet(u"background-color:rgba(35,35,35,50);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_13)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addBookGrpBox = QGroupBox(self.frame_13)
        self.addBookGrpBox.setObjectName(u"addBookGrpBox")
        font6 = QFont()
        font6.setPointSize(12)
        self.addBookGrpBox.setFont(font6)
        self.addBookGrpBox.setStyleSheet(u"QGroupBox{margin-top: 5ex;\n"
"	background:none;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 10px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	border-radius:8px;\n"
"	font: 25 14pt \"Roboto Light\";\n"
"	color:white;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.horizontalLayout_19 = QHBoxLayout(self.addBookGrpBox)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.bookTitleLE = QLineEdit(self.addBookGrpBox)
        self.bookTitleLE.setObjectName(u"bookTitleLE")
        self.bookTitleLE.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.bookTitleLE, 0, 0, 1, 1)

        self.authorLE = QLineEdit(self.addBookGrpBox)
        self.authorLE.setObjectName(u"authorLE")
        self.authorLE.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.authorLE, 1, 0, 1, 1)

        self.publisherLE = QLineEdit(self.addBookGrpBox)
        self.publisherLE.setObjectName(u"publisherLE")
        self.publisherLE.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.publisherLE, 2, 0, 1, 1)

        self.isbnLE = QLineEdit(self.addBookGrpBox)
        self.isbnLE.setObjectName(u"isbnLE")
        self.isbnLE.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.isbnLE, 3, 0, 1, 1)

        self.categoryLE = QComboBox(self.addBookGrpBox)
        self.categoryLE.addItem("")
        self.categoryLE.setObjectName(u"categoryLE")
        self.categoryLE.setMaximumSize(QSize(16777215, 45))
        self.categoryLE.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.gridLayout_7.addWidget(self.categoryLE, 4, 0, 1, 1)

        self.yearpubLE = QLineEdit(self.addBookGrpBox)
        self.yearpubLE.setObjectName(u"yearpubLE")
        self.yearpubLE.setMinimumSize(QSize(0, 40))

        self.gridLayout_7.addWidget(self.yearpubLE, 5, 0, 1, 1)

        self.addUserBtn_3 = QPushButton(self.addBookGrpBox)
        self.addUserBtn_3.setObjectName(u"addUserBtn_3")
        self.addUserBtn_3.setMinimumSize(QSize(100, 30))
        self.addUserBtn_3.setMaximumSize(QSize(100, 30))
        self.addUserBtn_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.addUserBtn_3, 6, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_19.addLayout(self.gridLayout_7)


        self.verticalLayout_2.addWidget(self.addBookGrpBox)


        self.horizontalLayout_11.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(80, 16777215))
        self.frame_14.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"	border: 2px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(81, 81, 122);\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.editOpBtn_3 = QPushButton(self.frame_14)
        self.editOpBtn_3.setObjectName(u"editOpBtn_3")
        self.editOpBtn_3.setMinimumSize(QSize(40, 40))
        self.editOpBtn_3.setMaximumSize(QSize(40, 40))
        font7 = QFont()
        font7.setPointSize(24)
        self.editOpBtn_3.setFont(font7)
        self.editOpBtn_3.setStyleSheet(u"color: white;")
        icon10 = QIcon()
        icon10.addFile(u":/20x20/icons/20x20/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editOpBtn_3.setIcon(icon10)
        self.editOpBtn_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_20.addWidget(self.editOpBtn_3)


        self.horizontalLayout_11.addWidget(self.frame_14, 0, Qt.AlignHCenter)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(500, 700))
        self.frame_15.setStyleSheet(u"background-color:rgba(35,35,35,50);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.editBooksGrpBox = QGroupBox(self.frame_15)
        self.editBooksGrpBox.setObjectName(u"editBooksGrpBox")
        self.editBooksGrpBox.setMaximumSize(QSize(500, 1000))
        self.editBooksGrpBox.setFont(font6)
        self.editBooksGrpBox.setStyleSheet(u"QGroupBox{margin-top: 5ex;\n"
"		background:none;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 10px 10pxpx;\n"
"    background-color:qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	border-radius: 8px;\n"
"	\n"
"	font: 25 14pt \"Roboto Light\";\n"
"color:white;\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.editBooksGrpBox)
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_18 = QFrame(self.editBooksGrpBox)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setStyleSheet(u"QFrame{background:transparent;}\\nQLineEdit{\\n	color: white;\\n	background-color: rgb(61, 63, 78);\\n	font: 25 10pt \"Montserrat Light\";\\n}")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Plain)

        self.verticalLayout_11.addWidget(self.frame_18)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(0)
        self.lineEdit = QLineEdit(self.editBooksGrpBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        font8 = QFont()
        font8.setFamily(u"Montserrat Light")
        font8.setPointSize(10)
        self.lineEdit.setFont(font8)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_8.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.editBooksGrpBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setMaximumSize(QSize(40, 40))
        icon11 = QIcon()
        icon11.addFile(u":/20x20/icons/20x20/cil-zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon11)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.pushButton_8, 0, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_8)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(40)
        self.lineEdit_14 = QLineEdit(self.editBooksGrpBox)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 40))
        self.lineEdit_14.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_10.addWidget(self.lineEdit_14, 0, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.editBooksGrpBox)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 40))
        self.lineEdit_16.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_10.addWidget(self.lineEdit_16, 1, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.editBooksGrpBox)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 40))
        self.lineEdit_17.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_10.addWidget(self.lineEdit_17, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.editBooksGrpBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.gridLayout_10.addWidget(self.comboBox, 3, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.editBooksGrpBox)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(0, 40))
        self.lineEdit_18.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_10.addWidget(self.lineEdit_18, 4, 0, 1, 1)

        self.lineEdit_20 = QLineEdit(self.editBooksGrpBox)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(0, 40))
        self.lineEdit_20.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_10.addWidget(self.lineEdit_20, 5, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_10)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_6 = QPushButton(self.editBooksGrpBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(100, 30))
        self.pushButton_6.setMaximumSize(QSize(100, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.editBooksGrpBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        self.pushButton_7.setMaximumSize(QSize(100, 30))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.gridLayout_12.addWidget(self.pushButton_7, 0, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_12)

        self.frame_20 = QFrame(self.editBooksGrpBox)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 100))
        self.frame_20.setStyleSheet(u"background:transparent;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(30, 0, 30, 0)

        self.verticalLayout_11.addWidget(self.frame_20)


        self.horizontalLayout_21.addWidget(self.editBooksGrpBox)


        self.horizontalLayout_11.addWidget(self.frame_15)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_10.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.booksPage)
        self.usersPage = QWidget()
        self.usersPage.setObjectName(u"usersPage")
        self.verticalLayout_17 = QVBoxLayout(self.usersPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_22 = QFrame(self.usersPage)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 300))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_22)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_22)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 60))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.allbooksLable_5 = QLabel(self.frame_28)
        self.allbooksLable_5.setObjectName(u"allbooksLable_5")
        font9 = QFont()
        font9.setFamily(u"Montserrat SemiBold")
        font9.setPointSize(22)
        font9.setBold(True)
        font9.setWeight(75)
        self.allbooksLable_5.setFont(font9)
        self.allbooksLable_5.setStyleSheet(u"color:white;")
        self.allbooksLable_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_76.addWidget(self.allbooksLable_5)


        self.verticalLayout_18.addWidget(self.frame_28)

        self.frame_30 = QFrame(self.frame_22)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_30)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(500, 16777215))
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"border:0px solid;\n"
"background-color: rgb(35, 35, 35,50);\n"
"padding: 20%;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 10px 10pxpx;\n"
"    background-color:qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius:8px;\n"
"	font: 25 14pt \"Roboto Light\";\n"
"	color:white;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_30 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setVerticalSpacing(10)
        self.lineEdit_27 = QLineEdit(self.groupBox_2)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(0, 40))
        self.lineEdit_27.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_27.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_27.setInputMethodHints(Qt.ImhPreferLowercase)

        self.gridLayout_11.addWidget(self.lineEdit_27, 0, 0, 1, 1)

        self.lineEdit_28 = QLineEdit(self.groupBox_2)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setMinimumSize(QSize(97, 40))
        self.lineEdit_28.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_28.setEchoMode(QLineEdit.Password)

        self.gridLayout_11.addWidget(self.lineEdit_28, 1, 0, 1, 1)

        self.loginBtn_2 = QPushButton(self.groupBox_2)
        self.loginBtn_2.setObjectName(u"loginBtn_2")
        self.loginBtn_2.setMinimumSize(QSize(80, 30))
        self.loginBtn_2.setMaximumSize(QSize(100, 30))
        self.loginBtn_2.setLayoutDirection(Qt.LeftToRight)
        self.loginBtn_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.gridLayout_11.addWidget(self.loginBtn_2, 2, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_30.addLayout(self.gridLayout_11)


        self.horizontalLayout_47.addWidget(self.groupBox_2)


        self.verticalLayout_18.addWidget(self.frame_30)


        self.verticalLayout_17.addWidget(self.frame_22)

        self.frame_25 = QFrame(self.usersPage)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.groupBox_4 = QGroupBox(self.frame_27)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(700, 500))
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"border:0px solid;\n"
"background-color: rgb(35, 35, 35,50);\n"
"padding: 20%;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 10px 10pxpx;\n"
"    background-color:qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius:8px;\n"
"	font: 25 14pt \"Roboto Light\";\n"
"	color:white;\n"
"}")
        self.horizontalLayout_75 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.frame_26 = QFrame(self.groupBox_4)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background:transparent;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.firstNameLE_2 = QLineEdit(self.frame_26)
        self.firstNameLE_2.setObjectName(u"firstNameLE_2")
        self.firstNameLE_2.setMinimumSize(QSize(300, 40))
        self.firstNameLE_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.firstNameLE_2, 0, 0, 1, 1)

        self.lastNameLE_2 = QLineEdit(self.frame_26)
        self.lastNameLE_2.setObjectName(u"lastNameLE_2")
        self.lastNameLE_2.setMinimumSize(QSize(300, 40))
        self.lastNameLE_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.lastNameLE_2, 1, 0, 1, 1)

        self.userNameLE_2 = QLineEdit(self.frame_26)
        self.userNameLE_2.setObjectName(u"userNameLE_2")
        self.userNameLE_2.setMinimumSize(QSize(300, 40))
        self.userNameLE_2.setMaximumSize(QSize(16777215, 40))
        self.userNameLE_2.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.gridLayout.addWidget(self.userNameLE_2, 2, 0, 1, 1)

        self.emailLE_2 = QLineEdit(self.frame_26)
        self.emailLE_2.setObjectName(u"emailLE_2")
        self.emailLE_2.setMinimumSize(QSize(300, 40))
        self.emailLE_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.emailLE_2, 3, 0, 1, 1)

        self.passwordLE_2 = QLineEdit(self.frame_26)
        self.passwordLE_2.setObjectName(u"passwordLE_2")
        self.passwordLE_2.setMinimumSize(QSize(300, 40))
        self.passwordLE_2.setMaximumSize(QSize(16777215, 40))
        self.passwordLE_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwordLE_2, 4, 0, 1, 1)

        self.repeatPasswordLE_2 = QLineEdit(self.frame_26)
        self.repeatPasswordLE_2.setObjectName(u"repeatPasswordLE_2")
        self.repeatPasswordLE_2.setMinimumSize(QSize(300, 40))
        self.repeatPasswordLE_2.setMaximumSize(QSize(16777215, 40))
        self.repeatPasswordLE_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.repeatPasswordLE_2, 5, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.frame_26)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(0, 40))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(9)
        self.comboBox_6.setFont(font10)
        self.comboBox_6.setAutoFillBackground(False)
        self.comboBox_6.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox_6.setIconSize(QSize(16, 16))
        self.comboBox_6.setFrame(True)

        self.gridLayout.addWidget(self.comboBox_6, 6, 0, 1, 1)

        self.addUserBtn_2 = QPushButton(self.frame_26)
        self.addUserBtn_2.setObjectName(u"addUserBtn_2")
        self.addUserBtn_2.setMinimumSize(QSize(100, 30))
        self.addUserBtn_2.setMaximumSize(QSize(100, 30))
        self.addUserBtn_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.addUserBtn_2, 7, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_74.addLayout(self.gridLayout)


        self.horizontalLayout_75.addWidget(self.frame_26)


        self.horizontalLayout_73.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.frame_27)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(700, 500))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"border:0px solid;\n"
"background-color: rgb(35, 35, 35,50);\n"
"padding: 20%;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 10px 10pxpx;\n"
"    background-color:qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius:8px;\n"
"	font: 25 14pt \"Roboto Light\";\n"
"	color:white;\n"
"}\n"
"\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(20)
        self.lineEdit_21 = QLineEdit(self.groupBox_3)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(300, 40))
        self.lineEdit_21.setMaximumSize(QSize(166777, 40))

        self.gridLayout_9.addWidget(self.lineEdit_21, 0, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.groupBox_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(300, 40))
        self.lineEdit_22.setMaximumSize(QSize(166777, 40))

        self.gridLayout_9.addWidget(self.lineEdit_22, 1, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.groupBox_3)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(300, 40))
        self.lineEdit_23.setMaximumSize(QSize(166777, 40))
        self.lineEdit_23.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.gridLayout_9.addWidget(self.lineEdit_23, 2, 0, 1, 1)

        self.lineEdit_24 = QLineEdit(self.groupBox_3)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(300, 40))
        self.lineEdit_24.setMaximumSize(QSize(166777, 40))

        self.gridLayout_9.addWidget(self.lineEdit_24, 3, 0, 1, 1)

        self.lineEdit_25 = QLineEdit(self.groupBox_3)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(300, 40))
        self.lineEdit_25.setMaximumSize(QSize(166777, 40))
        self.lineEdit_25.setEchoMode(QLineEdit.Password)

        self.gridLayout_9.addWidget(self.lineEdit_25, 4, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.groupBox_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(300, 40))
        self.lineEdit_8.setMaximumSize(QSize(166777, 40))
        self.lineEdit_8.setEchoMode(QLineEdit.Password)

        self.gridLayout_9.addWidget(self.lineEdit_8, 5, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 40))
        self.comboBox_3.setMaximumSize(QSize(166777, 40))
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.gridLayout_9.addWidget(self.comboBox_3, 6, 0, 1, 1)


        self.verticalLayout_20.addLayout(self.gridLayout_9)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.editUserBtn = QPushButton(self.groupBox_3)
        self.editUserBtn.setObjectName(u"editUserBtn")
        self.editUserBtn.setMinimumSize(QSize(100, 30))
        self.editUserBtn.setMaximumSize(QSize(100, 30))
        self.editUserBtn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.editUserBtn, 0, 0, 1, 1, Qt.AlignRight)

        self.deleteUserBtn = QPushButton(self.groupBox_3)
        self.deleteUserBtn.setObjectName(u"deleteUserBtn")
        self.deleteUserBtn.setMinimumSize(QSize(100, 30))
        self.deleteUserBtn.setMaximumSize(QSize(100, 30))
        self.deleteUserBtn.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.deleteUserBtn, 0, 1, 1, 1, Qt.AlignLeft)


        self.verticalLayout_20.addLayout(self.gridLayout_6)


        self.horizontalLayout_73.addWidget(self.groupBox_3)


        self.horizontalLayout_26.addWidget(self.frame_27)


        self.verticalLayout_17.addWidget(self.frame_25)

        self.stackedWidget.addWidget(self.usersPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_23 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.settingsPage)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background: transparent;")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_33)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_64 = QFrame(self.frame_33)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMaximumSize(QSize(16777215, 100))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.allbooksLable_4 = QLabel(self.frame_64)
        self.allbooksLable_4.setObjectName(u"allbooksLable_4")
        self.allbooksLable_4.setFont(font9)
        self.allbooksLable_4.setStyleSheet(u"color:white;")
        self.allbooksLable_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.allbooksLable_4)

        self.label_12 = QLabel(self.frame_64)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_49.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.frame_64, 0, Qt.AlignHCenter)

        self.frame_70 = QFrame(self.frame_33)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_35 = QFrame(self.frame_70)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 500))
        self.frame_35.setStyleSheet(u"background-color: rgba(35, 35, 35,50);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_35)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_35)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"background-color:none;")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Plain)
        self.verticalLayout_27 = QVBoxLayout(self.frame_43)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(16777215, 70))
        self.frame_45.setStyleSheet(u"background-color:none;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 20, 0, 0)
        self.label_8 = QLabel(self.frame_45)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(300, 30))
        self.label_8.setMaximumSize(QSize(300, 32))
        font11 = QFont()
        font11.setFamily(u"Montserrat SemiBold")
        font11.setPointSize(12)
        self.label_8.setFont(font11)
        self.label_8.setStyleSheet(u"border-radius:8px;\n"
"background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_8)


        self.verticalLayout_27.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(0, 200))
        self.frame_46.setMaximumSize(QSize(16777215, 300))
        self.frame_46.setStyleSheet(u"backgroun-color:none;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(500, 16777215))
        self.frame_48.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_48)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(30, -1, 20, -1)
        self.lineEdit_11 = QLineEdit(self.frame_48)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(200, 0))
        self.lineEdit_11.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_29.addWidget(self.lineEdit_11)

        self.comboBox_2 = QComboBox(self.frame_48)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 0))
        self.comboBox_2.setMaximumSize(QSize(16777215, 40))
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox_2.setIconSize(QSize(12, 12))

        self.verticalLayout_29.addWidget(self.comboBox_2)


        self.horizontalLayout_37.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_46)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(500, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(35, 35, 35, 50))
        brush8.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        brush10 = QBrush(QColor(255, 255, 255, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        brush11 = QBrush(QColor(255, 255, 255, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        self.frame_49.setPalette(palette2)
        self.frame_49.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_49)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(15, -1, 15, -1)
        self.lineEdit_13 = QLineEdit(self.frame_49)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(200, 0))
        self.lineEdit_13.setMaximumSize(QSize(16777215, 40))
        self.lineEdit_13.setEchoMode(QLineEdit.Password)

        self.verticalLayout_28.addWidget(self.lineEdit_13)

        self.lineEdit_26 = QLineEdit(self.frame_49)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(200, 0))
        self.lineEdit_26.setMaximumSize(QSize(16777215, 40))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush12 = QBrush(QColor(27, 29, 35, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush12)
        brush13 = QBrush(QColor(255, 255, 255, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        brush14 = QBrush(QColor(255, 255, 255, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush14)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        brush15 = QBrush(QColor(255, 255, 255, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.lineEdit_26.setPalette(palette3)
        self.lineEdit_26.setInputMethodHints(Qt.ImhDigitsOnly)

        self.verticalLayout_28.addWidget(self.lineEdit_26)


        self.horizontalLayout_37.addWidget(self.frame_49)


        self.verticalLayout_27.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 50))
        self.frame_47.setMaximumSize(QSize(16777215, 50))
        self.frame_47.setStyleSheet(u"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 50)
        self.pushButton_10 = QPushButton(self.frame_47)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 30))
        self.pushButton_10.setMaximumSize(QSize(100, 30))
        font12 = QFont()
        font12.setFamily(u"Roboto")
        font12.setPointSize(12)
        font12.setBold(False)
        font12.setItalic(False)
        font12.setWeight(3)
        self.pushButton_10.setFont(font12)
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.horizontalLayout_38.addWidget(self.pushButton_10)


        self.verticalLayout_27.addWidget(self.frame_47, 0, Qt.AlignVCenter)


        self.verticalLayout_26.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_35)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background-color: none;")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_44)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"background-color:none;\n"
"border:none;\n"
"border-right: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_50)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.frame_50)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(16777215, 50))
        self.frame_53.setStyleSheet(u"border:none;")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_9 = QLabel(self.frame_53)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font11)
        self.label_9.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 180), stop:0.984012 rgba(98, 114, 164, 180));\n"
"border-radius:8px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_9)


        self.verticalLayout_31.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_50)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"background:transparent;\n"
"border:none;")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_54)
        self.verticalLayout_34.setSpacing(20)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.fontComboBox = QFontComboBox(self.frame_54)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMinimumSize(QSize(0, 30))
        self.fontComboBox.setMaximumSize(QSize(16777215, 40))
        font13 = QFont()
        font13.setFamily(u"Montserrat Medium")
        font13.setPointSize(8)
        self.fontComboBox.setFont(font13)
        self.fontComboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")

        self.verticalLayout_34.addWidget(self.fontComboBox)

        self.comboBox_4 = QComboBox(self.frame_54)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 30))
        self.comboBox_4.setMaximumSize(QSize(70, 16777215))
        self.comboBox_4.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox_4.setIconSize(QSize(24, 24))

        self.verticalLayout_34.addWidget(self.comboBox_4)


        self.verticalLayout_31.addWidget(self.frame_54, 0, Qt.AlignTop)


        self.horizontalLayout_39.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_44)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"background-color:none;\n"
"border:none;\n"
"border-right: 1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Plain)
        self.verticalLayout_32 = QVBoxLayout(self.frame_51)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.frame_51)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(16777215, 50))
        self.frame_55.setStyleSheet(u"border:none;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_10 = QLabel(self.frame_55)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font11)
        self.label_10.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 180), stop:0.984012 rgba(98, 114, 164, 180));\n"
"border-radius:8px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.label_10)


        self.verticalLayout_32.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_51)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"border:none")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_56)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, -1, -1, -1)
        self.radioButton = QRadioButton(self.frame_56)
        self.radioButton.setObjectName(u"radioButton")
        font14 = QFont()
        font14.setFamily(u"Montserrat Light")
        font14.setPointSize(12)
        self.radioButton.setFont(font14)
        self.radioButton.setStyleSheet(u"background:transparent;")

        self.verticalLayout_35.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.frame_56)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font14)
        self.radioButton_2.setStyleSheet(u"background:transparent;")

        self.verticalLayout_35.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_56)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font14)
        self.radioButton_3.setStyleSheet(u"background:transparent;")

        self.verticalLayout_35.addWidget(self.radioButton_3)


        self.verticalLayout_32.addWidget(self.frame_56, 0, Qt.AlignHCenter)


        self.horizontalLayout_39.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_44)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"background-color:none;\n"
"border: none;\n"
"border-radius: 8px;")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_52)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_52)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setStyleSheet(u"border:none")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_11 = QLabel(self.frame_57)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font11)
        self.label_11.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 180), stop:0.984012 rgba(98, 114, 164, 180));")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_11)


        self.verticalLayout_33.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_52)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"border:none")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_58)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox = QCheckBox(self.frame_58)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font14)
        self.checkBox.setStyleSheet(u"background:transparent;")

        self.verticalLayout_9.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_58)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font14)
        self.checkBox_2.setStyleSheet(u"background:transparent;")

        self.verticalLayout_9.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame_58)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font14)
        self.checkBox_3.setStyleSheet(u"background:transparent;")

        self.verticalLayout_9.addWidget(self.checkBox_3)


        self.verticalLayout_33.addWidget(self.frame_58, 0, Qt.AlignHCenter)


        self.horizontalLayout_39.addWidget(self.frame_52)


        self.verticalLayout_26.addWidget(self.frame_44)


        self.horizontalLayout_31.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_70)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 500))
        self.frame_36.setStyleSheet(u"background-color: rgba(35, 35, 35,50);")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.frame_36)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 60))
        self.frame_37.setStyleSheet(u"background:none;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.user_initials_4 = QLabel(self.frame_37)
        self.user_initials_4.setObjectName(u"user_initials_4")
        self.user_initials_4.setMinimumSize(QSize(50, 50))
        self.user_initials_4.setMaximumSize(QSize(50, 50))
        self.user_initials_4.setFont(font1)
        self.user_initials_4.setFocusPolicy(Qt.ClickFocus)
        self.user_initials_4.setStyleSheet(u"QLabel {\n"
"	border-radius: 25px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	color: white;\n"
"	text-align:centre;\n"
"}\n"
"")
        self.user_initials_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.user_initials_4)


        self.verticalLayout_24.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 200))
        self.frame_38.setMaximumSize(QSize(16777215, 200))
        self.frame_38.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QFrame{background:none;}")
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Plain)
        self.verticalLayout_30 = QVBoxLayout(self.frame_38)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(100, -1, 100, 0)
        self.lineEdit_9 = QLineEdit(self.frame_38)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_30.addWidget(self.lineEdit_9)

        self.lineEdit_10 = QLineEdit(self.frame_38)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_30.addWidget(self.lineEdit_10)

        self.pushButton_9 = QPushButton(self.frame_38)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 30))
        self.pushButton_9.setMaximumSize(QSize(100, 30))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.verticalLayout_30.addWidget(self.pushButton_9)


        self.verticalLayout_24.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 50))
        self.frame_39.setStyleSheet(u"background:none;")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_2 = QLabel(self.frame_39)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 32))
        self.label_2.setMaximumSize(QSize(300, 16777215))
        font15 = QFont()
        font15.setFamily(u"Montserrat SemiBold")
        font15.setPointSize(12)
        font15.setBold(False)
        font15.setWeight(50)
        self.label_2.setFont(font15)
        self.label_2.setStyleSheet(u"background-color:qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 180), stop:0.984012 rgba(98, 114, 164, 180));\n"
"border-radius:8px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_2)


        self.verticalLayout_24.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_36)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"QFrame{\n"
"	border-right: 2px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	background:none;\n"
"}")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(60, -1, 60, -1)
        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"QFrame{border-left:1px solid qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));}\n"
"QCheckBox{\n"
"	color: white;\n"
"}")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 55, -1, -1)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(40, -1, 20, -1)
        self.changeThemeCB = QCheckBox(self.frame_42)
        self.changeThemeCB.setObjectName(u"changeThemeCB")
        self.changeThemeCB.setMinimumSize(QSize(22, 0))
        font16 = QFont()
        font16.setFamily(u"Monteserrat Light")
        font16.setPointSize(12)
        font16.setBold(False)
        font16.setItalic(False)
        font16.setWeight(50)
        self.changeThemeCB.setFont(font16)
        self.changeThemeCB.setStyleSheet(u"background:none;")

        self.gridLayout_2.addWidget(self.changeThemeCB, 0, 0, 1, 1)

        self.addUserCB = QCheckBox(self.frame_42)
        self.addUserCB.setObjectName(u"addUserCB")
        self.addUserCB.setMinimumSize(QSize(22, 0))
        self.addUserCB.setFont(font16)
        self.addUserCB.setStyleSheet(u"background:none;")

        self.gridLayout_2.addWidget(self.addUserCB, 0, 1, 1, 1)

        self.veiwStatisticsChB_2 = QCheckBox(self.frame_42)
        self.veiwStatisticsChB_2.setObjectName(u"veiwStatisticsChB_2")
        self.veiwStatisticsChB_2.setMaximumSize(QSize(16777215, 53))
        self.veiwStatisticsChB_2.setFont(font16)
        self.veiwStatisticsChB_2.setStyleSheet(u"background:none;")

        self.gridLayout_2.addWidget(self.veiwStatisticsChB_2, 1, 0, 1, 1)

        self.RemoveUserChB = QCheckBox(self.frame_42)
        self.RemoveUserChB.setObjectName(u"RemoveUserChB")
        self.RemoveUserChB.setMinimumSize(QSize(22, 0))
        self.RemoveUserChB.setFont(font16)
        self.RemoveUserChB.setStyleSheet(u"background:none;")

        self.gridLayout_2.addWidget(self.RemoveUserChB, 1, 1, 1, 1)

        self.configDBChB = QCheckBox(self.frame_42)
        self.configDBChB.setObjectName(u"configDBChB")
        self.configDBChB.setMinimumSize(QSize(22, 0))
        self.configDBChB.setFont(font16)
        self.configDBChB.setStyleSheet(u"background:none;")

        self.gridLayout_2.addWidget(self.configDBChB, 2, 0, 1, 1)

        self.veiwStatisticsChB = QCheckBox(self.frame_42)
        self.veiwStatisticsChB.setObjectName(u"veiwStatisticsChB")
        self.veiwStatisticsChB.setMinimumSize(QSize(22, 0))
        self.veiwStatisticsChB.setFont(font16)
        self.veiwStatisticsChB.setStyleSheet(u"background:none;")

        self.gridLayout_2.addWidget(self.veiwStatisticsChB, 2, 1, 1, 1)


        self.horizontalLayout_48.addLayout(self.gridLayout_2)


        self.horizontalLayout_35.addWidget(self.frame_42)


        self.verticalLayout_24.addWidget(self.frame_40)


        self.horizontalLayout_31.addWidget(self.frame_36)


        self.verticalLayout_25.addWidget(self.frame_70)


        self.verticalLayout_23.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.settingsPage)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(300, 0))
        self.frame_34.setMaximumSize(QSize(200, 100))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_43.setSpacing(15)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(10, 0, 10, 0)
        self.pushButton_11 = QPushButton(self.frame_34)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(150, 30))
        self.pushButton_11.setFont(font12)
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.horizontalLayout_43.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_34)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(150, 30))
        self.pushButton_12.setFont(font12)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	font: 25 12pt \"Roboto\";\n"
"	border-radius: 15px;\n"
"	border: 1px solid white;\n"
"	background-color: qlineargradient(spread:pad, x1:0.392, y1:0.170364, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(96, 76, 129);\n"
"}\n"
"")

        self.horizontalLayout_43.addWidget(self.pushButton_12)


        self.verticalLayout_23.addWidget(self.frame_34, 0, Qt.AlignRight)

        self.stackedWidget.addWidget(self.settingsPage)
        self.statisticsPage = QWidget()
        self.statisticsPage.setObjectName(u"statisticsPage")
        self.verticalLayout_15 = QVBoxLayout(self.statisticsPage)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 9, 0)
        self.frame_32 = QFrame(self.statisticsPage)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 40))
        self.frame_32.setMaximumSize(QSize(16777215, 50))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, -1)
        self.allbooksLable_3 = QLabel(self.frame_32)
        self.allbooksLable_3.setObjectName(u"allbooksLable_3")
        self.allbooksLable_3.setFont(font9)
        self.allbooksLable_3.setStyleSheet(u"color:white;")
        self.allbooksLable_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.allbooksLable_3)


        self.verticalLayout_15.addWidget(self.frame_32)

        self.frame_59 = QFrame(self.statisticsPage)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(800, 0))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.groupBox_5 = QGroupBox(self.frame_60)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox{margin-top: 5ex;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 5px 10px;\n"
"    background-color:qlineargradient(spread:pad, x1:0.125, y1:0.562409, x2:0.51, y2:0.95, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 rgba(98, 114, 164, 255));\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius:58px;\n"
"	font: 25 12pt \"Roboto Light\";\n"
"color:white;\n"
"}")
        self.horizontalLayout_53 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 10, 0, 9)
        self.frame_62 = QFrame(self.groupBox_5)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(450, 0))
        self.frame_62.setMaximumSize(QSize(450, 16777215))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_62)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.frame_62)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 40))
        self.frame_65.setMaximumSize(QSize(16777215, 40))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.allbooksLable_6 = QLabel(self.frame_65)
        self.allbooksLable_6.setObjectName(u"allbooksLable_6")
        font17 = QFont()
        font17.setFamily(u"Roboto Light")
        font17.setPointSize(10)
        self.allbooksLable_6.setFont(font17)
        self.allbooksLable_6.setStyleSheet(u"color:white;")
        self.allbooksLable_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.allbooksLable_6)


        self.verticalLayout_39.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_62)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_66)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_66)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_55.setSpacing(40)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(10, 15, -1, 20)
        self.CircularProgress_4 = QFrame(self.frame_67)
        self.CircularProgress_4.setObjectName(u"CircularProgress_4")
        self.CircularProgress_4.setMinimumSize(QSize(180, 180))
        self.CircularProgress_4.setMaximumSize(QSize(180, 180))
        self.CircularProgress_4.setStyleSheet(u"QFrame{\n"
"	border-radius: 90px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, \n"
"	stop:0  rgba(85, 170, 255, 255), stop:0.373979  rgba(85, 170, 255, 255), \n"
"	stop:0.373991 rgb(255, 0, 255), stop:0.624018 rgb(175, 137, 233),\n"
" 	stop: 0.624043 rgb(252, 183, 20), stop:0.82334 rgb(252, 183, 20), \n"
"	stop:0.82566 rgb(0, 255, 0), stop:1 rgb(0, 255, 0));\n"
"}\n"
"")
        self.CircularProgress_4.setFrameShape(QFrame.NoFrame)
        self.CircularProgress_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.CircularProgress_4)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.container_5 = QFrame(self.CircularProgress_4)
        self.container_5.setObjectName(u"container_5")
        self.container_5.setMinimumSize(QSize(120, 120))
        self.container_5.setMaximumSize(QSize(120, 120))
        self.container_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(52, 54, 68);\n"
"	border-radius: 60px;\n"
"}")
        self.container_5.setFrameShape(QFrame.NoFrame)
        self.container_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_54.addWidget(self.container_5)


        self.horizontalLayout_55.addWidget(self.CircularProgress_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(-1, 30, -1, 30)
        self.allbooksLable_15 = QLabel(self.frame_67)
        self.allbooksLable_15.setObjectName(u"allbooksLable_15")
        font18 = QFont()
        font18.setFamily(u"Roboto Light")
        font18.setPointSize(8)
        self.allbooksLable_15.setFont(font18)
        self.allbooksLable_15.setStyleSheet(u"color:white;")
        self.allbooksLable_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.allbooksLable_15, 4, 1, 1, 1)

        self.allbooksLable_13 = QLabel(self.frame_67)
        self.allbooksLable_13.setObjectName(u"allbooksLable_13")
        self.allbooksLable_13.setFont(font18)
        self.allbooksLable_13.setStyleSheet(u"color:white;")
        self.allbooksLable_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.allbooksLable_13, 2, 1, 1, 1)

        self.frame_88 = QFrame(self.frame_67)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(16777215, 10))
        self.frame_88.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_88, 2, 0, 1, 1)

        self.frame_90 = QFrame(self.frame_67)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 10))
        self.frame_90.setMaximumSize(QSize(16777215, 10))
        self.frame_90.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_90, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.allbooksLable_12 = QLabel(self.frame_67)
        self.allbooksLable_12.setObjectName(u"allbooksLable_12")
        self.allbooksLable_12.setFont(font18)
        self.allbooksLable_12.setStyleSheet(u"color:white;")
        self.allbooksLable_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.allbooksLable_12, 1, 1, 1, 1)

        self.allbooksLable_14 = QLabel(self.frame_67)
        self.allbooksLable_14.setObjectName(u"allbooksLable_14")
        self.allbooksLable_14.setFont(font18)
        self.allbooksLable_14.setStyleSheet(u"color:white;")
        self.allbooksLable_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.allbooksLable_14, 3, 1, 1, 1)

        self.frame_87 = QFrame(self.frame_67)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(10, 10))
        self.frame_87.setMaximumSize(QSize(10, 10))
        self.frame_87.setStyleSheet(u"background-color: rgb(252, 183, 20);")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_87, 1, 0, 1, 1)

        self.frame_89 = QFrame(self.frame_67)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 10))
        self.frame_89.setMaximumSize(QSize(16777215, 10))
        self.frame_89.setStyleSheet(u"background-color: rgb(242, 21, 252);")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_89, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)


        self.horizontalLayout_55.addLayout(self.gridLayout_3)


        self.verticalLayout_40.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_66)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_68)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 30))
        self.frame_69.setMaximumSize(QSize(16777215, 30))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.allbooksLable_16 = QLabel(self.frame_69)
        self.allbooksLable_16.setObjectName(u"allbooksLable_16")
        self.allbooksLable_16.setFont(font17)
        self.allbooksLable_16.setStyleSheet(u"color:white;")
        self.allbooksLable_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.allbooksLable_16)


        self.verticalLayout_41.addWidget(self.frame_69)

        self.frame_84 = QFrame(self.frame_68)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.frame_84)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(430, 230))
        self.groupBox_7.setMaximumSize(QSize(430, 230))
        self.groupBox_7.setStyleSheet(u"QGroupBox{margin-top: 5ex;\n"
"	color: #ffffff;\n"
"	font: 25 8pt \"Mulish Light\";\n"
"}\n"
"")
        self.verticalLayout_43 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 4)
        self.frame_91 = QFrame(self.groupBox_7)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_92 = QFrame(self.frame_91)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(40, 0))
        self.frame_92.setMaximumSize(QSize(70, 16777215))
        self.frame_92.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 25 8pt \"Montserrat Light\";")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_92)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.fifth_val_2 = QLabel(self.frame_92)
        self.fifth_val_2.setObjectName(u"fifth_val_2")
        self.fifth_val_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.fifth_val_2)

        self.forth_val_2 = QLabel(self.frame_92)
        self.forth_val_2.setObjectName(u"forth_val_2")
        self.forth_val_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.forth_val_2)

        self.thr_val_2 = QLabel(self.frame_92)
        self.thr_val_2.setObjectName(u"thr_val_2")
        self.thr_val_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.thr_val_2)

        self.sec_val_2 = QLabel(self.frame_92)
        self.sec_val_2.setObjectName(u"sec_val_2")
        self.sec_val_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.sec_val_2)

        self.first_val_2 = QLabel(self.frame_92)
        self.first_val_2.setObjectName(u"first_val_2")
        self.first_val_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.first_val_2)


        self.horizontalLayout_58.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.NoFrame)
        self.frame_93.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.frame_94 = QFrame(self.frame_93)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 150))
        self.frame_94.setMaximumSize(QSize(25, 150))
        self.frame_94.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(255, 85, 255), stop:1 rgb(255, 85, 255));")
        self.frame_94.setFrameShape(QFrame.NoFrame)
        self.frame_94.setFrameShadow(QFrame.Plain)
        self.frame_94.setLineWidth(0)

        self.horizontalLayout_59.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_93)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(0, 150))
        self.frame_95.setMaximumSize(QSize(25, 150))
        self.frame_95.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(85, 170, 255), stop:1 rgb(85, 170, 255));")
        self.frame_95.setFrameShape(QFrame.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_59.addWidget(self.frame_95)

        self.frame_96 = QFrame(self.frame_93)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(0, 150))
        self.frame_96.setMaximumSize(QSize(25, 150))
        self.frame_96.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(175, 137, 233), stop:1 rgb(175, 137, 233));")
        self.frame_96.setFrameShape(QFrame.NoFrame)
        self.frame_96.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_59.addWidget(self.frame_96)

        self.frame_97 = QFrame(self.frame_93)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(0, 150))
        self.frame_97.setMaximumSize(QSize(25, 150))
        self.frame_97.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(0, 255, 0), stop:1 rgb(0, 255, 0));")
        self.frame_97.setFrameShape(QFrame.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_59.addWidget(self.frame_97)

        self.frame_98 = QFrame(self.frame_93)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(0, 150))
        self.frame_98.setMaximumSize(QSize(25, 150))
        self.frame_98.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(252, 183, 20), stop:1 rgb(252, 183, 20));")
        self.frame_98.setFrameShape(QFrame.NoFrame)
        self.frame_98.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_59.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.frame_93)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 150))
        self.frame_99.setMaximumSize(QSize(25, 150))
        self.frame_99.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(200, 10, 8), stop:1 rgb(200, 10, 8));")
        self.frame_99.setFrameShape(QFrame.NoFrame)
        self.frame_99.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_59.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_93)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(25, 150))
        self.frame_100.setMaximumSize(QSize(25, 150))
        self.frame_100.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgb(252, 183, 20));")
        self.frame_100.setFrameShape(QFrame.NoFrame)
        self.frame_100.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_59.addWidget(self.frame_100)


        self.horizontalLayout_58.addWidget(self.frame_93)


        self.verticalLayout_43.addWidget(self.frame_91)

        self.frame_101 = QFrame(self.groupBox_7)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMaximumSize(QSize(16777215, 40))
        self.frame_101.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 25 8pt \"Montserrat Light\";")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_101)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(65, 10, 31, 16))
        self.label_25 = QLabel(self.frame_101)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(120, 10, 21, 16))
        self.label_26 = QLabel(self.frame_101)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(170, 10, 31, 16))
        self.label_27 = QLabel(self.frame_101)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(220, 10, 21, 16))
        self.label_28 = QLabel(self.frame_101)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(270, 10, 21, 16))
        self.label_29 = QLabel(self.frame_101)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(320, 10, 21, 16))
        self.label_30 = QLabel(self.frame_101)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(370, 10, 21, 16))

        self.verticalLayout_43.addWidget(self.frame_101)


        self.horizontalLayout_60.addWidget(self.groupBox_7)


        self.verticalLayout_41.addWidget(self.frame_84)


        self.verticalLayout_40.addWidget(self.frame_68)


        self.verticalLayout_39.addWidget(self.frame_66)


        self.horizontalLayout_53.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.groupBox_5)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_63)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_63)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(0, 40))
        self.frame_85.setMaximumSize(QSize(16777215, 40))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.allbooksLable_17 = QLabel(self.frame_85)
        self.allbooksLable_17.setObjectName(u"allbooksLable_17")
        self.allbooksLable_17.setFont(font17)
        self.allbooksLable_17.setStyleSheet(u"color:white;")
        self.allbooksLable_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.allbooksLable_17)


        self.verticalLayout_42.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_63)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_86)
        self.verticalLayout_45.setSpacing(20)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(60, -1, 60, -1)
        self.booksAvailLabel_5 = QLabel(self.frame_86)
        self.booksAvailLabel_5.setObjectName(u"booksAvailLabel_5")
        self.booksAvailLabel_5.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Thin\";\n"
"	color: white;\n"
"}")

        self.verticalLayout_45.addWidget(self.booksAvailLabel_5)

        self.booksAvailLabel_4 = QLabel(self.frame_86)
        self.booksAvailLabel_4.setObjectName(u"booksAvailLabel_4")
        self.booksAvailLabel_4.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Thin\";\n"
"	color: white;\n"
"}")

        self.verticalLayout_45.addWidget(self.booksAvailLabel_4)

        self.label_15 = QLabel(self.frame_86)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Thin\";\n"
"	color: white;\n"
"}")

        self.verticalLayout_45.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_86)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Thin\";\n"
"	color: white;\n"
"}")

        self.verticalLayout_45.addWidget(self.label_16)


        self.verticalLayout_42.addWidget(self.frame_86)


        self.horizontalLayout_53.addWidget(self.frame_63)


        self.horizontalLayout_50.addWidget(self.groupBox_5)


        self.horizontalLayout_45.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_61)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_102 = QFrame(self.frame_61)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(0, 40))
        self.frame_102.setMaximumSize(QSize(16777215, 40))
        self.frame_102.setFrameShape(QFrame.NoFrame)
        self.frame_102.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.allbooksLable_18 = QLabel(self.frame_102)
        self.allbooksLable_18.setObjectName(u"allbooksLable_18")
        font19 = QFont()
        font19.setFamily(u"Roboto Light")
        font19.setPointSize(12)
        self.allbooksLable_18.setFont(font19)
        self.allbooksLable_18.setStyleSheet(u"color:white;")
        self.allbooksLable_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.allbooksLable_18)


        self.verticalLayout_46.addWidget(self.frame_102)

        self.frame_103 = QFrame(self.frame_61)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(320, 0))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_103)
        self.verticalLayout_47.setSpacing(10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(-1, -1, -1, 10)
        self.frame_108 = QFrame(self.frame_103)
        self.frame_108.setObjectName(u"frame_108")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_108.sizePolicy().hasHeightForWidth())
        self.frame_108.setSizePolicy(sizePolicy1)
        self.frame_108.setMinimumSize(QSize(0, 200))
        self.frame_108.setMaximumSize(QSize(16777215, 250))
        self.frame_108.setStyleSheet(u"border: 1px solid white;")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(-1, -1, -1, 9)
        self.CircularProgress_2 = QFrame(self.frame_108)
        self.CircularProgress_2.setObjectName(u"CircularProgress_2")
        self.CircularProgress_2.setMinimumSize(QSize(180, 180))
        self.CircularProgress_2.setMaximumSize(QSize(180, 180))
        self.CircularProgress_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 90px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, \n"
"	stop:0  rgb(252, 183, 20), stop:0.373979  rgb(252, 183, 20), \n"
"	stop:0.373991 rgb(85, 170, 255), stop:0.624018 rgb(85, 170, 255));\n"
"}\n"
"")
        self.CircularProgress_2.setFrameShape(QFrame.NoFrame)
        self.CircularProgress_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.CircularProgress_2)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")

        self.horizontalLayout_64.addWidget(self.CircularProgress_2)

        self.CircularProgress_5 = QFrame(self.frame_108)
        self.CircularProgress_5.setObjectName(u"CircularProgress_5")
        self.CircularProgress_5.setMinimumSize(QSize(180, 180))
        self.CircularProgress_5.setMaximumSize(QSize(180, 180))
        self.CircularProgress_5.setStyleSheet(u"QFrame{\n"
"	border-radius: 90px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, \n"
"	stop:0  rgb(255, 85, 255), stop:0.373979 rgb(255, 85, 255), \n"
"	stop:0.373991 rgb(175, 137, 233), stop:0.624018 rgb(175, 137, 233),\n"
" 	stop: 0.624043 rgb(200, 10, 8), stop:0.82334 rgb(200, 10, 8));\n"
"}\n"
"")
        self.CircularProgress_5.setFrameShape(QFrame.NoFrame)
        self.CircularProgress_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.CircularProgress_5)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.container_6 = QFrame(self.CircularProgress_5)
        self.container_6.setObjectName(u"container_6")
        self.container_6.setMinimumSize(QSize(120, 120))
        self.container_6.setMaximumSize(QSize(120, 120))
        self.container_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(52, 54, 68);\n"
"	border-radius: 60px;\n"
"}")
        self.container_6.setFrameShape(QFrame.NoFrame)
        self.container_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_63.addWidget(self.container_6)


        self.horizontalLayout_64.addWidget(self.CircularProgress_5)


        self.verticalLayout_47.addWidget(self.frame_108)

        self.frame_107 = QFrame(self.frame_103)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(0, 50))
        self.frame_107.setMaximumSize(QSize(16777215, 130))
        self.frame_107.setFrameShape(QFrame.NoFrame)
        self.frame_107.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_109 = QFrame(self.frame_107)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(0, 65))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(50, -1, 50, 10)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.frame_111 = QFrame(self.frame_109)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(10, 10))
        self.frame_111.setMaximumSize(QSize(10, 10))
        self.frame_111.setStyleSheet(u"background-color: rgb(252, 183, 20);")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_111, 0, 0, 1, 1)

        self.allbooksLable_19 = QLabel(self.frame_109)
        self.allbooksLable_19.setObjectName(u"allbooksLable_19")
        self.allbooksLable_19.setFont(font18)
        self.allbooksLable_19.setStyleSheet(u"color:white;")
        self.allbooksLable_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.allbooksLable_19, 0, 1, 1, 1)

        self.frame_112 = QFrame(self.frame_109)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMaximumSize(QSize(16777215, 10))
        self.frame_112.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_112, 1, 0, 1, 1)

        self.allbooksLable_20 = QLabel(self.frame_109)
        self.allbooksLable_20.setObjectName(u"allbooksLable_20")
        self.allbooksLable_20.setFont(font18)
        self.allbooksLable_20.setStyleSheet(u"color:white;")
        self.allbooksLable_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.allbooksLable_20, 1, 1, 1, 1)


        self.horizontalLayout_67.addLayout(self.gridLayout_4)


        self.horizontalLayout_65.addWidget(self.frame_109)

        self.frame_110 = QFrame(self.frame_107)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(50, -1, 20, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.frame_113 = QFrame(self.frame_110)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(10, 10))
        self.frame_113.setMaximumSize(QSize(10, 10))
        self.frame_113.setStyleSheet(u"background-color: rgb(200, 10, 8);")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_113, 0, 0, 1, 1)

        self.allbooksLable_21 = QLabel(self.frame_110)
        self.allbooksLable_21.setObjectName(u"allbooksLable_21")
        self.allbooksLable_21.setFont(font18)
        self.allbooksLable_21.setStyleSheet(u"color:white;")
        self.allbooksLable_21.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.allbooksLable_21, 0, 1, 1, 1)

        self.frame_114 = QFrame(self.frame_110)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMaximumSize(QSize(16777215, 10))
        self.frame_114.setStyleSheet(u"background-color: rgb(175, 137, 233);")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_114, 1, 0, 1, 1)

        self.allbooksLable_22 = QLabel(self.frame_110)
        self.allbooksLable_22.setObjectName(u"allbooksLable_22")
        self.allbooksLable_22.setFont(font18)
        self.allbooksLable_22.setStyleSheet(u"color:white;")
        self.allbooksLable_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.allbooksLable_22, 1, 1, 1, 1)

        self.frame_115 = QFrame(self.frame_110)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMaximumSize(QSize(16777215, 10))
        self.frame_115.setStyleSheet(u"background-color: rgb(255, 85, 255);")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_115, 2, 0, 1, 1)

        self.allbooksLable_23 = QLabel(self.frame_110)
        self.allbooksLable_23.setObjectName(u"allbooksLable_23")
        self.allbooksLable_23.setFont(font18)
        self.allbooksLable_23.setStyleSheet(u"color:white;")
        self.allbooksLable_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.allbooksLable_23, 2, 1, 1, 1)


        self.horizontalLayout_68.addLayout(self.gridLayout_5)


        self.horizontalLayout_65.addWidget(self.frame_110)


        self.verticalLayout_47.addWidget(self.frame_107)


        self.verticalLayout_46.addWidget(self.frame_103)

        self.frame_106 = QFrame(self.frame_61)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_106)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_106)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 40))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.allbooksLable_24 = QLabel(self.frame_17)
        self.allbooksLable_24.setObjectName(u"allbooksLable_24")
        self.allbooksLable_24.setFont(font19)
        self.allbooksLable_24.setStyleSheet(u"color:white;")
        self.allbooksLable_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.allbooksLable_24)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_106)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.groupBox_8 = QGroupBox(self.frame_19)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(430, 180))
        self.groupBox_8.setMaximumSize(QSize(430, 230))
        self.groupBox_8.setStyleSheet(u"QGroupBox{margin-top: 5ex;\n"
"	color: #ffffff;\n"
"	font: 25 8pt \"Mulish Light\";\n"
"}\n"
"")
        self.verticalLayout_48 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 4)
        self.frame_104 = QFrame(self.groupBox_8)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_116 = QFrame(self.frame_104)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(40, 0))
        self.frame_116.setMaximumSize(QSize(70, 16777215))
        self.frame_116.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 25 8pt \"Montserrat Light\";")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_116)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.fifth_val_3 = QLabel(self.frame_116)
        self.fifth_val_3.setObjectName(u"fifth_val_3")
        self.fifth_val_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.fifth_val_3)

        self.forth_val_3 = QLabel(self.frame_116)
        self.forth_val_3.setObjectName(u"forth_val_3")
        self.forth_val_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.forth_val_3)

        self.thr_val_3 = QLabel(self.frame_116)
        self.thr_val_3.setObjectName(u"thr_val_3")
        self.thr_val_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.thr_val_3)

        self.sec_val_3 = QLabel(self.frame_116)
        self.sec_val_3.setObjectName(u"sec_val_3")
        self.sec_val_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.sec_val_3)

        self.first_val_3 = QLabel(self.frame_116)
        self.first_val_3.setObjectName(u"first_val_3")
        self.first_val_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.first_val_3)


        self.horizontalLayout_69.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.frame_104)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.NoFrame)
        self.frame_117.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.frame_118 = QFrame(self.frame_117)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(0, 150))
        self.frame_118.setMaximumSize(QSize(25, 150))
        self.frame_118.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(255, 85, 255), stop:1 rgb(255, 85, 255));")
        self.frame_118.setFrameShape(QFrame.NoFrame)
        self.frame_118.setFrameShadow(QFrame.Plain)
        self.frame_118.setLineWidth(0)

        self.horizontalLayout_70.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.frame_117)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMinimumSize(QSize(0, 150))
        self.frame_119.setMaximumSize(QSize(25, 150))
        self.frame_119.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(85, 170, 255), stop:1 rgb(85, 170, 255));")
        self.frame_119.setFrameShape(QFrame.NoFrame)
        self.frame_119.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_70.addWidget(self.frame_119)

        self.frame_120 = QFrame(self.frame_117)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(0, 150))
        self.frame_120.setMaximumSize(QSize(25, 150))
        self.frame_120.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(175, 137, 233), stop:1 rgb(175, 137, 233));")
        self.frame_120.setFrameShape(QFrame.NoFrame)
        self.frame_120.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_70.addWidget(self.frame_120)

        self.frame_121 = QFrame(self.frame_117)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMinimumSize(QSize(0, 150))
        self.frame_121.setMaximumSize(QSize(25, 150))
        self.frame_121.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(0, 255, 0), stop:1 rgb(0, 255, 0));")
        self.frame_121.setFrameShape(QFrame.NoFrame)
        self.frame_121.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_70.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.frame_117)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(0, 150))
        self.frame_122.setMaximumSize(QSize(25, 150))
        self.frame_122.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(252, 183, 20), stop:1 rgb(252, 183, 20));")
        self.frame_122.setFrameShape(QFrame.NoFrame)
        self.frame_122.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_70.addWidget(self.frame_122)

        self.frame_123 = QFrame(self.frame_117)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMinimumSize(QSize(0, 150))
        self.frame_123.setMaximumSize(QSize(25, 150))
        self.frame_123.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgb(200, 10, 8), stop:1 rgb(200, 10, 8));")
        self.frame_123.setFrameShape(QFrame.NoFrame)
        self.frame_123.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_70.addWidget(self.frame_123)

        self.frame_124 = QFrame(self.frame_117)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMinimumSize(QSize(25, 150))
        self.frame_124.setMaximumSize(QSize(25, 150))
        self.frame_124.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgb(52, 54, 68), stop:0.495 rgb(52, 54, 68), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgb(252, 183, 20));")
        self.frame_124.setFrameShape(QFrame.NoFrame)
        self.frame_124.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_70.addWidget(self.frame_124)


        self.horizontalLayout_69.addWidget(self.frame_117)


        self.verticalLayout_48.addWidget(self.frame_104)

        self.frame_125 = QFrame(self.groupBox_8)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMaximumSize(QSize(16777215, 40))
        self.frame_125.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 25 8pt \"Montserrat Light\";")
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_125)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(65, 10, 31, 16))
        self.label_32 = QLabel(self.frame_125)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(120, 10, 21, 16))
        self.label_33 = QLabel(self.frame_125)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(170, 10, 31, 16))
        self.label_34 = QLabel(self.frame_125)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(220, 10, 21, 16))
        self.label_35 = QLabel(self.frame_125)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(270, 10, 21, 16))
        self.label_36 = QLabel(self.frame_125)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(320, 10, 21, 16))
        self.label_37 = QLabel(self.frame_125)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(370, 10, 21, 16))

        self.verticalLayout_48.addWidget(self.frame_125)


        self.horizontalLayout_24.addWidget(self.groupBox_8)


        self.verticalLayout_13.addWidget(self.frame_19)


        self.verticalLayout_46.addWidget(self.frame_106)

        self.frame_105 = QFrame(self.frame_61)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(0, 130))
        self.frame_105.setMaximumSize(QSize(16777215, 150))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.booksAvailLabel_6 = QLabel(self.frame_105)
        self.booksAvailLabel_6.setObjectName(u"booksAvailLabel_6")
        self.booksAvailLabel_6.setMinimumSize(QSize(0, 120))
        self.booksAvailLabel_6.setMaximumSize(QSize(16777215, 130))
        self.booksAvailLabel_6.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Thin\";\n"
"	color: white;\n"
"}")

        self.horizontalLayout_72.addWidget(self.booksAvailLabel_6)

        self.booksAvailLabel_7 = QLabel(self.frame_105)
        self.booksAvailLabel_7.setObjectName(u"booksAvailLabel_7")
        self.booksAvailLabel_7.setMinimumSize(QSize(0, 120))
        self.booksAvailLabel_7.setMaximumSize(QSize(16777215, 130))
        self.booksAvailLabel_7.setStyleSheet(u"QLabel{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(68, 71, 90);\n"
"	\n"
"	font: 25 8pt \"Roboto Thin\";\n"
"	color: white;\n"
"}")

        self.horizontalLayout_72.addWidget(self.booksAvailLabel_7)


        self.verticalLayout_46.addWidget(self.frame_105)


        self.horizontalLayout_45.addWidget(self.frame_61)


        self.verticalLayout_15.addWidget(self.frame_59)

        self.stackedWidget.addWidget(self.statisticsPage)

        self.horizontalLayout_7.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.mainCanvas)


        self.verticalLayout.addWidget(self.parentHolder)


        self.horizontalLayout_29.addWidget(self.baseFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setStyleSheet(u"background-color: rgb(20, 21, 27);\n"
"color:white;\n"
"font: 12pt \"Century Gothic\";")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.filterTransaction, self.transactionFilter)
        QWidget.setTabOrder(self.transactionFilter, self.filterBookTitle)
        QWidget.setTabOrder(self.filterBookTitle, self.usernameFiler)
        QWidget.setTabOrder(self.usernameFiler, self.filterClientName)
        QWidget.setTabOrder(self.filterClientName, self.bookTitleFIlter)
        QWidget.setTabOrder(self.bookTitleFIlter, self.addNewOpBtn)
        QWidget.setTabOrder(self.addNewOpBtn, self.editOpBtn)
        QWidget.setTabOrder(self.editOpBtn, self.deleteEntryBtn)
        QWidget.setTabOrder(self.deleteEntryBtn, self.exportBtn)
        QWidget.setTabOrder(self.exportBtn, self.filterBookID)
        QWidget.setTabOrder(self.filterBookID, self.searchOpBtn_2)
        QWidget.setTabOrder(self.searchOpBtn_2, self.transactionFilter_3)
        QWidget.setTabOrder(self.transactionFilter_3, self.helpBtn)
        QWidget.setTabOrder(self.helpBtn, self.hideBtn)
        QWidget.setTabOrder(self.hideBtn, self.maximizeRestoreBtn)
        QWidget.setTabOrder(self.maximizeRestoreBtn, self.closeWindowBtn)
        QWidget.setTabOrder(self.closeWindowBtn, self.editOpBtn_2)
        QWidget.setTabOrder(self.editOpBtn_2, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.dashBoardBtn)
        QWidget.setTabOrder(self.dashBoardBtn, self.booksButton)
        QWidget.setTabOrder(self.booksButton, self.usersBtn)
        QWidget.setTabOrder(self.usersBtn, self.settingsBtn)
        QWidget.setTabOrder(self.settingsBtn, self.statisticsBtn)
        QWidget.setTabOrder(self.statisticsBtn, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.filterBookTitle_3)
        QWidget.setTabOrder(self.filterBookTitle_3, self.usernameFiler_3)
        QWidget.setTabOrder(self.usernameFiler_3, self.filterAuthor)
        QWidget.setTabOrder(self.filterAuthor, self.bookTitleFIlter_3)
        QWidget.setTabOrder(self.bookTitleFIlter_3, self.exportBtn_2)
        QWidget.setTabOrder(self.exportBtn_2, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.bookTitleLE)
        QWidget.setTabOrder(self.bookTitleLE, self.authorLE)
        QWidget.setTabOrder(self.authorLE, self.publisherLE)
        QWidget.setTabOrder(self.publisherLE, self.isbnLE)
        QWidget.setTabOrder(self.isbnLE, self.categoryLE)
        QWidget.setTabOrder(self.categoryLE, self.yearpubLE)
        QWidget.setTabOrder(self.yearpubLE, self.addUserBtn_3)
        QWidget.setTabOrder(self.addUserBtn_3, self.editOpBtn_3)
        QWidget.setTabOrder(self.editOpBtn_3, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.lineEdit_14)
        QWidget.setTabOrder(self.lineEdit_14, self.lineEdit_16)
        QWidget.setTabOrder(self.lineEdit_16, self.lineEdit_17)
        QWidget.setTabOrder(self.lineEdit_17, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.lineEdit_18)
        QWidget.setTabOrder(self.lineEdit_18, self.lineEdit_20)
        QWidget.setTabOrder(self.lineEdit_20, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.lineEdit_27)
        QWidget.setTabOrder(self.lineEdit_27, self.lineEdit_28)
        QWidget.setTabOrder(self.lineEdit_28, self.loginBtn_2)
        QWidget.setTabOrder(self.loginBtn_2, self.firstNameLE_2)
        QWidget.setTabOrder(self.firstNameLE_2, self.lastNameLE_2)
        QWidget.setTabOrder(self.lastNameLE_2, self.userNameLE_2)
        QWidget.setTabOrder(self.userNameLE_2, self.emailLE_2)
        QWidget.setTabOrder(self.emailLE_2, self.passwordLE_2)
        QWidget.setTabOrder(self.passwordLE_2, self.repeatPasswordLE_2)
        QWidget.setTabOrder(self.repeatPasswordLE_2, self.comboBox_6)
        QWidget.setTabOrder(self.comboBox_6, self.addUserBtn_2)
        QWidget.setTabOrder(self.addUserBtn_2, self.lineEdit_21)
        QWidget.setTabOrder(self.lineEdit_21, self.lineEdit_22)
        QWidget.setTabOrder(self.lineEdit_22, self.lineEdit_23)
        QWidget.setTabOrder(self.lineEdit_23, self.lineEdit_24)
        QWidget.setTabOrder(self.lineEdit_24, self.lineEdit_25)
        QWidget.setTabOrder(self.lineEdit_25, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.editUserBtn)
        QWidget.setTabOrder(self.editUserBtn, self.deleteUserBtn)
        QWidget.setTabOrder(self.deleteUserBtn, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.lineEdit_13)
        QWidget.setTabOrder(self.lineEdit_13, self.lineEdit_26)
        QWidget.setTabOrder(self.lineEdit_26, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.fontComboBox)
        QWidget.setTabOrder(self.fontComboBox, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.changeThemeCB)
        QWidget.setTabOrder(self.changeThemeCB, self.addUserCB)
        QWidget.setTabOrder(self.addUserCB, self.veiwStatisticsChB_2)
        QWidget.setTabOrder(self.veiwStatisticsChB_2, self.RemoveUserChB)
        QWidget.setTabOrder(self.RemoveUserChB, self.configDBChB)
        QWidget.setTabOrder(self.configDBChB, self.veiwStatisticsChB)
        QWidget.setTabOrder(self.veiwStatisticsChB, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_12)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mobingo Library", None))
        self.actionPeople.setText(QCoreApplication.translate("MainWindow", u"People", None))
        self.actionBooks.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.actionClients.setText(QCoreApplication.translate("MainWindow", u"Clients", None))
        self.actionPlaces.setText(QCoreApplication.translate("MainWindow", u"Places", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLog_off.setText(QCoreApplication.translate("MainWindow", u"Log off", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionPDF.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.actionExcell.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.actionCSV.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionLog_out.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave_2.setToolTip(QCoreApplication.translate("MainWindow", u"Save operation", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionwidgetChange.setText(QCoreApplication.translate("MainWindow", u"widgetChange", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mobingo Library v 1.0.1", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.dateTime.setText(QCoreApplication.translate("MainWindow", u"Monday 23 June, 2020 03:35PM", None))
#if QT_CONFIG(tooltip)
        self.hideBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.hideBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Resize window", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeWindowBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close window", None))
#endif // QT_CONFIG(tooltip)
        self.closeWindowBtn.setText("")
#if QT_CONFIG(tooltip)
        self.dashBoardBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.dashBoardBtn.setText("")
#if QT_CONFIG(tooltip)
        self.booksButton.setToolTip(QCoreApplication.translate("MainWindow", u"Books", u"books"))
#endif // QT_CONFIG(tooltip)
        self.booksButton.setText("")
#if QT_CONFIG(tooltip)
        self.usersBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Users", None))
#endif // QT_CONFIG(tooltip)
        self.usersBtn.setText("")
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.statisticsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Statistics", None))
#endif // QT_CONFIG(tooltip)
        self.statisticsBtn.setText("")
        self.user_initialsLabel.setText(QCoreApplication.translate("MainWindow", u"SE", None))
#if QT_CONFIG(tooltip)
        self.addNewOpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Add new operation", None))
#endif // QT_CONFIG(tooltip)
        self.addNewOpBtn.setText("")
#if QT_CONFIG(tooltip)
        self.editOpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Edit Operation", None))
#endif // QT_CONFIG(tooltip)
        self.editOpBtn.setText("")
#if QT_CONFIG(tooltip)
        self.clearFilterBtn.setToolTip(QCoreApplication.translate("MainWindow", u"clear filters", None))
#endif // QT_CONFIG(tooltip)
        self.clearFilterBtn.setText("")
#if QT_CONFIG(tooltip)
        self.deleteEntryBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Delete entry", None))
#endif // QT_CONFIG(tooltip)
        self.deleteEntryBtn.setText("")
        self.booksAvailLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">1569</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Books Available</span></p><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">100</span></p><p align=\"center\"><span style=\" font-size:14pt;\"> New Clients</span></p><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">500</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Students in Library</span></p><p><br/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">25</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Books burrowed today</span></p><p><br/></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">69</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Pending Requests</span></p><p><br/></p></body></html>", None))
        self.filterTransaction.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter Transaction ID", None))
        self.transactionFilter.setText("")
        self.filterBookTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter by Book title", None))
        self.usernameFiler.setText("")
        self.filterClientName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter by client name", None))
        self.bookTitleFIlter.setText("")
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Transaction ID", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Book ID", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Return Date", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Remarks", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Comments", None));
        self.editOpBtn_2.setText("")
        self.searchOpBtn_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">2100</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Available books</span></p><p><br/></p></body></html>", None))
        self.allbooksLable.setText(QCoreApplication.translate("MainWindow", u"All Books", None))
        self.filterBookID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter Book ID", None))
        self.transactionFilter_3.setText("")
        self.filterBookTitle_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter by Book title", None))
        self.usernameFiler_3.setText("")
        self.filterAuthor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter by client name", None))
        self.bookTitleFIlter_3.setText("")
        self.exportBtn_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"SN", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Author", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Publisher", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Cost", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"All Books", None))
        self.allbooksLable_2.setText(QCoreApplication.translate("MainWindow", u"Add, Edit or Delete Books", None))
        self.addBookGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"Add book", None))
        self.bookTitleLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Book Title", None))
        self.authorLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.publisherLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Publisher", None))
        self.isbnLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.categoryLE.setItemText(0, QCoreApplication.translate("MainWindow", u"Category", None))

        self.yearpubLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year of Publisher", None))
        self.addUserBtn_3.setText(QCoreApplication.translate("MainWindow", u"Add Book", None))
        self.editOpBtn_3.setText("")
        self.editBooksGrpBox.setTitle(QCoreApplication.translate("MainWindow", u"Edit or Delete Book", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter book title to search", None))
        self.pushButton_8.setText("")
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Publisher", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year of Publication", None))
        self.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Book Price", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Add or edit ", None))
        self.allbooksLable_5.setText(QCoreApplication.translate("MainWindow", u"All about Users", None))
        self.groupBox_2.setTitle("")
        self.lineEdit_27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_28.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lineEdit_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.loginBtn_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.groupBox_4.setTitle("")
        self.firstNameLE_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.firstNameLE_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lastNameLE_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lastNameLE_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.userNameLE_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.userNameLE_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.emailLE_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.emailLE_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.passwordLE_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.passwordLE_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.repeatPasswordLE_2.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.repeatPasswordLE_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repeat password", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.addUserBtn_2.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.groupBox_3.setTitle("")
        self.lineEdit_21.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lineEdit_22.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lineEdit_23.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User name", None))
        self.lineEdit_24.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.lineEdit_25.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lineEdit_25.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_8.setStyleSheet(QCoreApplication.translate("MainWindow", u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repeat Password", None))
        self.editUserBtn.setText(QCoreApplication.translate("MainWindow", u"Edit User", None))
        self.deleteUserBtn.setText(QCoreApplication.translate("MainWindow", u"Delete User", None))
        self.allbooksLable_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_12.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Database Configuration", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Fonts", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"18", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Themes", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Theme 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Theme 2", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Theme 3", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Allow Notifications", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Turn off ", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Log Notifications", None))
        self.user_initials_4.setText(QCoreApplication.translate("MainWindow", u"SE", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Configure User Privileges", None))
        self.changeThemeCB.setText(QCoreApplication.translate("MainWindow", u"Change Theme", None))
        self.addUserCB.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.veiwStatisticsChB_2.setText(QCoreApplication.translate("MainWindow", u"View Statistics", None))
        self.RemoveUserChB.setText(QCoreApplication.translate("MainWindow", u"Remove User", None))
        self.configDBChB.setText(QCoreApplication.translate("MainWindow", u"Configure Database", None))
        self.veiwStatisticsChB.setText(QCoreApplication.translate("MainWindow", u"View Statistics", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.allbooksLable_3.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Information on Books", None))
        self.allbooksLable_6.setText(QCoreApplication.translate("MainWindow", u"Book Categories", None))
        self.allbooksLable_15.setText(QCoreApplication.translate("MainWindow", u"Literature", None))
        self.allbooksLable_13.setText(QCoreApplication.translate("MainWindow", u"Arts", None))
        self.allbooksLable_12.setText(QCoreApplication.translate("MainWindow", u"International Politcs", None))
        self.allbooksLable_14.setText(QCoreApplication.translate("MainWindow", u"Science and Technology", None))
        self.allbooksLable_16.setText(QCoreApplication.translate("MainWindow", u"Books burrowed this week", None))
        self.groupBox_7.setTitle("")
        self.fifth_val_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.forth_val_2.setText(QCoreApplication.translate("MainWindow", u"400", None))
        self.thr_val_2.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.sec_val_2.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.first_val_2.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Mon", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Wed", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Thu", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Frid", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Sat", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Sun", None))
        self.allbooksLable_17.setText(QCoreApplication.translate("MainWindow", u"Add, Edit or Delete Books", None))
        self.booksAvailLabel_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">1569</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Books Available</span></p><p><br/></p></body></html>", None))
        self.booksAvailLabel_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">1569</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Books Available</span></p><p><br/></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">25</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Books burrowed today</span></p><p><br/></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">69</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Pending Requests</span></p><p><br/></p></body></html>", None))
        self.allbooksLable_18.setText(QCoreApplication.translate("MainWindow", u"Client Data", None))
#if QT_CONFIG(tooltip)
        self.CircularProgress_2.setToolTip(QCoreApplication.translate("MainWindow", u"Male female ratio", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.CircularProgress_5.setToolTip(QCoreApplication.translate("MainWindow", u"Visitor ratio", None))
#endif // QT_CONFIG(tooltip)
        self.allbooksLable_19.setText(QCoreApplication.translate("MainWindow", u"Males", None))
        self.allbooksLable_20.setText(QCoreApplication.translate("MainWindow", u"Females", None))
        self.allbooksLable_21.setText(QCoreApplication.translate("MainWindow", u"Visitors", None))
        self.allbooksLable_22.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.allbooksLable_23.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.allbooksLable_24.setText(QCoreApplication.translate("MainWindow", u"Visitors to the library over the last 7 days", None))
        self.groupBox_8.setTitle("")
        self.fifth_val_3.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.forth_val_3.setText(QCoreApplication.translate("MainWindow", u"400", None))
        self.thr_val_3.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.sec_val_3.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.first_val_3.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Mon", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Tue", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Wed", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Thu", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Frid", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Sat", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Sun", None))
        self.booksAvailLabel_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">1569</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Books Available</span></p><p><br/></p></body></html>", None))
        self.booksAvailLabel_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">1569</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Books Available</span></p><p><br/></p></body></html>", None))
    # retranslateUi

