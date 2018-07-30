import os.path
import csv
import collections
import pickle
from datetime import datetime

from smiles_generator import *

def load_functional_groups():
    global functional_groups
    fg_in = open("fg_dict.pickle", "rb")
    functional_groups = pickle.load(fg_in)
    fg_in.close()

def load_functional_group_sets():  
    global fg_sets_dict
    fg_sets_in = open("fg_sets_dict.pickle", "rb")
    fg_sets_dict = pickle.load(fg_sets_in)
    fg_sets_in.close()

def save_functional_groups():
    fg_out = open("fg_dict.pickle","wb")
    pickle.dump(functional_groups, fg_out)
    fg_out.close()

def save_functional_group_sets():
    fg_sets_out = open("fg_sets_dict.pickle", "wb")
    pickle.dump(fg_sets_dict, fg_sets_out)
    fg_sets_out.close()

def main_menu():
    print("\nMain Menu:\n")
    print("1. Generate Analogues")
    print("2. Add Custom Functional Group")
    print("0. Exit\n")

def show_functional_groups():
    print("\nAvailable functional groups:\n")
    for fg_set in fg_sets_dict:
        print('{0:}:'.format(fg_set), end=' ')
        for group in fg_sets_dict[fg_set]:
            print('{0:}'.format(group), end=' ')
        print('\n')

def functional_groups_menu_first_selection():
    print("Select functional groups:\n")
    menu_item = 1
    for fg_set in fg_sets_dict:
        print(str(menu_item)+': '+fg_set)
        menu_item += 1
    print(str(menu_item)+": Select single functional group")
    print("0. All")
    print("\n")

def functional_groups_menu_additional_selection():
    print("Select functional groups:\n")
    menu_item = 1
    for fg_set in fg_sets_dict:
        print(str(menu_item)+': '+fg_set)
        menu_item += 1
    print(str(menu_item)+": Select single functional group")
    print("0. Cancel")
    print("\n")

def menu_select(len_menu):
    valid = False
    while not valid:
        try:
            selection = int(input("Select an option: "))
            if selection in range(len_menu):
                valid = True
            else:
                print(f"Enter a number between 0 and {str(len_menu-1)}")
        except:
            print(f"Enter a number between 0 and {str(len_menu-1)}")
    return selection

def select_functional_groups(first):
    groups = []
    selection = []
    functional_groups_menu_first_selection()
    fg_menu_choice = menu_select(len(fg_sets_dict)+2)
    if fg_menu_choice == 0:
        for smiles in functional_groups.values():
            selection.append(smiles)
    else:
        selecting = True
        while selecting:
            if fg_menu_choice == (len(fg_sets_dict) + 1):
                new_groups = select_individual_groups()
            else:
                fg_set = list(fg_sets_dict.keys())[fg_menu_choice-1]
                new_groups = fg_sets_dict[fg_set]
            for group in new_groups:
                groups.append(group)
            valid = False
            while not valid: 
                select_more = input("Select more functional groups? y/n: ").lower()
                if select_more[0] in ('y', 'n'):    
                    valid = True
            if select_more[0] == 'n':
                save_selection_as_set(groups)
                selecting = False
            else:
                functional_groups_menu_additional_selection()
                fg_menu_choice = menu_select(len(fg_sets_dict)+2)
                if fg_menu_choice == 0:
                    selecting = False
                else:
                    continue
    if first:
        selection = [functional_groups[group][1] if len(functional_groups[group]) == 2 else functional_groups[group][0] for group in groups]
    else:
        selection = [functional_groups[group][0] for group in groups]
      
    return selection

def select_individual_groups():
    show_functional_groups()
    groups = []
    selecting = True
    print("Enter name of functional group or press enter to stop selecting")
    while selecting:
        group = input("Select functional group: ")
        if group in functional_groups.keys():
            groups.append(group)
        elif group == '':
            selecting = False
        else:
            print("Please choose a functional group from the available list\n")
    return groups

