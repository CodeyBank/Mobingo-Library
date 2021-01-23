import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QGuiApplication)
from PySide2.QtWidgets import *
import pymysql
import pyautogui as sc
import datetime
import time
import random
import string

pymysql.install_as_MySQLdb()
import MySQLdb

# Import the uiFunctions file
from ui_functions import *
from app_functions import *
from ui_styles import *

# GUI FILE IMPORTS
from new_library import Ui_MainWindow
from login_ui import Ui_Dialog
from register_ui import Ui_Dialog_register
from newOperation import *


class MainWindow(QMainWindow):
    clickCount = 0
    currentUser = ''

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Instantiate method to handle all button clicks
        self.buttonHandler()

        # Connect to the database
        self.db = MySQLdb.connect(host='', user='', password='', db="library", port=)
        self.cur = self.db.cursor()

        # Adjust table widgets
        UIFunctions.adjustTableWidget(self)
        UIFunctions.resize_tHeaders(self)

        # Remove standard title bar
        UIFunctions.removeTitleBar(True)

        # Set initial window size
        startSize = QSize(1366, 768)
        self.resize(startSize)
        self.setMinimumSize(startSize)

        # Toggle side menu size
        self.ui.pushButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        # Set the default screen
        UIFunctions.selectStandardMenu(self, "dashBoardBtn")
        self.ui.stackedWidget.setCurrentWidget(self.ui.dashBoardPage)

        # Populate table data
        self.show_all_operations()

        # Move window, maximize and restore size
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # widget to move
        self.ui.topMenu.mouseMoveEvent = moveWindow

        # Load UI definitions
        UIFunctions.uiDefinitions(self)

        # Create and Activate timer
        self.timer = QTimer(self)
        self.timer.setInterval(60000)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start()

    # mousePressEvent is a Qt Mouse Event handler
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def logOut(self):
        self.loginWin = loginWindow()
        self.close()
        self.loginWin.show()

    def buttonHandler(self):
        # this handles filters on the dashboard table
        self.ui.transactionFilter.clicked.connect(lambda: UIFunctions.filterOperations(self, 'transaction_id', 'trID'))
        self.ui.usernameFiler.clicked.connect(lambda: UIFunctions.filterOperations(self, 'username', 'uName'))
        self.ui.bookTitleFIlter.clicked.connect(lambda: UIFunctions.filterOperations(self, 'client', 'clName'))
        self.ui.clearFilterBtn.clicked.connect(self.show_all_operations)

        # Navigation buttons on the side menu
        self.ui.dashBoardBtn.clicked.connect(self.navigationButtons)
        self.ui.booksButton.clicked.connect(self.navigationButtons)
        self.ui.usersBtn.clicked.connect(self.navigationButtons)
        self.ui.settingsBtn.clicked.connect(self.navigationButtons)
        self.ui.statisticsBtn.clicked.connect(self.navigationButtons)
        # Shutdown button
        self.ui.closeWindowBtn.clicked.connect(self.logOut)
        # Popup windows
        self.ui.addNewOpBtn.clicked.connect(self.addNewOps)

    def addNewOps(self):
        self.window4 = addNewOperation()
        self.window4.show()

    def navigationButtons(self):
        btnWidget = self.sender()
        if btnWidget.objectName() == 'dashBoardBtn':
            print('dash board button pressed')
            self.ui.stackedWidget.setCurrentWidget(self.ui.dashBoardPage)
            UIFunctions.resetStyle(self, 'dashBoardBtn')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == 'booksButton':
            print('users button pressed')
            self.ui.stackedWidget.setCurrentWidget(self.ui.booksPage)
            UIFunctions.resetStyle(self, 'booksButton')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == 'usersBtn':
            print('users button pressed')
            self.ui.stackedWidget.setCurrentWidget(self.ui.usersPage)
            UIFunctions.resetStyle(self, 'usersBtn')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == 'settingsBtn':
            print("settings button pressed")
            self.ui.stackedWidget.setCurrentWidget(self.ui.settingsPage)
            UIFunctions.resetStyle(self, 'settingsBtn')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        if btnWidget.objectName() == 'statisticsBtn':
            print('statistics button pressed')
            self.ui.stackedWidget.setCurrentWidget(self.ui.statisticsPage)
            UIFunctions.resetStyle(self, 'statisticsBtn')
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    def show_all_operations(self):
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.insertRow(0)
        self.cur.execute('''
              SELECT transaction_id, client, username, book_id, activity, date, return_date, location, remarks FROM operations
              ''')
        data = self.cur.fetchall()
        if data:
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                current_row = self.ui.tableWidget_2.rowCount()
                self.ui.tableWidget_2.insertRow(current_row)

    def updateTime(self):
        toDay = datetime.datetime.today()
        dt_string = toDay.strftime("%A %d %B, %Y %I:%M")
        # set AM or PM value
        if toDay.hour >= 12:
            amPM = ' PM'
        else:
            amPM = ' AM'
        self.ui.dateTime.setText(dt_string + amPM)


