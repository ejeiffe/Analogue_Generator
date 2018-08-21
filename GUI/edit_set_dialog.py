from collections import OrderedDict

from PyQt5.QtWidgets import *

from dict_manager import *
from select_substituents_dialog import *

class EditSetDialog(QDialog):

    def __init__(self, set_name):
        super().__init__()
        self.set_name = set_name
        self.dict_manager = DictManager()
        self.groups = self.dict_manager.fg_sets_dict[set_name]
        self.new_groups = self.groups
        self.set_changed = False

        self.setWindowTitle("Edit Set")

        self.set_name_label = QLabel("Set name: ")
        self.set_name_line_edit = QLineEdit()
        self.set_name_line_edit.setText(self.set_name)
        self.set_contains_label = QLabel("Set contains: ")
        self.set_groups_label = QLabel(", ".join(self.groups))
        self.select_groups_button = QPushButton("Select Groups")
      
        self.save_changes_button = QPushButton("Save Changes")
        self.save_changes_button.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")

        self.edit_set_button_layout = QHBoxLayout()
        self.edit_set_button_layout.addWidget(self.save_changes_button)
        self.edit_set_button_layout.addWidget(self.cancel_button)

        self.edit_set_layout = QVBoxLayout()
        self.edit_set_layout.addWidget(self.set_name_label)
        self.edit_set_layout.addWidget(self.set_name_line_edit)
        self.edit_set_layout.addWidget(self.set_contains_label)
        self.edit_set_layout.addWidget(self.set_groups_label)
        self.edit_set_layout.addWidget(self.select_groups_button)
        self.edit_set_layout.addLayout(self.edit_set_button_layout)
        self.setLayout(self.edit_set_layout)

        self.set_name_line_edit.textChanged.connect(self.enable_save_button)
        self.select_groups_button.clicked.connect(self.open_selection_dialog)
        self.save_changes_button.clicked.connect(self.save_changes)
        self.cancel_button.clicked.connect(self.close)

    def enable_save_button(self):
        self.save_changes_button.setEnabled(True)

    def open_selection_dialog(self):
        set_name = self.set_name_line_edit.text()
        select_subs_dialog = SelectSubsEditSetDialog(set_name)
        select_subs_dialog.exec_()
        self.new_groups = select_subs_dialog.substituents
        self.set_groups_label.setText(", ".join(self.new_groups))
        self.enable_save_button()

    def save_changes(self):
        new_set_name = self.set_name_line_edit.text()
        if new_set_name != self.set_name:
            new_sets_dict = OrderedDict((new_set_name if k == self.set_name else k, v) for k,v in self.dict_manager.fg_sets_dict.items())
            new_sets_dict[new_set_name] = self.new_groups
            self.dict_manager.fg_sets_dict = new_sets_dict 
        else:
            self.dict_manager.fg_sets_dict[self.set_name] = self.new_groups
        self.dict_manager.save_functional_group_sets()
        self.set_changed = True
        self.close()
