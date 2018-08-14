from PyQt5.QtWidgets import *

from dict_manager import *
from add_to_set_dialog import *

class NewGroupDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.dict_manager = DictManager()
        self.group_added = False

        self.setWindowTitle("New Functional Group")

        self.group_name_label = QLabel("Functional group name: ")
        self.group_name_line_edit = QLineEdit()
        self.smiles_info_label = QLabel("""Note that two SMILES strings should be entered for groups containing ring structures to ensure correct connectivity.\n 
The first SMILES string will be used when the corresponding R group is in the middle or at the end of the input string.\n 
The second SMILES string will be used when the R group is at the beginning of the input string.""", wordWrap = True)
        self.first_smiles_label = QLabel("SMILES (middle/end of string):")
        self.first_smiles_line_edit = QLineEdit()
        self.second_smiles_label = QLabel("Optional - SMILES (beginning of string):")
        self.second_smiles_line_edit = QLineEdit()

        self.save_group_button = QPushButton("Save Group")
        self.save_group_button.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")

        self.new_group_button_layout = QHBoxLayout()
        self.new_group_button_layout.addWidget(self.save_group_button)
        self.new_group_button_layout.addWidget(self.cancel_button)

        self.new_group_layout = QVBoxLayout()
        self.new_group_layout.addWidget(self.group_name_label)
        self.new_group_layout.addWidget(self.group_name_line_edit)
        self.new_group_layout.addWidget(self.smiles_info_label)
        self.new_group_layout.addWidget(self.first_smiles_label)
        self.new_group_layout.addWidget(self.first_smiles_line_edit)
        self.new_group_layout.addWidget(self.second_smiles_label)
        self.new_group_layout.addWidget(self.second_smiles_line_edit)
        self.new_group_layout.addLayout(self.new_group_button_layout)
        self.setLayout(self.new_group_layout)

        self.group_name_line_edit.textChanged.connect(self.enable_save_button)
        self.first_smiles_line_edit.textChanged.connect(self.enable_save_button)
        self.save_group_button.clicked.connect(self.save_group)
        self.cancel_button.clicked.connect(self.close)

    def enable_save_button(self):
        if self.group_name_line_edit.text() != "" and self.first_smiles_line_edit.text() != "":
            self.save_group_button.setEnabled(True)

    def save_group(self):
        group_name = self.group_name_line_edit.text()
        first_smiles = self.first_smiles_line_edit.text()
        second_smiles = self.second_smiles_line_edit.text()
        if group_name in self.dict_manager.fg_dict:
            invalid_name_message = QMessageBox()
            invalid_name_message.setWindowTitle("Invalid Group Name")
            invalid_name_message.setText(f"The group '{group_name}' already exists. Please choose another name")
            invalid_name_message.exec_()
        else:
            if second_smiles != "":
                self.dict_manager.fg_dict[group_name] = (first_smiles, second_smiles)
            else:
                self.dict_manager.fg_dict[group_name] = (first_smiles,)
            self.open_add_to_set_dialog(group_name)
            self.dict_manager.save_functional_groups()
            self.group_added = True
            self.close()

    def open_add_to_set_dialog(self, group_name):
        add_to_set_dialog = AddToSetDialog([group_name])
        add_to_set_dialog.exec_()
        



