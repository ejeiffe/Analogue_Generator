from PyQt5.QtWidgets import *

from dict_manager import *

class NewSetDialog(QDialog):

    def __init__(self, groups):
        super().__init__()
        self.groups = groups
        self.dict_manager = DictManager()
        self.new_set_saved = False

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
        if set_name in self.dict_manager.fg_sets_dict:
            invalid_name_message = QMessageBox()
            invalid_name_message.setWindowTitle("Invalid Set Name")
            invalid_name_message.setText(f"The group '{set_name}' already exists. Please choose another name")
            invalid_name_message.exec_()
        else:
            self.dict_manager.fg_sets_dict[set_name] = self.groups
            self.dict_manager.save_functional_group_sets()
            self.new_set_saved = True
            self.close()

        
