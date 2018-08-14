from PyQt5.QtWidgets import *

from dict_manager import *

class ViewSmilesDialog(QDialog):

    def __init__(self, group_name):
        super().__init__()
        self.group_name = group_name
        self.dict_manager = DictManager()
        self.smiles_changed = False

        self.setWindowTitle(f"SMILES for {self.group_name}")

        self.first_smiles_label = QLabel("SMILES (middle/end of string):")
        self.first_smiles_line_edit = QLineEdit()
        self.second_smiles_label = QLabel("Optional - SMILES (beginning of string):")
        self.second_smiles_line_edit = QLineEdit()

        self.first_smiles_line_edit.setText(self.dict_manager.fg_dict[self.group_name][0])
        if len(self.dict_manager.fg_dict[self.group_name]) == 2:
            self.second_smiles_line_edit.setText(self.dict_manager.fg_dict[self.group_name][1])

        self.save_changes_button = QPushButton("Save Changes")
        self.save_changes_button.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")

        self.view_smiles_button_layout = QHBoxLayout()
        self.view_smiles_button_layout.addWidget(self.save_changes_button)
        self.view_smiles_button_layout.addWidget(self.cancel_button)

        self.view_smiles_layout = QVBoxLayout()
        self.view_smiles_layout.addWidget(self.first_smiles_label)
        self.view_smiles_layout.addWidget(self.first_smiles_line_edit)
        self.view_smiles_layout.addWidget(self.second_smiles_label)
        self.view_smiles_layout.addWidget(self.second_smiles_line_edit)
        self.view_smiles_layout.addLayout(self.view_smiles_button_layout)
        self.setLayout(self.view_smiles_layout)

        self.first_smiles_line_edit.textChanged.connect(self.enable_save_button)
        self.second_smiles_line_edit.textChanged.connect(self.enable_save_button)
        self.save_changes_button.clicked.connect(self.confirm_save)
        self.cancel_button.clicked.connect(self.close)

    def enable_save_button(self):
        self.save_changes_button.setEnabled(True)

    def confirm_save(self):
        confirm_save_message = QMessageBox()
        confirm_save_message.setWindowTitle("Save changes to SMILES")
        confirm_save_message.setText(f"Are you sure you want to change the SMILES string for {self.group_name}?")
        confirm_save_message.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        confirm = confirm_save_message.exec_()
        if confirm == QMessageBox.Save:
            self.save_smiles()     

    def save_smiles(self):
        first_smiles = self.first_smiles_line_edit.text()
        second_smiles = self.second_smiles_line_edit.text()
        if second_smiles != "":
            self.dict_manager.fg_dict[self.group_name] = (first_smiles, second_smiles)
        else:
            self.dict_manager.fg_dict[self.group_name] = (first_smiles,)
        self.dict_manager.save_functional_groups()
        self.smiles_changed = True
        self.close()
