import pickle

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class SelectSubsTable(QTableWidget):

    def __init__(self, fg_sets_dict):
        super().__init__()
        self.fg_sets_dict = fg_sets_dict

        self.horizontalHeader().setVisible(False)

        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.populate_table()

    def populate_table(self):
        self.setRowCount(len(self.fg_sets_dict))
        self.setColumnCount(8)
        self.setVerticalHeaderLabels([key for key in self.fg_sets_dict.keys()])
        row = 0
        column_count = 8
        for key in self.fg_sets_dict.keys():
            column = 0
            for item in self.fg_sets_dict[key]:
                if column > column_count:
                    column_count = column
                    self.setColumnCount(column_count)
                table_item = QTableWidgetItem(item)
                self.setItem(row, column, table_item)
                column += 1   
            row += 1

    def load_functional_group_sets(self):
        fg_sets_in = open("fg_sets_dict.pickle", "rb")
        self.fg_sets_dict = pickle.load(fg_sets_in)
        fg_sets_in.close()