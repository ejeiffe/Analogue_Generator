import os.path
import csv
import pickle
from datetime import datetime

from smiles_generator import *

selections_list = ['Hydrogen', 'Alkyl', 'Oxy', 'Amino', 'Halo', 'EWG', 'Carbonyl', 'Custom']

def load_dictionaries():
    global functional_groups
    global selections_dict
    fg_in = open("fg_dict.pickle", "rb")
    functional_groups = pickle.load(fg_in)
    fg_in.close()
    selections_in = open("selections_dict.pickle", "rb")
    selections_dict = pickle.load(selections_in)
    selections_in.close()

def main_menu():
    print("\nMain Menu:\n")
    print("1. Generate Analogues")
    print("2. Add Custom Functional Group")
    print("0. Exit\n")

def show_functional_groups():
    print("\nAvailable functional groups:\n")
    for selection in selections_list:
        print('{0:}:'.format(selection), end=' ')
        for group in selections_dict[selection]:
            print('{0:}'.format(group), end=' ')
        print('\n')

def functional_groups_menu_first_selection():
    print("Select functional groups:\n")
    menu_item = 1
    for selection in selections_list:
        print(str(menu_item)+': '+selection)
        menu_item += 1
    print("0. All")
    print("\n")

def functional_groups_menu_additional_selection():
    print("Select functional groups:\n")
    menu_item = 1
    for selection in selections_list:
        print(str(menu_item)+': '+selection)
        menu_item += 1
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

def select_functional_groups():
    selection = []
    functional_groups_menu_first_selection()
    fg_menu_choice = menu_select(len(selections_list)+1)
    if fg_menu_choice == 0:
        for smiles in functional_groups.values():
            selection.append(smiles)
    else:
        selecting = True
        while selecting:
            groups = selections_dict[selections_list[fg_menu_choice-1]]
            for smiles in [functional_groups[group] for group in groups]:
                selection.append(smiles)
            valid = False
            while not valid: 
                select_more = input("Select more functional groups? y/n: ").lower()
                if select_more[0] in ('y', 'n'):    
                    valid = True
                    if select_more[0] == 'n':
                        selecting = False
                    else:
                        functional_groups_menu_additional_selection()
                        fg_menu_choice = menu_select(len(selections_list)+1)
                        if fg_menu_choice == 0:
                            selecting = False
                        else:
                            continue
    return selection


def get_r_group_substitutions(r_groups):
    show_functional_groups()
    r_group_substitutions = {}
    for r in sorted(r_groups):
        print(f"\nSelect substitutions for {r}:\n")
        r_group_substitutions[r] = select_functional_groups()
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
    group_smiles = input("Enter SMILES string for functional group: ")
    functional_groups[group_name] = group_smiles
    selections_dict["Custom"].append(group_name)
    save_dictionaries()

def save_dictionaries():
    fg_out = open("fg_dict.pickle","wb")
    pickle.dump(functional_groups, fg_out)
    fg_out.close()
    selections_out = open("selections_dict.pickle", "wb")
    pickle.dump(selections_dict, selections_out)
    selections_out.close()

if __name__ == "__main__":
    print("Welcome to the analogue generator!\n")
    if os.path.exists("fg_dict.pickle"):
        load_dictionaries()
        print("Functional groups loaded")
    else:
        from initialise_functional_groups import *
        print("Functional groups initialised")
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

        
        