class loginWindow(QDialog):
    initial = ''

    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.count = 0
        # Connect to the database
        self.db = MySQLdb.connect(host='localhost', user='root', password='Thebossm@#995', db="library", port=3310)
        self.cur = self.db.cursor()  # Create a cursor

        # Call button handler function
        self.buttonHandler()

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

    def loginHandler(self):
        username = self.ui.usernameLEdit.text()
        password = self.ui.passwordLEdit.text()
        sql = '''SELECT * FROM users '''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                self.ui.error_label.setText('')
                initial = (row[1][0].upper() + row[1][1].upper())
                print(initial)
                self.window2 = MainWindow()
                self.close()
                self.window2.show()
                self.window2.ui.user_initialsLabel.setText(initial)
                MainWindow.currentUser = username
            else:
                self.ui.error_label.setText('Invalid credentials, please try again')

    def buttonHandler(self):
        self.ui.pushButton_4.clicked.connect(self.loginHandler)
        self.ui.logOffBtn.clicked.connect(self.closeWindow)
        self.ui.signUpBtn.clicked.connect(self.openRegisterWindow)
        self.ui.viewPasswordBtn.clicked.connect(self.showPassword)

    def closeWindow(self):
        self.close()

    def openRegisterWindow(self):
        self.regWindow = registerWindow()
        self.close()
        self.regWindow.show()

    def showPassword(self):
        if self.count == 0:
            self.ui.passwordLEdit.setEchoMode(QLineEdit.Normal)
            self.count = 1
        elif self.count == 1:
            self.ui.passwordLEdit.setEchoMode(QLineEdit.Password)
            self.count = 0


class registerWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.ui = Ui_Dialog_register()
        self.ui.setupUi(self)

        self.count = 1
        # Connect to the database
        self.db = MySQLdb.connect(host='', user='', password='', db="library", port=)
        self.cur = self.db.cursor()  # Create a cursor
        # Call button handler function
        self.buttonHandler1()

        # Remove default title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

    def passwordValidation(self):
        self.ui.error_labelPW.setText('')
        specialCharacters = ["@", '#', '$', '%', '^', '&', '(', ')', '-', "=", "+", '<', '>']
        password = self.ui.passwordLEdit_2.text()
        rep_password = self.ui.repeatpasswordLEdit_3.text()
        errorFlag = False
        check = []

        print(password, rep_password)
        if password != rep_password:
            errorFlag = True
            self.ui.error_labelPW.setText('Passwords do not match')
            print("mismatch")

        if len(password) < 5:
            errorFlag = True
            self.ui.error_labelPW.setText('Password too short')
            print("too short")
        # confirm that there is a special character in the password
        for character in specialCharacters:
            if character not in password:
                check.append('N')
                # print('special character not found')
            else:
                check.append('Y')
        if 'Y' not in check:
            errorFlag = True
            self.ui.error_labelPW.setText('Password must contain special characters')
            print('special character not found')

        if (password == '') and (rep_password == ''):
            errorFlag = True
            self.ui.error_labelPW.setText('Password fields cannot be empty')
            print('empty field')

        return errorFlag

    def usernameValidation(self):
        self.ui.error_labelUN.setText('')
        username = self.ui.usernameLEdit.text()
        errorFlagUN = False
        sql = ''' SELECT * from users'''
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1]:
                self.ui.error_labelUN.setText('Username already exists')
                errorFlagUN = True
        if username == '':
            self.ui.error_labelUN.setText('Username field cannot be empty')
            errorFlagUN = True
        elif len(username) < 4:
            errorFlagUN = True
            self.ui.error_labelUN.setText('Username too short')
        return errorFlagUN

    def emailValidation(self):
        errorFlagEM = False
        email = self.ui.emailLEdit.text()
        self.ui.error_labelEM.setText('')

        for character in email:
            if '@' not in email:
                self.ui.error_labelEM.setText('Invalid Email address')
                errorFlagEM = True
        return errorFlagEM

    def addUser(self):
        password = self.ui.passwordLEdit_2.text()
        username = self.ui.usernameLEdit.text()
        email = self.ui.emailLEdit.text()
        er1 = self.emailValidation()
        er2 = self.usernameValidation()
        er3 = self.passwordValidation()

        if (not er1) and (not er2) and (not er3):
            self.cur.execute('''
                    INSERT INTO users(user_name, user_email, user_password) VALUES(%s, %s, %s)
                    ''', (username, email, password))
            self.db.commit()
            self.ui.successLabel.setText('User added successfully. Go back to login page')

    def buttonHandler1(self):
        self.ui.pushButton_4.clicked.connect(self.addUser)
        self.ui.signUpBtn.clicked.connect(self.loginWindowOpen)
        self.ui.logOffBtn.clicked.connect(self.closeWindow)
        self.ui.viewPasswordBtn.clicked.connect(self.showPassword)

    def closeWindow(self):
        self.close()

    def loginWindowOpen(self):
        self.window1 = loginWindow()
        self.close()
        self.window1.show()

    def showPassword(self):
        if self.count == 0:
            self.ui.passwordLEdit_2.setEchoMode(QLineEdit.Normal)
            self.ui.repeatpasswordLEdit_3.setEchoMode(QLineEdit.Normal)
            self.count = 1
        elif self.count == 1:
            self.ui.passwordLEdit_2.setEchoMode(QLineEdit.Password)
            self.ui.repeatpasswordLEdit_3.setEchoMode(QLineEdit.Password)
            self.count = 0


