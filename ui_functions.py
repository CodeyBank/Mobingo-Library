from main import *

# ## ==> APP FUNCTIONS
# from app_functions import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUNT INITIAL MENU
count = 1


class UIFunctions(MainWindow, loginWindow):
    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    # #######################################################################
    # START - GUI FUNCTIONS
    # #######################################################################

    # MAXIMIZE/RESTORE
    # #######################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.maximizeRestoreBtn.setToolTip("Restore")
            self.ui.maximizeRestoreBtn.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.maximizeRestoreBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreBtn.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))

    ## ==> RETURN STATUS
    def returStatus(self):
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.sideBar.width()
            maxExtend = maxWidth
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.sideBar, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def adjustTableWidget(self):
        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setVisible(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableWidget_2.horizontalHeader().setVisible(True)
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    def selectMenu(getStyle):
        select = getStyle + ("\nQPushButton { "
                             "border-left: 5px solid qlineargradient(spread:pad, x1:0.006, y1:0.699182, x2:0.993128, "
                             "y2:0.325, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 "
                             "rgba(98, 114, 164, 255));"
                             "background-color: rgba(88, 91, 115, 150) }")
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(("\nQPushButton { "
                             "border-left: 5px solid qlineargradient(spread:pad, x1:0.006, y1:0.699182, x2:0.993128, "
                             "y2:0.325, stop:0.00627353 rgba(178, 138, 236, 255), stop:0.984012 "
                             "rgba(98, 114, 164, 255));"
                             "background-color: rgba(88, 91, 115, 150) }"), "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.top_Buttons.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        # search for all the objects (children) in the parent object
        for w in self.ui.top_Buttons.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # Adjust the size of the table headers to match the content
    def resize_tHeaders(self):
        t1 = range(0, 9)
        # t2 = range(0, 7)
        # t3 = range(0, 4)
        header_ops = self.ui.tableWidget_2.horizontalHeader()
        # header_allbooks = self.allbooks_table.horizontalHeader()
        # header_allclients = self.allclients_table.horizontalHeader()

        for item in t1:
            header_ops.setSectionResizeMode(item, QtWidgets.QHeaderView.ResizeToContents)
        # for item1 in t2:
        #     header_allbooks.setSectionResizeMode(item1, QtWidgets.QHeaderView.ResizeToContents)
        # for item2 in t3:
        #     header_allclients.setSectionResizeMode(item2, QtWidgets.QHeaderView.ResizeToContents)

    def filterOperations(self, querytype, filter):
        # Retrieve user inputs
        tID = self.ui.filterTransaction.text()
        userName = self.ui.filterBookTitle.text()
        clientName = self.ui.filterClientName.text()
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.insertRow(0)
        sql = ''' SELECT * FROM operations WHERE #column = "#value" '''
        if filter == 'trID':
            s1 = sql.replace('#column', querytype).replace("#value", tID)
            self.cur.execute(s1)
        elif filter == 'uName':
            s1 = sql.replace('#column', querytype).replace("#value", userName)
            self.cur.execute(s1)
        elif filter == 'clName':
            s1 = sql.replace('#column', querytype).replace("#value", clientName)
            self.cur.execute(s1)
        else:
            pass
            # self.ui.statusBar().showMessage("Fields cannot be empty", 3000)

        data = self.cur.fetchall()
        if data:
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                current_row = self.ui.tableWidget_2.rowCount()
                self.ui.tableWidget_2.insertRow(current_row)
        else:
            print('nothing was found')
            # self.ui.statusBar().showMessage("No records found", 3000)

    # Handle error message boxes
    @staticmethod
    def showDialog(error_type, text, message):
        msg = QMessageBox()
        if error_type == 'information':
            msg.setIcon(QMessageBox.Information)
        if error_type == 'error':
            msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setInformativeText(message)
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok)
        retVal = msg.exec_()
        if retVal == QMessageBox.Ok:
            # self.closeWindow()
            pass

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def doubleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.topMenu.mouseDoubleClickEvent = doubleClickMaximizeRestore # signal to slot connection

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.baseFrame.setGraphicsEffect(self.shadow)

        ### ==> MINIMIZE
        self.ui.hideBtn.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.maximizeRestoreBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.closeWindowBtn.clicked.connect(lambda: self.close())

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################
