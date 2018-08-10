import csv
import pickle
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from smiles_generator import *
from select_substituents_dialog import *
from new_group_dialog import *

class AGTabs(QWidget):

    def __init__(self, fg_dict, fg_sets_dict):
        super().__init__()
        self.fg_dict = fg_dict
        self.fg_sets_dict = fg_sets_dict

        self.tabs = QTabWidget()
        self.generate_analogues_tab = QWidget()
        self.manage_groups_tab = QWidget()
        self.manage_sets_tab = QWidget()
        
        self.tabs.addTab(self.generate_analogues_tab, "Generate Analogues")
        self.tabs.addTab(self.manage_groups_tab, "Manage Functional Groups")
        self.tabs.addTab(self.manage_sets_tab, "Manage Sets")
        
        self.enter_smiles_label = QLabel("Enter SMILES string:")
        self.enter_smiles_line_edit = QLineEdit()
        self.submit_smiles_button = QPushButton("Submit")
        self.generate_csv_button = QPushButton("Generate CSV File")
        self.generate_csv_button.setEnabled(False)
        self.generate_analogues_exit_button = QPushButton("Exit")

        self.r_groups_layout = QGridLayout()
        self.r_groups_layout.addWidget(QLabel("R Group"),0,0)
        self.r_groups_layout.addWidget(QLabel("Substituents"),0,1)

        self.generate_analogues_button_layout = QHBoxLayout()
        self.generate_analogues_button_layout.addWidget(self.generate_csv_button)
        self.generate_analogues_button_layout.addWidget(self.generate_analogues_exit_button, 0, Qt.AlignRight)
        
        self.generate_analogues_top_layout = QHBoxLayout()
        self.generate_analogues_top_layout.addWidget(self.enter_smiles_label)
        self.generate_analogues_top_layout.addWidget(self.enter_smiles_line_edit)
        self.generate_analogues_top_layout.addWidget(self.submit_smiles_button)

        self.generate_analogues_layout = QVBoxLayout()
        self.generate_analogues_layout.addLayout(self.generate_analogues_top_layout)
        self.generate_analogues_layout.addLayout(self.r_groups_layout)
        self.generate_analogues_layout.addLayout(self.generate_analogues_button_layout)
        self.generate_analogues_tab.setLayout(self.generate_analogues_layout)

        self.manage_groups_table = SelectSubsTable(self.fg_sets_dict)

        self.manage_groups_create_new_button = QPushButton("Create New Group")
        self.manage_groups_view_smiles_button = QPushButton("View SMILES")
        self.manage_groups_view_smiles_button.setEnabled(False)
        self.manage_groups_add_to_set_button = QPushButton("Add to Set")
        self.manage_groups_add_to_set_button.setEnabled(False)
        self.manage_groups_delete_group_button = QPushButton("Delete Group(s)")
        self.manage_groups_delete_group_button.setEnabled(False)
        self.manage_groups_exit_button = QPushButton("Exit")

        self.manage_groups_button_layout = QHBoxLayout()
        self.manage_groups_button_layout.addWidget(self.manage_groups_create_new_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_view_smiles_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_add_to_set_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_delete_group_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_exit_button)
        
        self.manage_groups_layout = QVBoxLayout()
        self.manage_groups_layout.addWidget(self.manage_groups_table)
        self.manage_groups_layout.addLayout(self.manage_groups_button_layout)
        self.manage_groups_tab.setLayout(self.manage_groups_layout)

        self.manage_sets_exit_button = QPushButton("Exit")

        self.manage_sets_layout = QVBoxLayout()
        self.manage_sets_layout.addWidget(self.manage_sets_exit_button, 0, Qt.AlignRight)
        self.manage_sets_tab.setLayout(self.manage_sets_layout)

        self.tab_widget_layout = QVBoxLayout()
        self.tab_widget_layout.addWidget(self.tabs)
        self.setLayout(self.tab_widget_layout)

        self.submit_smiles_button.clicked.connect(self.get_r_groups)
        self.generate_csv_button.clicked.connect(self.generate_csv_file)

        self.manage_groups_table.clicked.connect(self.enable_manage_groups_buttons)
        self.manage_groups_create_new_button.clicked.connect(self.open_new_group_dialog)

    def initialise_new_smiles_generator(self):
        self.smiles_generator = SmilesGenerator(self.enter_smiles_line_edit.text())
        self.r_group_substituents = {}
        self.r_group_select_buttons = {}
        self.r_group_rows = {}
        self.r_group_select_buttons = {}
        self.r_group_rows = {}

    def get_r_groups(self):
        self.initialise_new_smiles_generator()
        r_groups = sorted(self.smiles_generator.r_groups)
        row = 1
        for r_group in r_groups:
            self.r_group_rows[r_group] = row
            self.r_group_select_buttons[r_group] = QPushButton("Select")
            self.r_group_select_buttons[r_group].clicked.connect(lambda _, r=r_group: self.open_selection_dialog(r_group =r))
            self.r_groups_layout.addWidget(QLabel(r_group),row,0)
            self.r_groups_layout.addWidget(self.r_group_select_buttons[r_group],row,2)
            row += 1
            
    def open_selection_dialog(self, r_group):
        select_subs_dialog = SelectSubsDialog(r_group, self.fg_sets_dict)
        select_subs_dialog.exec_()
        if select_subs_dialog.substituents:
            self.r_group_substituents[r_group] = select_subs_dialog.substituents
            substituents_label = ", ".join(self.r_group_substituents[r_group])
            self.r_groups_layout.addWidget(QLabel(substituents_label, wordWrap = True),self.r_group_rows[r_group],1)
        if select_subs_dialog.new_set_saved:
            self.load_functional_group_sets()
        if len(self.r_group_substituents) == len(self.smiles_generator.r_groups):
            self.generate_csv_button.setEnabled(True)    

    def get_r_group_smiles(self):
        self.r_group_smiles = {}
        for r_group in self.smiles_generator.r_groups:
            if r_group == self.smiles_generator.r_groups[0]:
                smiles = [self.fg_dict[group][1] if len(self.fg_dict[group]) == 2 else self.fg_dict[group][0] for group in self.r_group_substituents[r_group]]
            else:
                smiles = [self.fg_dict[group][0] for group in self.r_group_substituents[r_group]]
            self.r_group_smiles[r_group] = smiles

    def generate_csv_file(self):
        self.get_r_group_smiles()
        self.smiles_generator.generate_substitutions_list(self.r_group_smiles)
        output = self.smiles_generator.generate_output_list()
        filename = "analogue_generator_"+str(datetime.now())[:-7].replace(" ", "_").replace(":", "")+".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(output)
        csvfile.close()

    def load_functional_groups(self):
        fg_in = open("fg_dict.pickle", "rb")
        self.fg_dict = pickle.load(fg_in)
        fg_in.close()

    def load_functional_group_sets(self):  
        fg_sets_in = open("fg_sets_dict.pickle", "rb")
        self.fg_sets_dict = pickle.load(fg_sets_in)
        fg_sets_in.close()

    def enable_manage_groups_buttons(self):
        self.manage_groups_view_smiles_button.setEnabled(True)
        self.manage_groups_add_to_set_button.setEnabled(True)
        self.manage_groups_delete_group_button.setEnabled(True)

    def open_new_group_dialog(self):
        new_group_dialog = NewGroupDialog(self.fg_dict, self.fg_sets_dict)
        new_group_dialog.exec_()
        if new_group_dialog.group_added:
            self.load_functional_groups()
            self.load_functional_group_sets()
            self.manage_groups_table.populate_table()
    
