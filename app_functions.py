################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from main import *


class Functions:
    pass
    # def show_all_operations(self):
    #     self.ui.tableWidget_2.setRowCount(0)
    #     self.ui.tableWidget_2.insertRow(0)
    #     self.cur.execute('''
    #        SELECT transaction_id, client, username, book_id, activity, date, return_date, location, remarks FROM operations
    #        ''')
    #     data = self.cur.fetchall()
    #     if data:
    #         for row, form in enumerate(data):
    #             for column, item in enumerate(form):
    #                 self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
    #             current_row = self.ui.tableWidget_2.rowCount()
    #             self.ui.tableWidget_2.insertRow(current_row)
