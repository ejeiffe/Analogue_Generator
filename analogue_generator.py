import csv
from datetime import datetime

from smiles_generator import *

functional_groups = {'H': '[H]', 'Me': 'CH3', 'Et': 'CH2CH3', 'n-Pr': 'CH2CH2CH3', 'i-Pr': 'C(CH3)CH3', 'n-Bu': 'CH2CH2CH2CH3', 'sec-Bu': 'CH(CH3)CH2CH3', 'i-Bu': 'CH2CH(CH3)CH3', 't-Bu': 'C(CH3)(CH3)CH3',
                    'OH': 'OH', 'OMe': 'OCH3', 'OEt': 'OCH2CH3',
                    'NH2': 'NH2', 'NHMe': 'N(H)CH3', 'N(Me)2': 'N(CH3)CH3',
                    'F': 'F', 'Cl': 'Cl', 'Br': 'Br', 'I': 'I',
                    'CF3': 'CF3', 'NO2': '[N+](=O)[O-]', 'CN': 'CN'}

def show_functional_groups():
    print("Available functional groups:")
    print(functional_groups.keys())

def functional_groups_menu_first_selection():
    print("Select functional groups:\n")
    print("1. Hydrogen")
    print("2. Alkyl")
    print("3. Oxy")
    print("4. Amino")
    print("5. Halo")
    print("6. EWG")
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
    show_functional_groups()
    selection = []
    functional_groups_menu_first_selection()
    fg_menu_choice = menu_select(7)
    if fg_menu_choice == 0:
        for smiles in functional_groups.values():
            selection.append(smiles)
    else:
        selecting = True
        while selecting:
            if fg_menu_choice == 1:
                groups = ('H')
            elif fg_menu_choice == 2:
                groups = ('Me', 'Et', 'n-Pr', 'i-Pr', 'n-Bu', 'sec-Bu', 'i-Bu', 't-Bu')
            elif fg_menu_choice == 3:
                groups = ('OH', 'OMe', 'OEt')
            elif fg_menu_choice == 4:
                groups = ('NH2', 'NHMe', 'N(Me)2')
            elif fg_menu_choice == 5:
                groups = ('F', 'Cl', 'Br', 'I')
            else:
                groups = ('CF3', 'NO2', 'CN')
            for smiles in [functional_groups[group] for group in groups]:
                selection.append(smiles)
            select_more = ""
            while not (select_more.startswith('y') or select_more.startswith('n')): 
                select_more = input("Select more functional groups? y/n:" ).lower()
                if select_more.startswith('n'):    
                    selecting = False
                else:
                    functional_groups_menu_additional_selection()
                    fg_menu_choice = menu_select(7)
                    if fg_menu_choice == 0:
                        selecting = False
                    else:
                        continue
    return selection


def get_r_group_substitutions(r_groups):
    r_group_substitutions = {}
    for r in r_groups:
        print(f"Select substitutions for {r}:\n")
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
        print("CSV file created.")
        run_again = ""
        while not (run_again.startswith('y') or run_again.startswith('n')): 
            run_again = input("Generate analogues from another SMILES string? y/n:" ).lower()
            if run_again.startswith('n'):    
                running = False