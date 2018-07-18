import csv
from datetime import datetime

functional_groups = {"hydrogen": 'H', 'fluoro': 'F', 'methyl': 'CH3'}

def select_functional_groups():
    pass
    #return a list selected from the dictionary

def get_r_group_substitutions(r_groups):
    r_group_substitutions = {}
    for r in r_groups:
        r_group_substitutions[r] = select_functional_groups()
    return r_group_substitutions

def generate_csv_file(output):
    filename = "analogue_generator_"+str(datetime.now())[:-7].replace(" ", "_").replace(":", "")+".csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(output)
    csvfile.close()

if __name__ == "__main__":
    print("Welcome to the analogue generator!")
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