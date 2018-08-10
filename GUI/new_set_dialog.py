import pickle

from PyQt5.QtWidgets import *

class NewSetDialog(QDialog):

    def __init__(self, group_name, fg_sets_dict):
        super().__init__()
        self.group_name = group_name
        self.fg_sets_dict = fg_sets_dict

        self.setWindowTitle("New Set")
        
        self.set_name_label = QLabel("Enter name for new set:")
        self.set_name_line_edit = QLineEdit()

        self.save_set_button = QPushButton("Save Set")
        self.set_name_label.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")

        self.new_set_button_layout = QHBoxLayout()
        self.new_set_button_layout.addWidget(self.save_set_button)
        self.new_set_button_layout.addWidget(self.cancel_button)

        self.new_set_layout = QVBoxLayout()
        self.new_set_layout.addWidget(self.set_name_label)
        self.new_set_layout.addWidget(self.set_name_line_edit)
        self.new_set_layout.addLayout(self.new_set_button_layout)
        self.setLayout(self.new_set_layout)

        self.set_name_line_edit.textChanged.connect(self.enable_save_button)
        self.save_set_button.clicked.connect(self.save_set)
        self.cancel_button.clicked.connect(self.close)

    def enable_save_button(self):
        self.save_set_button.setEnabled(True)

    def save_set(self):
        set_name = self.set_name_line_edit.text()
        self.fg_sets_dict[set_name] = list(self.group_name)
        self.save_functional_group_sets()
        self.close()

    def save_functional_group_sets(self):
        fg_sets_out = open("fg_sets_dict.pickle", "wb")
        pickle.dump(self.fg_sets_dict, fg_sets_out)
        fg_sets_out.close()
        
