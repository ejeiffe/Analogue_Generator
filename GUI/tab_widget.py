import csv
from datetime import datetime
from collections import OrderedDict

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from dict_manager import *
from smiles_generator import *
from select_substituents_dialog import *
from new_group_dialog import *
from edit_group_dialog import *

class AGTabs(QWidget):

    def __init__(self):
        super().__init__()
        self.dict_manager = DictManager()

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

        self.manage_groups_instructions_label = QLabel("Ctrl + click to select multiple items. Double click to view SMILES.")
        self.manage_groups_table = SelectSubsTable()

        self.manage_groups_create_new_button = QPushButton("Create New Group")
        self.manage_groups_edit_group_button = QPushButton("Edit Group")
        self.manage_groups_edit_group_button.setEnabled(False)
        self.manage_groups_add_to_set_button = QPushButton("Add to Set")
        self.manage_groups_add_to_set_button.setEnabled(False)
        self.manage_groups_delete_group_button = QPushButton("Delete Group(s)")
        self.manage_groups_delete_group_button.setEnabled(False)
        self.manage_groups_exit_button = QPushButton("Exit")

        self.manage_groups_button_layout = QHBoxLayout()
        self.manage_groups_button_layout.addWidget(self.manage_groups_create_new_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_edit_group_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_add_to_set_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_delete_group_button)
        self.manage_groups_button_layout.addWidget(self.manage_groups_exit_button)
        
        self.manage_groups_layout = QVBoxLayout()
        self.manage_groups_layout.addWidget(self.manage_groups_instructions_label)
        self.manage_groups_layout.addWidget(self.manage_groups_table)
        self.manage_groups_layout.addLayout(self.manage_groups_button_layout)
        self.manage_groups_tab.setLayout(self.manage_groups_layout)

        self.manage_sets_list_label = QLabel("Functional Group Sets:")
        self.manage_sets_list = QListWidget()
        self.manage_sets_list.setFixedWidth(300)
        self.manage_sets_list.addItems(self.dict_manager.fg_sets_dict.keys())

        self.manage_sets_list_layout = QVBoxLayout()
        self.manage_sets_list_layout.addWidget(self.manage_sets_list_label)
        self.manage_sets_list_layout.addWidget(self.manage_sets_list)

        self.manage_sets_set_contains_label = QLabel("Set contains:")
        self.manage_sets_groups_label = QLabel()
        self.manage_sets_info_label = QLabel()
        
        self.manage_sets_save_changes_button = QPushButton("Save Changes")
        self.manage_sets_save_changes_button.setVisible(False)
        self.manage_sets_save_changes_button.setEnabled(False)
        self.manage_sets_cancel_reorder_button = QPushButton("Cancel")
        self.manage_sets_cancel_reorder_button.setVisible(False)

        self.manage_sets_reorder_button_layout = QHBoxLayout()
        self.manage_sets_reorder_button_layout.addWidget(self.manage_sets_save_changes_button)
        self.manage_sets_reorder_button_layout.addWidget(self.manage_sets_cancel_reorder_button)

        self.manage_sets_label_layout = QVBoxLayout()
        self.manage_sets_label_layout.addWidget(self.manage_sets_set_contains_label)
        self.manage_sets_label_layout.addWidget(self.manage_sets_groups_label)
        self.manage_sets_label_layout.addWidget(self.manage_sets_info_label)
        self.manage_sets_label_layout.addLayout(self.manage_sets_reorder_button_layout)

        self.manage_sets_top_layout = QHBoxLayout()
        self.manage_sets_top_layout.addLayout(self.manage_sets_list_layout)
        self.manage_sets_top_layout.addLayout(self.manage_sets_label_layout)

        self.manage_sets_create_new_button = QPushButton("Create New Set")
        self.manage_sets_edit_set_button = QPushButton("Edit Set")
        self.manage_sets_edit_set_button.setEnabled(False)
        self.manage_sets_reorder_sets_button = QPushButton("Reorder Sets")
        self.manage_sets_delete_set_button = QPushButton("Delete Set(s)")
        self.manage_sets_delete_set_button.setEnabled(False)
        self.manage_sets_exit_button = QPushButton("Exit")

        self.manage_sets_button_layout = QHBoxLayout()
        self.manage_sets_button_layout.addWidget(self.manage_sets_create_new_button)
        self.manage_sets_button_layout.addWidget(self.manage_sets_edit_set_button)
        self.manage_sets_button_layout.addWidget(self.manage_sets_reorder_sets_button)
        self.manage_sets_button_layout.addWidget(self.manage_sets_delete_set_button)
        self.manage_sets_button_layout.addWidget(self.manage_sets_exit_button)

        self.manage_sets_layout = QVBoxLayout()
        self.manage_sets_layout.addLayout(self.manage_sets_top_layout)
        self.manage_sets_layout.addLayout(self.manage_sets_button_layout)
        self.manage_sets_tab.setLayout(self.manage_sets_layout)

        self.tab_widget_layout = QVBoxLayout()
        self.tab_widget_layout.addWidget(self.tabs)
        self.setLayout(self.tab_widget_layout)

        self.submit_smiles_button.clicked.connect(self.get_r_groups)
        self.generate_csv_button.clicked.connect(self.generate_csv_file)

        self.manage_groups_table.clicked.connect(self.enable_manage_groups_buttons)
        self.manage_groups_create_new_button.clicked.connect(self.open_new_group_dialog)
        self.manage_groups_edit_group_button.clicked.connect(self.open_edit_group_dialog)
        self.manage_groups_add_to_set_button.clicked.connect(self.open_add_to_set_dialog)
        self.manage_groups_delete_group_button.clicked.connect(self.confirm_delete_group)

        self.manage_sets_list.clicked.connect(self.show_set_contents)
        self.manage_sets_list.model().rowsMoved.connect(self.enable_manage_sets_save_changes_button)
        self.manage_sets_reorder_sets_button.clicked.connect(self.reorder_sets)
        self.manage_sets_save_changes_button.clicked.connect(self.save_set_order)
        self.manage_sets_cancel_reorder_button.clicked.connect(self.exit_reorder_mode)

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
        select_subs_dialog = SelectSubsDialog(r_group)
        select_subs_dialog.exec_()
        if select_subs_dialog.substituents:
            self.r_group_substituents[r_group] = select_subs_dialog.substituents
            substituents_label = ", ".join(self.r_group_substituents[r_group])
            self.r_groups_layout.addWidget(QLabel(substituents_label, wordWrap = True),self.r_group_rows[r_group],1)
        if select_subs_dialog.new_set_saved:
            self.dict_manager.load_functional_group_sets()
        if len(self.r_group_substituents) == len(self.smiles_generator.r_groups):
            self.generate_csv_button.setEnabled(True)    

    def get_r_group_smiles(self):
        self.r_group_smiles = {}
        for r_group in self.smiles_generator.r_groups:
            if r_group == self.smiles_generator.r_groups[0]:
                smiles = [self.dict_manager.fg_dict[group][1] if len(self.dict_manager.fg_dict[group]) == 2 else self.dict_manager.fg_dict[group][0] for group in self.r_group_substituents[r_group]]
            else:
                smiles = [self.dict_manager.fg_dict[group][0] for group in self.r_group_substituents[r_group]]
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


    def enable_manage_groups_buttons(self):
        if len(self.manage_groups_table.selectedItems()) == 1:
            self.manage_groups_edit_group_button.setEnabled(True)
        else:
            self.manage_groups_edit_group_button.setEnabled(False)
        self.manage_groups_add_to_set_button.setEnabled(True)
        self.manage_groups_delete_group_button.setEnabled(True)

    def open_new_group_dialog(self):
        new_group_dialog = NewGroupDialog()
        new_group_dialog.exec_()
        if new_group_dialog.group_added:
            self.dict_manager.load_functional_groups()
            self.dict_manager.load_functional_group_sets()
            self.manage_groups_table.populate_table()

    def open_edit_group_dialog(self):
        group_name = self.manage_groups_table.currentItem().text()
        edit_group_dialog = EditGroupDialog(group_name)
        edit_group_dialog.exec_()
        if edit_group_dialog.group_changed:
            self.dict_manager.load_functional_groups()

    def open_add_to_set_dialog(self):
        groups = [item.text() for item in self.manage_groups_table.selectedItems()]
        groups = list(set(groups))
        add_to_set_dialog = AddToSetDialog(groups)
        add_to_set_dialog.exec_()
        self.dict_manager.load_functional_group_sets()
        self.manage_groups_table.populate_table()

    def confirm_delete_group(self):
        confirm_delete_message = QMessageBox()
        confirm_delete_message.setWindowTitle("Delete groups")
        confirm_delete_message.setText(f"Are you sure you want to delete the selected functional groups?")
        confirm_delete_message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm = confirm_delete_message.exec_()
        if confirm == QMessageBox.Yes:
            self.delete_groups()
            self.dict_manager.save_functional_groups()
            self.dict_manager.save_functional_group_sets()
            self.manage_groups_table.clear()
            self.manage_groups_table.dict_manager.load_functional_group_sets()
            self.manage_groups_table.populate_table()
    
    def delete_groups(self):
        groups = [item.text() for item in self.manage_groups_table.selectedItems()]
        for group in groups:
            del self.dict_manager.fg_dict[group]
            for set_name in self.dict_manager.fg_sets_dict:
                if group in self.dict_manager.fg_sets_dict[set_name]:
                    self.dict_manager.fg_sets_dict[set_name].remove(group)

    def show_set_contents(self):
        current_set = self.manage_sets_list.currentItem().text()
        self.manage_sets_groups_label.setText(", ".join(self.dict_manager.fg_sets_dict[current_set]))

    def reorder_sets(self):
        self.manage_sets_info_label.setText("Click and drag set names to reorder")
        self.manage_sets_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.manage_sets_save_changes_button.setVisible(True)
        self.manage_sets_cancel_reorder_button.setVisible(True)

    def enable_manage_sets_save_changes_button(self):
        self.manage_sets_save_changes_button.setEnabled(True)

    def save_set_order(self):
        list_items = []
        for n in range(self.manage_sets_list.count()):
            list_items.append(self.manage_sets_list.item(n))
        new_set_order = [item.text() for item in list_items]
        new_fg_sets_dict = OrderedDict((set_name, self.dict_manager.fg_sets_dict[set_name]) for set_name in new_set_order)
        self.dict_manager.fg_sets_dict = new_fg_sets_dict
        self.dict_manager.save_functional_group_sets()
        self.manage_groups_table.populate_table()
        self.exit_reorder_mode()

    def exit_reorder_mode(self):
        self.manage_sets_info_label.setText("")
        self.manage_sets_list.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.manage_sets_save_changes_button.setVisible(False)
        self.manage_sets_cancel_reorder_button.setVisible(False)
