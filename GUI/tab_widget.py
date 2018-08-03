from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from smiles_generator import *

class AGTabs(QWidget):

    def __init__(self, fg_dict, fg_sets_dict):
        super().__init__()
        self.fg_dict = fg_dict
        self.fg_sets_dict = fg_sets_dict

        self.tabs = QTabWidget()
        self.generate_analogues_tab = QWidget()
        self.custom_groups_tab = QWidget()
        self.custom_sets_tab = QWidget()

        self.tabs.addTab(self.generate_analogues_tab, "Generate Analogues")
        self.tabs.addTab(self.custom_groups_tab, "Custom Groups")
        self.tabs.addTab(self.custom_sets_tab, "Custom Sets")

        self.enter_smiles_label = QLabel("Enter SMILES string:")
        self.enter_smiles_line_edit = QLineEdit()
        self.submit_smiles_button = QPushButton("Submit")
        self.generate_analogues_exit_button = QPushButton("Exit")

        self.r_groups_layout = QGridLayout()
        self.r_groups_layout.addWidget(QLabel("R Group"),0,0)
        self.r_groups_layout.addWidget(QLabel("Substituents"),0,1)
        
        self.generate_analogues_top_layout = QHBoxLayout()
        self.generate_analogues_top_layout.addWidget(self.enter_smiles_label)
        self.generate_analogues_top_layout.addWidget(self.enter_smiles_line_edit)
        self.generate_analogues_top_layout.addWidget(self.submit_smiles_button)

        self.generate_analogues_layout = QVBoxLayout()
        self.generate_analogues_layout.addLayout(self.generate_analogues_top_layout)
        self.generate_analogues_layout.addLayout(self.r_groups_layout)
        self.generate_analogues_layout.addWidget(self.generate_analogues_exit_button, 0, Qt.AlignRight)
        self.generate_analogues_tab.setLayout(self.generate_analogues_layout)

        self.custom_groups_exit_button = QPushButton("Exit")
        
        self.custom_groups_layout = QVBoxLayout()
        self.custom_groups_layout.addWidget(self.custom_groups_exit_button, 0, Qt.AlignRight)
        self.custom_groups_tab.setLayout(self.custom_groups_layout)

        self.custom_sets_exit_button = QPushButton("Exit")

        self.custom_sets_layout = QVBoxLayout()
        self.custom_sets_layout.addWidget(self.custom_sets_exit_button, 0, Qt.AlignRight)
        self.custom_sets_tab.setLayout(self.custom_sets_layout)

        self.tab_widget_layout = QVBoxLayout()
        self.tab_widget_layout.addWidget(self.tabs)
        self.setLayout(self.tab_widget_layout)

        self.submit_smiles_button.clicked.connect(self.get_r_groups)

    def get_r_groups(self):
        self.smiles_generator = SmilesGenerator(self.enter_smiles_line_edit.text())
        self.r_group_select_buttons = {}
        row = 1
        for r_group in sorted(self.smiles_generator.r_groups):
            self.r_group_select_buttons[r_group] = QPushButton("Select")
            self.r_groups_layout.addWidget(QLabel(r_group),row,0)
            self.r_groups_layout.addWidget(self.r_group_select_buttons[r_group],row,2)
            row += 1
