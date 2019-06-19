from PyQt5.QtWidgets import *

class ReorderSubsDialog(QDialog):

    def __init__(self, r_group, substituents):
        super().__init__()
        self.r_group = r_group
        self.substituents = substituents
        self.subs_order_changed = False

        self.setWindowTitle(f"Substituents for {self.r_group}")

        self.reorder_subs_info_label = QLabel("Click and drag groups to reorder")
        self.reorder_subs_list = QListWidget()
        self.reorder_subs_list.addItems(self.substituents)
        self.reorder_subs_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.reorder_subs_save_changes_button = QPushButton("Save Changes")
        self.reorder_subs_save_changes_button.setEnabled(False)
        self.reorder_subs_cancel_button = QPushButton("Cancel")

        self.reorder_subs_button_layout = QHBoxLayout()
        self.reorder_subs_button_layout.addWidget(self.reorder_subs_save_changes_button)
        self.reorder_subs_button_layout.addWidget(self.reorder_subs_cancel_button)

        self.reorder_subs_layout = QVBoxLayout()
        self.reorder_subs_layout.addWidget(self.reorder_subs_info_label)
        self.reorder_subs_layout.addWidget(self.reorder_subs_list)
        self.reorder_subs_layout.addLayout(self.reorder_subs_button_layout)
        self.setLayout(self.reorder_subs_layout)

        self.reorder_subs_list.model().rowsMoved.connect(self.enable_save_changes_button)
        self.reorder_subs_save_changes_button.clicked.connect(self.save_subs_order)
        self.reorder_subs_cancel_button.clicked.connect(self.close)


    def enable_save_changes_button(self):
        self.reorder_subs_save_changes_button.setEnabled(True)

    def save_subs_order(self):
        list_items = []
        for n in range(self.reorder_subs_list.count()):
            list_items.append(self.reorder_subs_list.item(n))
        self.substituents = [item.text() for item in list_items]
        self.subs_order_changed = True
        self.close()