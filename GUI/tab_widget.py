from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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

        self.generate_analogues_exit_button = QPushButton("Exit")
        self.custom_groups_exit_button = QPushButton("Exit")
        self.custom_sets_exit_button = QPushButton("Exit")

        self.generate_analogues_layout = QVBoxLayout()
        self.generate_analogues_layout.addWidget(self.generate_analogues_exit_button, 0, Qt.AlignRight)
        self.generate_analogues_tab.setLayout(self.generate_analogues_layout)

        self.custom_groups_layout = QVBoxLayout()
        self.custom_groups_layout.addWidget(self.custom_groups_exit_button, 0, Qt.AlignRight)
        self.custom_groups_tab.setLayout(self.custom_groups_layout)

        self.custom_sets_layout = QVBoxLayout()
        self.custom_sets_layout.addWidget(self.custom_sets_exit_button, 0, Qt.AlignRight)
        self.custom_sets_tab.setLayout(self.custom_sets_layout)

        self.tab_widget_layout = QVBoxLayout()
        self.tab_widget_layout.addWidget(self.tabs)
        self.setLayout(self.tab_widget_layout)