def save_selection_as_set(groups):
    valid = False
    while not valid: 
        save_selection = input("Save selection? y/n: ").lower()
        if save_selection[0] in ('y', 'n'):    
            valid = True
    if save_selection[0] == 'y':
        fg_set = input("Enter name for functional group set: ")
        fg_sets_dict[fg_set] = groups
        save_functional_group_sets()
        print(f"Selection saved as {fg_set}.")
    else:
        print("Selection not saved.\n")

                   
def get_r_group_substitutions(r_groups):
    show_functional_groups()
    r_group_substitutions = {}
    for r in sorted(r_groups):
        if r == r_groups[0]:
            first = True
        else:
            first = False
        print(f"\nSelect substitutions for {r}:\n")
        r_group_substitutions[r] = select_functional_groups(first)
    return r_group_substitutions

def generate_csv_file(output):
    filename = "analogue_generator_"+str(datetime.now())[:-7].replace(" ", "_").replace(":", "")+".csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output)
    csvfile.close()

def generate_analogues():
    valid = False
    while not valid:
        input_smiles = input("Enter SMILES string: ")
        try:
            smiles_generator = SmilesGenerator(input_smiles)
            valid = True
        except:
            print("Please enter a valid SMILES string, with R groups enclosed in square brackets.")
    smiles_generator.generate_substitutions_list(get_r_group_substitutions(smiles_generator.r_groups))
    smiles_generator.generate_output_list()
    generate_csv_file(smiles_generator.output)
    print("CSV file created.\n")

def run_generator_again():
    valid = False
    while not valid: 
        run_again = input("Generate analogues from another SMILES string? y/n: ").lower()
        if run_again[0] in ('y', 'n'):    
            valid = True
    if run_again[0] == 'y':
        return True
    return False

def add_custom_functional_group():
    group_name = input("Enter name of functional group: ")
    print("""\nNote that two SMILES strings should be entered for ring structures to ensure correct connectivity.\n 
        The first SMILES string will be used when the corresponding R group is at the beginning of the string, the second when the R group is in the middle (on a branch) or at the end.\n""")
    valid = False
    while not valid: 
        two_smiles = input("Enter two SMILES strings? y/n: ").lower()
        if two_smiles[0] in ('y', 'n'):    
            valid = True
    if two_smiles[0] == 'y':
        group_smiles_first = input("Enter SMILES string for functional group (beginning of string): ")
        group_smiles_else = input("Enter SMILES string for functional group (middle/end of string): ")
        functional_groups[group_name] = (group_smiles_else, group_smiles_first)
    else:
        group_smiles = input("Enter SMILES string for functional group: ")
        functional_groups[group_name] = (group_smiles,)
    save_functional_groups()
    fg_set = add_functional_group_to_set()
    fg_sets_dict[fg_set].append(group_name)
    save_functional_group_sets()

def add_to_set_menu():
    print("\nAdd functional group to set: ")
    menu_item = 1
    for fg_set in fg_sets_dict:
        print(str(menu_item)+': '+fg_set)
        menu_item += 1
    print("0. Create New Set\n")

def add_functional_group_to_set():
    add_to_set_menu()
    add_set_menu_choice = menu_select(len(fg_sets_dict)+1)
    if add_set_menu_choice == 0:
        fg_set = input("Enter name for new functional group set: ")
        fg_sets_dict[fg_set] = []
    else:
        fg_set = list(fg_sets_dict.keys())[add_set_menu_choice-1]
    return fg_set


if __name__ == "__main__":
    print("\nWelcome to the analogue generator!")
    if os.path.exists("fg_dict.pickle"):
        load_functional_groups()
    else:
        from initialise_dictionaries import functional_groups
    if os.path.exists("fg_sets_dict.pickle"):
        load_functional_group_sets()
    else:
        from initialise_dictionaries import fg_sets_dict
    running = True
    while running:
        main_menu()
        main_select = menu_select(3)
        if main_select == 1:
            generator = True
            while generator:
                generate_analogues()
                generator = run_generator_again()
        elif main_select == 2:
            add_custom_functional_group()
        else:
            running = False

        
        