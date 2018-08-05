from PyQt5.QtWidgets import *

from select_substituents_table import *

class SelectSubsDialog(QDialog):

    def __init__(self, r_group, fg_sets_dict):
        super().__init__()
        self.r_group = r_group
        self.fg_sets_dict = fg_sets_dict
        self.substituents = None

        self.setWindowTitle(f"Select Substituents for {self.r_group}")

        self.instructions_label = QLabel("Ctrl + click to select multiple items.")

        self.select_subs_table = SelectSubsTable(self.r_group, self.fg_sets_dict)

        self.save_button = QPushButton("Save Selection")
        self.save_button.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")

        self.select_subs_button_layout = QHBoxLayout()
        self.select_subs_button_layout.addWidget(self.save_button)
        self.select_subs_button_layout.addWidget(self.cancel_button)

        self.select_subs_layout = QVBoxLayout()
        self.select_subs_layout.addWidget(self.instructions_label)
        self.select_subs_layout.addWidget(self.select_subs_table)
        self.select_subs_layout.addLayout(self.select_subs_button_layout)
        self.setLayout(self.select_subs_layout)

        self.select_subs_table.itemSelectionChanged.connect(self.enable_save_button)
        self.save_button.clicked.connect(self.get_substituents)
        self.cancel_button.clicked.connect(self.close)

    def enable_save_button(self):
        self.save_button.setEnabled(True)

    def get_substituents(self):
        self.substituents = [item.text() for item in self.select_subs_table.selectedItems()]
        self.close()



