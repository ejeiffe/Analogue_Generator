import pickle

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
                    'Carbonyl': ['CHO', 'COMe', 'COOH', 'COOMe', 'COONH2', 'COONHMe', 'COON(Me)2'],
                    'Custom': []}

def initialise_functional_groups():
    fg_out = open("fg_dict.pickle","wb")
    pickle.dump(functional_groups, fg_out)
    fg_out.close()
    selections_out = open("selections_dict.pickle", "wb")
    pickle.dump(selections_dict, selections_out)
    selections_out.close()

