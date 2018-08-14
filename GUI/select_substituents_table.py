from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from dict_manager import *

class SelectSubsTable(QTableWidget):

    def __init__(self):
        super().__init__()
        self.dict_manager = DictManager()

        self.horizontalHeader().setVisible(False)

        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.populate_table()

    def populate_table(self):
        self.dict_manager.load_functional_group_sets()
        self.setRowCount(len(self.dict_manager.fg_sets_dict))
        self.setColumnCount(8)
        self.setVerticalHeaderLabels([key for key in self.dict_manager.fg_sets_dict.keys()])
        row = 0
        column_count = 8
        for key in self.dict_manager.fg_sets_dict.keys():
            column = 0
            for item in self.dict_manager.fg_sets_dict[key]:
                if column > column_count:
                    column_count = column
                    self.setColumnCount(column_count)
                table_item = QTableWidgetItem(item)
                self.setItem(row, column, table_item)
                column += 1   
            row += 1

