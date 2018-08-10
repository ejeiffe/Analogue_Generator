import pickle

from PyQt5.QtWidgets import *

from new_set_dialog import *

class AddToSetDialog(QDialog):

    def __init__(self, group_name, fg_sets_dict):
        super().__init__()
        self.group_name = group_name
        self.fg_sets_dict = fg_sets_dict

        self.setWindowTitle("Add New Group to Set")

        self.set_names = fg_sets_dict.keys()
        self.select_set_label = QLabel("Select Set")
        self.sets_combo_box = QComboBox()
        self.sets_combo_box.addItems(self.set_names)

        self.add_to_set_button = QPushButton("Add to Selected Set")
        self.new_set_button = QPushButton("Create New Set")

        self.add_to_set_button_layout = QHBoxLayout()
        self.add_to_set_button_layout.addWidget(self.add_to_set_button)
        self.add_to_set_button_layout.addWidget(self.new_set_button)
        
        self.add_to_set_layout = QVBoxLayout()
        self.add_to_set_layout.addWidget(self.select_set_label)
        self.add_to_set_layout.addWidget(self.sets_combo_box)
        self.add_to_set_layout.addLayout(self.add_to_set_button_layout)
        self.setLayout(self.add_to_set_layout)

        self.add_to_set_button.clicked.connect(self.add_to_selected_set)
        self.new_set_button.clicked.connect(self.open_new_set_dialog)

    def add_to_selected_set(self):
        set_name = self.sets_combo_box.currentText()
        self.fg_sets_dict[set_name].append(self.group_name)
        self.save_functional_group_sets()
        self.close()

    def open_new_set_dialog(self):
        new_set_dialog = NewSetDialog(self.group_name, self.fg_sets_dict)
        new_set_dialog.exec_()
        self.close()

    def save_functional_group_sets(self):
        fg_sets_out = open("fg_sets_dict.pickle", "wb")
        pickle.dump(self.fg_sets_dict, fg_sets_out)
        fg_sets_out.close()




