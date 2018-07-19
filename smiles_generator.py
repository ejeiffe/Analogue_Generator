import re

class SmilesGenerator:

    def __init__(self, input_smiles):
        self.input_smiles = input_smiles.replace('R]', 'R0]')

        self.r_groups = re.findall("(R\d)", self.input_smiles)

        self.input_split = re.split("(R\d)", self.input_smiles)
        self.input_split = [x for x in self.input_split if "R" not in x]
        self.input_split = [x[:-1] + 'Q' if x[-1] in ('[', ']') else x for x in self.input_split]
        self.input_split = ['Q' + x[1:] if x[0] == ']' else x for x in self.input_split]
        
    def generate_substitutions_list(self, r_group_substitutions):
        total_iterations = 1
    
        for r in self.r_groups:
            total_iterations *= len(r_group_substitutions[r])

        self.substitutions_list = []

        for n in range(total_iterations):
            self.substitutions_list.append([])

        sub_index = 0
        for r in self.r_groups:
            first_index = 0
            for i in range(total_iterations//len(r_group_substitutions[r])):
                for j in range(len(r_group_substitutions[r])):
                    self.substitutions_list[first_index].append(r_group_substitutions[r][j])
                    first_index += 1
            sub_index += 1

    def generate_output_list(self):
        self.output = []
        for i in range(len(self.substitutions_list)):
            new_smiles = ''
            for j in range(len(self.input_split)-1):
                new_smiles += self.input_split[j]
                new_smiles += self.substitutions_list[i][j]
            new_smiles += self.input_split[-1]
            new_smiles = new_smiles.replace('Q','')
            self.output.append([new_smiles])

