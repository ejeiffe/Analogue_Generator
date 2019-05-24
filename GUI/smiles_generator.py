import re

from dict_manager import *

class SmilesGenerator:

    def __init__(self, input_smiles):
        #Ensures that all R groups are followed by a number
        self.input_smiles = input_smiles.replace('R]', 'R0]') #Ensures that every R-group has an associated number
        self._dict_manager = DictManager()
        self.initialise_r_groups()

       
    def initialise_r_groups(self):
        self._r_groups = list((re.findall("(R\d)", self.input_smiles)))
        #Marking R-group at start of string to ensure correct SMILES are selected for ring-containing substituents. 
        if self.input_smiles.startswith("[R"):
            self._r_groups[0] += "*"

    def get_r_groups(self): #Generates sorted R-group list for display by tab widget
        r_groups = list(set([r[:-1] if r[-1] == "*" else r for r in self._r_groups]))
        r_groups.sort()
        return r_groups

    def get_r_group_smiles(self, r_group_selections):
        r_group_smiles = {}
        for r_group in self._r_groups:
            if r_group not in r_group_smiles:
                if r_group[-1] == "*": #Check if R-group marked as start of molecule SMILES string
                    smiles = [self._dict_manager.fg_dict[group][1] if len(self._dict_manager.fg_dict[group]) == 2 else self._dict_manager.fg_dict[group][0] for group in r_group_selections[r_group[:-1]]]
                else:
                    smiles = [self._dict_manager.fg_dict[group][0] for group in r_group_selections[r_group]]
                r_group_smiles[r_group] = smiles
        return r_group_smiles
        
    def generate_substitutions_list(self, r_group_selections):
        r_group_smiles = self.get_r_group_smiles(r_group_selections)
        total_iterations = 1
    
        for r in self._r_groups:
            total_iterations *= len(r_group_smiles[r])

        iterations = total_iterations
           
        self._substitutions_list = []

        #Setting up list of empty lists, ready for items to be appended.
        for n in range(total_iterations):
            self._substitutions_list.append([])

        #Generating all possible combinations of R groups
        sub_index = 0
        for r in self._r_groups:
            first_index = 0
            for i in range(total_iterations//iterations):
                for j in range(len(r_group_smiles[r])):
                    for k in range(iterations//len(r_group_smiles[r])):
                        self._substitutions_list[first_index].append(r_group_smiles[r][j])
                        first_index += 1
            sub_index += 1
            iterations //= len(r_group_smiles[r])

    def prepare_input_split (self):    
        self._input_split = re.split("(R\d)", self.input_smiles)
        self._input_split = [x for x in self._input_split if "R" not in x]
        #Replacing the [] around R groups in the original SMILES with a character that can be stripped out later
        self._input_split = [x[:-1] + 'Q' if x[-1] in ('[', ']') else x for x in self._input_split]
        self._input_split = ['Q' + x[1:] if x[0] == ']' else x for x in self._input_split]
        


    def generate_output_list(self):
        self.prepare_input_split()
        output = []
        # Splices together R groups from the substitution lists with the remaining SMILES fragments from the input string
        for i in range(len(self._substitutions_list)):
            new_smiles = ''
            for j in range(len(self._input_split)-1):
                new_smiles += self._input_split[j]
                new_smiles += self._substitutions_list[i][j]
            new_smiles += self._input_split[-1]
            new_smiles = new_smiles.replace('Q','')
            output.append([new_smiles])
        return output

