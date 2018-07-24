import csv
from datetime import datetime

from smiles_generator import *

functional_groups = {'H': '[H]', 'Me': 'C', 'Et': 'CC', 'n-Pr': 'CCC', 'i-Pr': 'C(C)(C)', 'n-Bu': 'CCCC', 'sec-Bu': 'C(C)(CC)', 'i-Bu': 'CC(C)C', 't-Bu': 'C(C)(C)(C)',
                    'OH': 'O', 'OMe': 'O(C)', 'OEt': 'O(CC)',
                    'NH2': 'N', 'NHMe': 'N(C)', 'N(Me)2': 'N(C)C',
                    'F': 'F', 'Cl': 'Cl', 'Br': 'Br', 'I': 'I',
                    'CF3': 'C(F)(F)(F)', 'NO2': '[N+](=O)([O-])', 'CN': '[CN]',
                    'CHO': 'C(=O)', 'COMe': 'C(=O)(C)', 'COOH': 'C(=O)(O)', 'COOMe': 'C(=O)(OC)', 'COONH2': 'C(=O)(ON)', 'COONHMe': 'C(=O)(ONC)', 'COON(Me)2': 'C(=O)(ON(C)C)'}

selections_dict = {'Hydrogen' : ['H'],
                    'Alkyl': ['Me', 'Et', 'n-Pr', 'i-Pr', 'n-Bu', 'sec-Bu', 'i-Bu', 't-Bu'],
                    'Oxy': ['OH', 'OMe', 'OEt'],
                    'Amino': ['NH2', 'NHMe', 'N(Me)2'],
                    'Halo': ['F', 'Cl', 'Br', 'I'],
                    'EWG': ['CF3', 'NO2', 'CN'],
                    'Carbonyl': ['CHO', 'COMe', 'COOH', 'COOMe', 'COONH2', 'COONHMe', 'COON(Me)2']}

selections_list = ['Hydrogen', 'Alkyl', 'Oxy', 'Amino', 'Halo', 'EWG', 'Carbonyl']

def show_functional_groups():
    print("Available functional groups:\n")
    for selection in selections_list:
        print('{0:}:'.format(selection), end=' ')
        for group in selections_dict[selection]:
            print('{0:}'.format(group), end=' ')
        print('\n')

def functional_groups_menu_first_selection():
    print("Select functional groups:\n")
    print("1. Hydrogen")
    print("2. Alkyl")
    print("3. Oxy")
    print("4. Amino")
    print("5. Halo")
    print("6. EWG")
    print("7. Carbonyl")
    print("0. All")
    print("\n")

def functional_groups_menu_additional_selection():
    print("Select functional groups:\n")
    print("1. Hydrogen")
    print("2. Alkyl")
    print("3. Oxy")
    print("4. Amino")
    print("5. Halo")
    print("6. EWG")
    print("7. Carbonyl")
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
    fg_menu_choice = menu_select(8)
    if fg_menu_choice == 0:
        for smiles in functional_groups.values():
            selection.append(smiles)
    else:
        selecting = True
        while selecting:
            if fg_menu_choice == 1:
                groups = selections_dict['Hydrogen']
            elif fg_menu_choice == 2:
                groups = selections_dict['Alkyl']
            elif fg_menu_choice == 3:
                groups = selections_dict['Oxy']
            elif fg_menu_choice == 4:
                groups = selections_dict['Amino']
            elif fg_menu_choice == 5:
                groups = selections_dict['Halo']
            elif fg_menu_choice == 6:
                groups = selections_dict['EWG']
            elif fg_menu_choice == 7:
                groups = selections_dict['Carbonyl']
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
                        fg_menu_choice = menu_select(8)
                        if fg_menu_choice == 0:
                            selecting = False
                        else:
                            continue
    return selection


def get_r_group_substitutions(r_groups):
    show_functional_groups()
    r_group_substitutions = {}
    for r in r_groups:
        print(f"\nSelect substitutions for {r}:\n")
        r_group_substitutions[r] = select_functional_groups()
    return r_group_substitutions

def generate_csv_file(output):
    filename = "analogue_generator_"+str(datetime.now())[:-7].replace(" ", "_").replace(":", "")+".csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(output)
    csvfile.close()

if __name__ == "__main__":
    print("Welcome to the analogue generator!\n")
    running = True
    while running:
        input_smiles = input("Enter SMILES string: ")
        smiles_generator = SmilesGenerator(input_smiles)
        smiles_generator.generate_substitutions_list(get_r_group_substitutions(smiles_generator.r_groups))
        smiles_generator.generate_output_list()
        generate_csv_file(smiles_generator.output)
        print("CSV file created.\n")
        valid = False
        while not valid: 
            run_again = input("Generate analogues from another SMILES string? y/n: ").lower()
            if run_again[0] in ('y', 'n'):    
                valid = True
                if run_again[0] == 'n':
                    running = False