from PyQt5.QtWidgets import *

from dict_manager import *

class SaveSelectionDialog(QDialog):

    def __init__(self, selection):
        super().__init__()
        self.selection = selection
        self.dict_manager = DictManager()
        self.substituents_label_text = ', '.join(selection)
        self.new_set_saved = False

        self.setWindowTitle("Save Selection as Set")

        self.selected_groups_label = QLabel("Selected groups: ")
        self.substituents_label = QLabel(self.substituents_label_text)
        self.custom_set_name_label = QLabel("Enter a name for the functional group set:")
        self.custom_set_name_line_edit = QLineEdit()

        self.save_button = QPushButton("Save Custom Set")
        self.save_button.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")

        self.save_selection_button_layout = QHBoxLayout()
        self.save_selection_button_layout.addWidget(self.save_button)
        self.save_selection_button_layout.addWidget(self.cancel_button)

        self.save_selection_layout = QVBoxLayout()
        self.save_selection_layout.addWidget(self.selected_groups_label)
        self.save_selection_layout.addWidget(self.substituents_label)
        self.save_selection_layout.addWidget(self.custom_set_name_label)
        self.save_selection_layout.addWidget(self.custom_set_name_line_edit)
        self.save_selection_layout.addLayout(self.save_selection_button_layout)
        self.setLayout(self.save_selection_layout)

        self.custom_set_name_line_edit.textChanged.connect(self.enable_save_button)
        self.save_button.clicked.connect(self.save_custom_set)
        self.cancel_button.clicked.connect(self.close)

    def enable_save_button(self):
        self.save_button.setEnabled(True)

    def save_custom_set(self):
        custom_set_name = self.custom_set_name_line_edit.text()
        self.dict_manager.fg_sets_dict[custom_set_name] = self.selection
        self.dict_manager.save_functional_group_sets()
        self.new_set_saved = True
        self.close()

