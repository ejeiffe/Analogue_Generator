import os
import pickle

from initialise_dictionaries import *

class DictManager():

    def __init__(self):
        if os.path.exists("fg_dict.pickle"):
            self.load_functional_groups()
        else:
            self.fg_dict = functional_groups
        if os.path.exists("fg_sets_dict.pickle"):
            self.load_functional_group_sets()
        else:
            self.fg_sets_dict = fg_sets_dict

    def load_functional_groups(self):
        fg_in = open("fg_dict.pickle", "rb")
        self.fg_dict = pickle.load(fg_in)
        fg_in.close()

    def load_functional_group_sets(self):  
        fg_sets_in = open("fg_sets_dict.pickle", "rb")
        self.fg_sets_dict = pickle.load(fg_sets_in)
        fg_sets_in.close()

    def save_functional_groups(self):
        fg_out = open("fg_dict.pickle","wb")
        pickle.dump(self.fg_dict, fg_out)
        fg_out.close()

    def save_functional_group_sets(self):
        fg_sets_out = open("fg_sets_dict.pickle", "wb")
        pickle.dump(self.fg_sets_dict, fg_sets_out)
        fg_sets_out.close()
