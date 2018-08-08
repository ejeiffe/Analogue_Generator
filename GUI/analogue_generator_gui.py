import os
import sys
import pickle

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from initialise_dictionaries import *
from tab_widget import *

class AGMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Analogue Generator")
        self.setMinimumHeight(300)
        self.setMinimumWidth(500)

        self.set_up_dictionaries()

        self.central_widget = AGTabs(self.fg_dict, self.fg_sets_dict)
        self.setCentralWidget(self.central_widget)

        self.central_widget.generate_analogues_exit_button.clicked.connect(self.close)
        self.central_widget.custom_groups_exit_button.clicked.connect(self.close)
        self.central_widget.custom_sets_exit_button.clicked.connect(self.close)

    def load_functional_groups(self):
        fg_in = open("fg_dict.pickle", "rb")
        self.fg_dict = pickle.load(fg_in)
        fg_in.close()

    def load_functional_group_sets(self):  
        fg_sets_in = open("fg_sets_dict.pickle", "rb")
        self.fg_sets_dict = pickle.load(fg_sets_in)
        fg_sets_in.close()

    def set_up_dictionaries(self):
        if os.path.exists("fg_dict.pickle"):
            self.load_functional_groups()
        else:
            self.fg_dict = functional_groups
        if os.path.exists("fg_sets_dict.pickle"):
            self.load_functional_group_sets()
        else:
            self.fg_sets_dict = fg_sets_dict

if __name__ == "__main__":
    analogue_generator = QApplication(sys.argv)
    main_window = AGMainWindow()
    main_window.show()
    main_window.raise_()
    analogue_generator.exec_()

    