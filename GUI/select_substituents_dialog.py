from PyQt5.QtWidgets import *

from select_substituents_table import *
from save_selection_dialog import *

class SelectSubsDialog(QDialog):

    def __init__(self, r_group, fg_sets_dict):
        super().__init__()
        self.r_group = r_group
        self.fg_sets_dict = fg_sets_dict
        self.substituents = None
        self.new_set_saved = False

        self.setWindowTitle(f"Select Substituents for {self.r_group}")

        self.instructions_label = QLabel("Ctrl + click to select multiple items.")

        self.select_subs_table = SelectSubsTable(self.fg_sets_dict)

        self.save_button = QPushButton("Save Selection")
        self.save_button.setEnabled(False)
        self.save_as_set_button = QPushButton("Save Selection as Set")
        self.save_as_set_button.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")

        self.select_subs_button_layout = QHBoxLayout()
        self.select_subs_button_layout.addWidget(self.save_button)
        self.select_subs_button_layout.addWidget(self.save_as_set_button)
        self.select_subs_button_layout.addWidget(self.cancel_button)

        self.select_subs_layout = QVBoxLayout()
        self.select_subs_layout.addWidget(self.instructions_label)
        self.select_subs_layout.addWidget(self.select_subs_table)
        self.select_subs_layout.addLayout(self.select_subs_button_layout)
        self.setLayout(self.select_subs_layout)

        self.select_subs_table.itemSelectionChanged.connect(self.enable_save_buttons)
        self.save_button.clicked.connect(self.save_substituents)
        self.save_as_set_button.clicked.connect(self.save_selection)
        self.cancel_button.clicked.connect(self.close)

    def enable_save_buttons(self):
        self.save_button.setEnabled(True)
        self.save_as_set_button.setEnabled(True)

    def get_substituents(self):
        self.substituents = [item.text() for item in self.select_subs_table.selectedItems()]
        self.substituents = list(set(self.substituents))
        
    def save_substituents(self):
        self.get_substituents()
        self.close()

    def save_selection(self):
        self.get_substituents()
        save_selection_dialog = SaveSelectionDialog(self.substituents, self.fg_sets_dict)
        save_selection_dialog.exec_()
        if save_selection_dialog.new_set_saved:
            self.new_set_saved = True
        self.close()




