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
from edit_set_dialog import *

class AGTabs(QWidget):

    def __init__(self):
        super().__init__()
        self.dict_manager = DictManager()
        self.smiles_generator = None

        #Widgets and layouts
        #Tabs
        self.tabs = QTabWidget()
        self.generate_analogues_tab = QWidget()
        self.manage_groups_tab = QWidget()
        self.manage_sets_tab = QWidget()
        
        self.tabs.addTab(self.generate_analogues_tab, "Generate Analogues")
        self.tabs.addTab(self.manage_groups_tab, "Manage Functional Groups")
        self.tabs.addTab(self.manage_sets_tab, "Manage Sets")
        
        #Widgets and layouts for Generate Analogues Tab
        self.enter_smiles_label = QLabel("Enter SMILES string:")
        self.enter_smiles_line_edit = QLineEdit()
        self.submit_smiles_button = QPushButton("Submit")
        self.clear_smiles_input_button = QPushButton("Clear")
        self.generate_csv_button = QPushButton("Generate CSV File")
        self.generate_csv_button.setEnabled(False)
        self.generate_analogues_exit_button = QPushButton("Exit")

        self.r_groups_box = QGroupBox()
        self.r_groups_layout = QGridLayout()
        self.r_groups_layout.setVerticalSpacing(8)
        self.r_groups_layout.addWidget(QLabel("<u>R Group</u>"),0,0)
        self.r_groups_layout.addWidget(QLabel("<u>Substituents</u>"),0,1)
        self.r_groups_layout.addWidget(QLabel(" "), 0, 2)
        self.r_groups_layout.setAlignment(Qt.AlignTop)
        self.r_groups_box.setLayout(self.r_groups_layout)

        self.generate_analogues_button_layout = QHBoxLayout()
        self.generate_analogues_button_layout.addWidget(self.generate_csv_button, 0, Qt.AlignLeft)
        self.generate_analogues_button_layout.addWidget(self.generate_analogues_exit_button, 0, Qt.AlignRight)
        
        self.generate_analogues_top_layout = QHBoxLayout()
        self.generate_analogues_top_layout.addWidget(self.enter_smiles_label)
        self.generate_analogues_top_layout.addWidget(self.enter_smiles_line_edit)
        self.generate_analogues_top_layout.addWidget(self.submit_smiles_button)
        self.generate_analogues_top_layout.addWidget(self.clear_smiles_input_button)

        self.generate_analogues_layout = QVBoxLayout()
        self.generate_analogues_layout.addLayout(self.generate_analogues_top_layout)
        self.generate_analogues_layout.addWidget(self.r_groups_box)
        self.generate_analogues_layout.addLayout(self.generate_analogues_button_layout)
        self.generate_analogues_tab.setLayout(self.generate_analogues_layout)

        #Widgets and layouts for Manage Groups Tab
        self.manage_groups_instructions_label = QLabel("Click row heading to select functional group set. Ctrl + click or Shift + click to select multiple items. Double click functional group name to view SMILES.")
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

        #Widgets and layouts for Manage Sets Tab
        self.manage_sets_list_label = QLabel("Functional Group Sets:")
        self.manage_sets_list = QListWidget()
        self.manage_sets_list.setFixedWidth(300)
        self.manage_sets_list.addItems(self.dict_manager.fg_sets_dict.keys())

        self.manage_sets_list_layout = QVBoxLayout()
        self.manage_sets_list_layout.addWidget(self.manage_sets_list_label)
        self.manage_sets_list_layout.addWidget(self.manage_sets_list)
        self.manage_sets_list_layout.setAlignment(Qt.AlignLeft)

        self.manage_sets_set_contains_label = QLabel("<u>Set contains:</u>")
        self.manage_sets_set_contains_label.setFixedWidth(500)
        self.manage_sets_groups_label = QLabel(wordWrap = True)
        
        
        
        self.manage_sets_label_box = QGroupBox()
        self.manage_sets_label_layout = QVBoxLayout()
        self.manage_sets_label_layout.addWidget(self.manage_sets_set_contains_label)
        self.manage_sets_label_layout.addWidget(self.manage_sets_groups_label)
        self.manage_sets_label_box.setLayout(self.manage_sets_label_layout)
        self.manage_sets_label_box.setMaximumHeight(150)
        
        self.manage_sets_info_label = QLabel("Click and drag set names to reorder")
        self.manage_sets_save_changes_button = QPushButton("Save Changes")
        self.manage_sets_save_changes_button.setEnabled(False)
        self.manage_sets_cancel_reorder_button = QPushButton("Cancel")

        self.manage_sets_reorder_button_layout = QHBoxLayout()
        self.manage_sets_reorder_button_layout.addWidget(self.manage_sets_save_changes_button, 0)
        self.manage_sets_reorder_button_layout.addWidget(self.manage_sets_cancel_reorder_button, 0)

        self.manage_sets_reorder_box = QGroupBox()
        self.manage_sets_reorder_layout = QVBoxLayout()
        self.manage_sets_reorder_layout.addWidget(self.manage_sets_info_label)
        self.manage_sets_reorder_layout.addLayout(self.manage_sets_reorder_button_layout)
        self.manage_sets_reorder_box.setLayout(self.manage_sets_reorder_layout)
        self.manage_sets_reorder_box.setMaximumHeight(100)
        self.manage_sets_reorder_box.setVisible(False)

        self.manage_sets_top_right_layout = QVBoxLayout()
        self.manage_sets_top_right_layout.addWidget(self.manage_sets_label_box)
        self.manage_sets_top_right_layout.addWidget(self.manage_sets_reorder_box)

        self.manage_sets_top_layout = QHBoxLayout()
        self.manage_sets_top_layout.addLayout(self.manage_sets_list_layout)
        self.manage_sets_top_layout.addLayout(self.manage_sets_top_right_layout)
        
        self.manage_sets_create_new_button = QPushButton("Create New Set")
        self.manage_sets_edit_set_button = QPushButton("Edit Set")
        self.manage_sets_edit_set_button.setEnabled(False)
        self.manage_sets_reorder_sets_button = QPushButton("Reorder Sets")
        self.manage_sets_delete_set_button = QPushButton("Delete Set")
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

        #Tab Widget layout
        self.tab_widget_layout = QVBoxLayout()
        self.tab_widget_layout.addWidget(self.tabs)
        self.setLayout(self.tab_widget_layout)

        #Connections
        #Connections for Generate Analogues Tab
        self.submit_smiles_button.clicked.connect(self.initialise_r_group_layout)
        self.clear_smiles_input_button.clicked.connect(self.clear_smiles_input)
        self.generate_csv_button.clicked.connect(self.generate_csv_file)

        #Connections for Manage Groups Tab
        self.manage_groups_table.clicked.connect(self.enable_manage_groups_buttons)
        self.manage_groups_create_new_button.clicked.connect(self.open_new_group_dialog)
        self.manage_groups_edit_group_button.clicked.connect(self.open_edit_group_dialog)
        self.manage_groups_add_to_set_button.clicked.connect(self.open_add_to_set_dialog)
        self.manage_groups_delete_group_button.clicked.connect(self.confirm_delete_group)

        #Connections for Manage Sets Tab
        self.manage_sets_list.clicked.connect(self.show_set_contents)
        self.manage_sets_list.clicked.connect(self.enable_manage_sets_buttons)
        self.manage_sets_list.model().rowsMoved.connect(self.enable_manage_sets_save_changes_button)
        self.manage_sets_create_new_button.clicked.connect(self.open_selection_dialog_new_set)
        self.manage_sets_edit_set_button.clicked.connect(self.open_edit_set_dialog)
        self.manage_sets_reorder_sets_button.clicked.connect(self.enter_reorder_mode)
        self.manage_sets_save_changes_button.clicked.connect(self.save_set_order)
        self.manage_sets_cancel_reorder_button.clicked.connect(self.exit_reorder_mode)
        self.manage_sets_delete_set_button.clicked.connect(self.confirm_delete_set)

    #Methods connected to Generate Analogues Tab      
    def initialise_smiles_generator(self):
        try:
            self.smiles_generator = SmilesGenerator(self.enter_smiles_line_edit.text())
        except:
            self.show_invalid_smiles_message()
            return False
        if self.smiles_generator:
            return True

    def get_r_groups(self):
        r_groups = self.smiles_generator.get_r_groups()
        if len(r_groups) == 0:
            self.show_invalid_smiles_message()
            return False
        else:
            self.r_group_selections = {}
            return r_groups

    def initialise_r_group_layout(self):
        if self.initialise_smiles_generator():
            r_groups = self.get_r_groups()
        if r_groups:        
            self.r_group_select_buttons = {}
            self.r_group_reorder_buttons = {}
            self.r_group_rows = {}
            row = 1
            for r_group in r_groups:
                self.r_group_rows[r_group] = row
                self.r_group_select_buttons[r_group] = QPushButton("Select")
                self.r_group_reorder_buttons[r_group] = QPushButton("Reorder")
                self.r_group_reorder_buttons[r_group].setEnabled(False)
                self.r_group_select_buttons[r_group].clicked.connect(lambda _, r=r_group: self.open_selection_dialog(r_group =r))
                self.r_groups_layout.addWidget(QLabel(r_group),row,0, Qt.AlignTop)
                self.r_groups_layout.addWidget(self.r_group_select_buttons[r_group],row,2, Qt.AlignTop)
                self.r_groups_layout.addWidget(self.r_group_reorder_buttons[r_group],row,3, Qt.AlignTop)
                row += 1

    def show_invalid_smiles_message(self):
        invalid_smiles_message = QMessageBox()
        invalid_smiles_message.setWindowTitle("Invalid SMILES string")
        invalid_smiles_message.setText("Please enter a valid SMILES string, with R groups enclosed in square brackets.")
        invalid_smiles_message.exec_()

    def clear_smiles_input(self):
        self.enter_smiles_line_edit.setText("")
        self.generate_csv_button.setEnabled(False)
        row_count = self.r_groups_layout.rowCount()
        if row_count > 1:
            for i in range(1, row_count):
                for j in range(3):
                    item = self.r_groups_layout.itemAtPosition(i,j)
                    if item:
                        widget = item.widget()
                        self.r_groups_layout.removeWidget(widget)
                        widget.deleteLater()

            
    def open_selection_dialog(self, r_group):
        select_subs_dialog = SelectSubsDialog(r_group)
        select_subs_dialog.exec_()
        if select_subs_dialog.new_set_saved:
            self.dict_manager.load_functional_group_sets()
        if select_subs_dialog.substituents:
            self.display_r_group_selections(r_group, select_subs_dialog.substituents)
            self.r_group_reorder_buttons[r_group].setEnabled(True)

    def display_r_group_selections(self, r_group, substituents):
        self.r_group_selections[r_group] = substituents
        substituents_label = ", ".join(self.r_group_selections[r_group])
        row = self.r_group_rows[r_group]
        item = self.r_groups_layout.itemAtPosition(row, 1)
        if item:
            widget = item.widget()
            self.r_groups_layout.removeWidget(widget)
            widget.deleteLater()
        self.r_groups_layout.addWidget(QLabel(substituents_label, wordWrap = True),row,1)
        if len(self.r_group_selections) == len(self.r_group_rows):
            self.generate_csv_button.setEnabled(True)   

    

    def generate_csv_file(self):
        self.smiles_generator.generate_substitutions_list(self.r_group_selections)
        output = self.smiles_generator.generate_output_list()
        filename = "analogue_generator_"+str(datetime.now())[:-7].replace(" ", "_").replace(":", "")+".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(output)
        csvfile.close()
        self.show_csv_confirm_message()

    def show_csv_confirm_message(self):
        csv_confirm_message = QMessageBox()
        csv_confirm_message.setWindowTitle(" ")
        csv_confirm_message.setText("CSV file saved.")
        csv_confirm_message.exec_()

    #Methods connected to Manage Groups Tab
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
            self.manage_groups_table.refresh_table()
            self.refresh_manage_sets_list()
            self.show_new_group_confirm_message()

    def show_new_group_confirm_message(self):
        new_group_message = QMessageBox()
        new_group_message.setWindowTitle(" ")
        new_group_message.setText("New group saved.")
        new_group_message.exec_()

    def open_edit_group_dialog(self):
        group_name = self.manage_groups_table.currentItem().text()
        edit_group_dialog = EditGroupDialog(group_name)
        edit_group_dialog.exec_()
        if edit_group_dialog.group_changed:
            self.dict_manager.load_functional_groups()
            self.manage_groups_table.refresh_table()
            self.show_save_confirm_message()

    def show_save_confirm_message(self):
        save_confirm_message = QMessageBox()
        save_confirm_message.setWindowTitle(" ")
        save_confirm_message.setText("Changes saved.")
        save_confirm_message.exec_()

    def open_add_to_set_dialog(self):
        groups = [item.text() for item in self.manage_groups_table.selectedItems()]
        groups = list(set(groups))
        add_to_set_dialog = AddToSetDialog(groups)
        add_to_set_dialog.exec_()
        self.dict_manager.load_functional_group_sets()
        self.manage_groups_table.refresh_table()
        self.refresh_manage_sets_list()
        if add_to_set_dialog.new_set_saved:
            self.show_new_set_confirm_message()
        else:
            self.show_save_confirm_message()

    def confirm_delete_group(self):
        confirm_delete_message = QMessageBox()
        confirm_delete_message.setWindowTitle("Delete groups")
        confirm_delete_message.setText(f"Are you sure you want to delete the selected functional groups?")
        confirm_delete_message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm = confirm_delete_message.exec_()
        if confirm == QMessageBox.Yes:
            groups = [item.text() for item in self.manage_groups_table.selectedItems()]
            self.delete_groups(groups)
            self.manage_groups_table.refresh_table()
    
    def delete_groups(self, groups):
        for group in groups:
            del self.dict_manager.fg_dict[group]
            for set_name in self.dict_manager.fg_sets_dict:
                if group in self.dict_manager.fg_sets_dict[set_name]:
                    self.dict_manager.fg_sets_dict[set_name].remove(group)
        self.dict_manager.save_functional_groups()
        self.dict_manager.save_functional_group_sets()
        self.show_del_group_confirm_message()

    def show_del_group_confirm_message(self):
        del_group_confirm_message = QMessageBox()
        del_group_confirm_message.setWindowTitle(" ")
        del_group_confirm_message.setText("Group(s) deleted.")
        del_group_confirm_message.exec_()

    #Methods connected to Manage Sets Tab
    def enable_manage_sets_buttons(self):
        self.manage_sets_edit_set_button.setEnabled(True)
        self.manage_sets_delete_set_button.setEnabled(True)

    def show_set_contents(self):
        current_set = self.manage_sets_list.currentItem().text()
        self.manage_sets_groups_label.setText(", ".join(self.dict_manager.fg_sets_dict[current_set]))

    def open_selection_dialog_new_set(self):
        select_subs_for_set_dialog = SelectSubsForNewSetDialog()
        select_subs_for_set_dialog.exec_()
        if select_subs_for_set_dialog.new_set_saved:
            self.dict_manager.load_functional_group_sets()
            self.refresh_manage_sets_list()
            self.manage_groups_table.refresh_table()
            self.show_new_set_confirm_message()

    def show_new_set_confirm_message(self):
        new_set_confirm_message = QMessageBox()
        new_set_confirm_message.setWindowTitle(" ")
        new_set_confirm_message.setText("New set saved.")
        new_set_confirm_message.exec_()

    def refresh_manage_sets_list(self):
        self.manage_sets_list.clear()
        self.manage_sets_list.addItems(self.dict_manager.fg_sets_dict.keys())
        self.manage_sets_groups_label.setText("")

    def open_edit_set_dialog(self):
        set_name = self.manage_sets_list.currentItem().text()
        edit_set_dialog = EditSetDialog(set_name)
        edit_set_dialog.exec_()
        if edit_set_dialog.set_changed:
            self.dict_manager.load_functional_group_sets()
            if edit_set_dialog.new_groups != edit_set_dialog.groups:
                lost_groups = []
                for group in edit_set_dialog.groups:
                    if group not in edit_set_dialog.new_groups:
                        lost_groups.append(group)
                if len(lost_groups) > 0:
                    unique_groups = []
                for group in lost_groups:
                    unique = True
                    for key in self.dict_manager.fg_sets_dict.keys():
                        if group in self.dict_manager.fg_sets_dict[key]:
                            unique = False
                            break
                    if unique:
                        unique_groups.append(group)
                if len(unique_groups) > 0:
                    self.handle_unique_groups(unique_groups)
                else:
                    self.manage_groups_table.refresh_table()
                    self.refresh_manage_sets_list()
            else:
                self.manage_groups_table.refresh_table()
                self.refresh_manage_sets_list()
            self.show_save_confirm_message()

    def enter_reorder_mode(self):
        self.manage_sets_reorder_box.setVisible(True)
        self.manage_sets_list.setDragDropMode(QAbstractItemView.InternalMove)

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
        self.manage_groups_table.refresh_table()
        self.exit_reorder_mode()
        self.show_save_confirm_message()

    def exit_reorder_mode(self):
        self.manage_sets_reorder_box.setVisible(False)
        self.manage_sets_list.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.refresh_manage_sets_list()

    def delete_set(self):
        set_name = self.manage_sets_list.currentItem().text()
        temp_dict = {key:value for (key, value) in self.dict_manager.fg_sets_dict.items()}
        unique_groups = []
        del temp_dict[set_name]
        for group in self.dict_manager.fg_sets_dict[set_name]:
            unique = True
            for key in temp_dict.keys():
                if group in temp_dict[key]:
                    unique = False
                    break
            if unique:
                unique_groups.append(group)
        del self.dict_manager.fg_sets_dict[set_name]
        self.dict_manager.save_functional_group_sets()
        if len(unique_groups) > 0:
            self.handle_unique_groups(unique_groups)
        self.show_del_set_confirm_message()

    def show_del_set_confirm_message(self):
        del_set_confirm_message = QMessageBox()
        del_set_confirm_message.setWindowTitle(" ")
        del_set_confirm_message.setText("Set deleted.")
        del_set_confirm_message.exec_()
        
    def handle_unique_groups(self, groups):
        for group in groups:        
            unique_groups_message = QMessageBox()
            unique_groups_message.setWindowTitle(f"Delete group: {group}?")
            unique_groups_message.setText("Group not included in any other set. Delete group or assign to new set.")
            unique_groups_message.setStandardButtons(QMessageBox.Discard)
            unique_groups_message.addButton("Add to set", QMessageBox.AcceptRole)
            choice = unique_groups_message.exec_()
            if choice == QMessageBox.Discard:
                self.delete_groups([group])
            else:
                add_to_set_dialog = AddToSetDialog([group])
                add_to_set_dialog.exec_()
                if add_to_set_dialog.new_set_saved:
                    self.show_new_set_confirm_message()
                else:
                    self.show_save_confirm_message()
            self.dict_manager.load_functional_group_sets()
            self.manage_groups_table.refresh_table()
            self.refresh_manage_sets_list()
            
    def confirm_delete_set(self):
        confirm_delete_message = QMessageBox()
        confirm_delete_message.setWindowTitle("Delete set")
        confirm_delete_message.setText(f"Are you sure you want to delete the selected set?")
        confirm_delete_message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm = confirm_delete_message.exec_()
        if confirm == QMessageBox.Yes:
            self.delete_set()
            self.dict_manager.save_functional_groups()
            self.dict_manager.save_functional_group_sets()
            self.manage_groups_table.refresh_table()
            self.refresh_manage_sets_list()