class addNewOperation(QDialog, MainWindow):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.ui = Ui_Dialog_newOperation()
        self.ui.setupUi(self)
        self.mainUI = MainWindow()

        # Connect to the database
        self.db = MySQLdb.connect(host='localhost', user='root', password='Thebossm@#995', db="library", port=3310)
        self.cur = self.db.cursor()  # Create a cursor

        # REMOVE  STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)

        # Initialize transaction Id generator function
        self.createTransactionId()
        self.var = ''

        self.ui.addButton.clicked.connect(self.addNewOperationToDB)
        self.ui.closeBtn.clicked.connect(self.closeWindow)

    def addNewOperationToDB(self):
        noDays = self.ui.spinBox.value()
        # Retrieve information in the line edits
        client = self.ui.lineEdit.text()
        activity = self.ui.comboBox.currentText()
        bookID = self.ui.lineEdit_3.text()
        location = self.ui.lineEdit_5.text()
        remarks = self.ui.textEdit.toPlainText()
        username = MainWindow.currentUser
        dateOfOps = datetime.date.today()
        now = time.localtime()
        operation_time = time.strftime("%H:%M:%S", now)
        transactionID = addNewOperation.var
        to = dateOfOps + datetime.timedelta(days=int(noDays))
        # make sure number of days is set
        if client and activity and bookID and location and remarks:
            self.cur.execute('''
                                INSERT INTO operations (transaction_id, client, username, book_id, activity, date, return_date, location, remarks)
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                            ''',
                             (transactionID, client, username, bookID, activity, operation_time, to, location, remarks))
            self.db.commit()
            self.showDialog('information', 'Successful Operation', 'Operation has been added to database successfully')

            self.mainUI.show_all_operations()

        else:
            self.showDialog('error', 'Error', 'Field cannot be empty')
            self.mainUI.mumu()

        # Add information to the database

    def showDialog(self, error_type, text, message):
        msg = QMessageBox()
        if error_type == 'information':
            msg.setIcon(QMessageBox.Information)
        if error_type == 'error':
            msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setInformativeText(message)
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Retry)
        retVal = msg.exec_()
        if retVal == QMessageBox.Ok:
            self.closeWindow()

    def createTransactionId(self):
        # generate Transaction ID
        int1 = random.randint(0, 9)
        int2 = random.randint(0, 9)
        letters = string.ascii_uppercase
        result_str = ''.join(random.choice(letters) for i in range(7))

        transactionID = '#' + str(int1) + str(int2) + result_str
        self.ui.transactionID.setText(transactionID)
        addNewOperation.var = transactionID

    def closeWindow(self):
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainView = MainWindow()
    mainView.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
