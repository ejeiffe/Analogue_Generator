import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from tab_widget import *

class AGMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Analogue Generator")
        
        self.central_widget = AGTabs()
        self.setCentralWidget(self.central_widget)

        self.resize(800, 500)

        self.central_widget.generate_analogues_exit_button.clicked.connect(self.close)
        self.central_widget.manage_groups_exit_button.clicked.connect(self.close)
        self.central_widget.manage_sets_exit_button.clicked.connect(self.close)
        

if __name__ == "__main__":
    analogue_generator = QApplication(sys.argv)
    main_window = AGMainWindow()
    main_window.show()
    main_window.raise_()
    analogue_generator.exec_()

    