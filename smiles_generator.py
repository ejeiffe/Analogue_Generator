import re

class SmilesGenerator:

    def __init__(self, input_smiles):
        self.input_smiles = input_smiles.replace('R]', 'R0]')

        self.r_groups = re.findall("(R\d)", self.input_smiles)

        self.input_split = re.split("(R\d)", self.input_smiles)

        
    def generate_substitutions_list(self, r_group_substitutions):
        total_iterations = 1
    
        for r in self.r_groups:
            total_iterations *= len(r_group_substitutions[r])

        self.substitutions_list = []

        for n in range(total_iterations):
            self.substitutions_list.append([])

        sub_index = 0
        for R in R_groups:
            first_index = 0
            for i in range(len(r_group_substitutions[r])):
                for j in range(total_iterations//len(r_group_substitutions[r])):
                    self.substitutions_list[first_index].append(r_group_substitutions[r][i])
                    first_index += 1
            sub_index += 1

    def generate_output_list(self):
        self.output = []
        for i in range(len(self.substitutions_list)):
            new_smiles = ''
            for j in range(len(self.input_split)-1):
                new_smiles += self.input_split[j]
                new_smiles += self.substitutions_list[i][j]
            new_smiles += split_test[-1]
            self.output.append([new_smiles])

