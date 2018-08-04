from PyQt5.QtWidgets import *

class SelectSubsDialog(QDialog):

    def __init__(self, r_group, fg_sets_dict):
        super().__init__()
        self.r_group = r_group
        self.fg_sets_dict = fg_sets_dict

        self.setWindowTitle(f"Select Substituents for {self.r_group}")

        self.save_button = QPushButton("Save Selection")
        self.cancel_button = QPushButton("Cancel")

        self.select_subs_button_layout = QHBoxLayout()
        self.select_subs_button_layout.addWidget(self.save_button)
        self.select_subs_button_layout.addWidget(self.cancel_button)

        self.select_subs_layout = QVBoxLayout()
        self.select_subs_layout.addLayout(self.select_subs_button_layout)
        self.setLayout(self.select_subs_layout)

        self.cancel_button.clicked.connect(self.close)

