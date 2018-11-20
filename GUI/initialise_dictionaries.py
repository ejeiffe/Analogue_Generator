from collections import OrderedDict

# Rings are identified as %10 and %20 in functional group SMILES strings to avoid clashes with open rings in input structures.

functional_groups = {'H': ('[H]',), 'Me': ('C',), 'Et': ('CC',), 'n-Pr': ('CCC',), 'i-Pr': ('C(C)(C)',), 'n-Bu': ('CCCC',), 'sec-Bu': ('C(C)(CC)',), 'i-Bu': ('CC(C)C',), 't-Bu': ('C(C)(C)(C)',),
                    'OH': ('O',), 'OMe': ('O(C)',), 'OEt': ('O(CC)',),
                    'NH2': ('N',), 'NHMe': ('N(C)',), 'N(Me)2': ('N(C)C',),
                    'F': ('F',), 'Cl': ('Cl',), 'Br': ('Br',), 'I': ('I',),
                    'CF3': ('C(F)(F)(F)',), 'NO2': ('[N+](=O)([O-])',), 'CN': ('[CN]',),
                    'CHO': ('C(=O)',), 'COMe': ('C(=O)(C)',), 'COOH': ('C(=O)(O)',), 'COOMe': ('C(=O)(OC)',), 'CONH2': ('C(=O)(N)',), 'CONHMe': ('C(=O)(NC)',), 'CON(Me)2': ('C(=O)(N(C)C)',),
                    'SO2NH2': ('S(=O)(=O)(N)',), 'SO2NHMe': ('S(=O)(=O)(NC)',), 'SO2N(Me)2': ('S(=O)(=O)(N(C)C)',),
                    'Cyclohexyl': ('C%10CCCCC%10',), 'Cyclopentyl': ('C%10CCCC%10',), 'Cyclobutyl': ('C%10CCC%10',), 'Cyclopropyl': ('C%10CC%10',),
                    'Ph': ('C%10=CC=CC=C%10',), 'Bn': ('C(C%10=CC=CC=C%10)',), 
                    '1-Naphthyl': ('C%10=C%20C(C=CC=C%20)=CC=C%10', 'C%10=CC=C%20C(C=CC=C%20)=C%10'), '2-Naphthyl': ('C%10=CC=C%20C(C=CC=C%20)=C%10','C%10=C%20C(C=CC=C%20)=CC=C%10'),
                    '2-Py': ('C%10=NC=CC=C%10', 'C%10=CC=CN=C%10'), '3-Py': ('C%10=CN=CC=C%10', 'C%10=CC=NC=C%10'), '4-Py': ('C%10=CC=NC=C%10','C%10=CN=CC=C%10'),
                    '2-Pyrrole': ('C%10=CC=CN%10', 'N%10C=CC=C%10'), '3-Pyrrole': ('C%10=CNC=C%10',), '2-Furan': ('C%10=CC=CO%10', 'O%10C=CC=C%10'), 
                    '3-Furan': ('C%10=COC=C%10',), '2-Thiophene': ('C%10=CC=CS%10', 'S%10C=CC=C%10'), '3-Thiophene': ('C%10=CSC=C%10',),
                    'N-Imidazole': ('N%10C=NC=C%10', 'C%10=CN=CN%10'),'2-(1H-Imidazole)':('C%10=NC=CN%10', 'N%10C=CN=C%10'),
                    '4-(1H-Imidazole)': ('C%10=CNC=N%10', 'N%10=CNC=C%10'), '5-(1H-Imidazole)': ('C%10=CN=CN%10', 'N%10C=NC=C%10'), 
                    '2-(N-Me-Imidazole)':('C%10=NC=CN(C)%10','N(C)%10C=CN=C%10'),'4-(N-Me-Imidazole)': ('C%10=CN(C)C=N%10', 'N%10=CN(C)C=C%10'), 
                    '5-(N-Me-Imidazole)': ('C%10=CN=CN(C)%10', 'N(C)%10C=NC=C%10'),
                    'N-Indole': ('N%10C=CC%20=CC=CC=C%20%10', 'C%20%10=CC=CC=C%20C=CN%10' ), '2-Indole': ('C%10=CC%20=CC=CC=C%20N%10', 'N%10C%20=CC=CC=C%20C=C%10'), 
                    '3-Indole': ('C%10=CNC%20=CC=CC=C%20%10','C%20%10=CC=CC=C%20NC=C%10'), '4-Indole': ('C%10=C(C=CN%20)C%20=CC=C%10','C%10=CC=C%20C(NC=C%20)=C%10'), 
                    '5-Indole': ('C%10=CC=C%20C(C=CN%20)=C%10','C%10=C(C=CN%20)C%20=CC=C%10'), '6-Indole': ('C%10=CC=C(C=CN%20)C%20=C%10','C%10=C%20C(C=CN%20)=CC=C%10'), 
                    '7-Indole': ('C%10=C%20C(C=CN%20)=CC=C%10','C%10=CC=C(C=CN%20)C%20=C%10'),
                    'N-Indoline': ('N%10CCC%20=CC=CC=C%20%10', 'C%20%10=CC=CC=C%20CCN%10'), '2-Indoline': ('C%10CC%20=CC=CC=C%20N%10', 'N%10C%20=CC=CC=C%20CC%10'), 
                    '3-Indoline': ('C%10CNC%20=CC=CC=C%20%10','C%20%10=CC=CC=C%20NCC%10'), '4-Indoline': ('C%10=C(CCN%20)C%20=CC=C%10','C%10=CC=C%20C(NCC%20)=C%10'), 
                    '5-Indoline': ('C%10=CC=C%20C(CCN%20)=C%10','C%10=C(CCN%20)C%20=CC=C%10'), '6-Indoline': ('C%10=CC=C(CCN%20)C%20=C%10','C%10=C%20C(CCN%20)=CC=C%10'), 
                    '7-Indoline': ('C%10=C%20C(CCN%20)=CC=C%10','C%10=CC=C(CCN%20)C%20=C%10')}
                    
fg_sets_dict = OrderedDict([('Hydrogen', ['H']),
                    ('Alkyl', ['Me', 'Et', 'n-Pr', 'i-Pr', 'n-Bu', 'sec-Bu', 'i-Bu', 't-Bu']),
                    ('Oxy', ['OH', 'OMe', 'OEt']),
                    ('Amino', ['NH2', 'NHMe', 'N(Me)2']),
                    ('Halo', ['F', 'Cl', 'Br', 'I']),
                    ('EWG', ['CF3', 'NO2', 'CN']),
                    ('Carbonyl', ['CHO', 'COMe', 'COOH', 'COOMe', 'CONH2', 'CONHMe', 'CON(Me)2']),
                    ('Sulphonamide', ['SO2NH2', 'SO2NHMe', 'SO2N(Me)2']),
                    ('Cycloalkyl', ['Cyclohexyl', 'Cyclopentyl', 'Cyclobutyl', 'Cyclopropyl']),
                    ('Aromatic', ['Ph', 'Bn', '1-Naphthyl', '2-Naphthyl']),
                    ('Pyridyl', ['2-Py', '3-Py', '4-Py']),
                    ('5-Membered Heteroaromatic', ['2-Pyrrole', '3-Pyrrole', '2-Furan', '3-Furan', '2-Thiophene', '3-Thiophene']),
                    ('Imidazole', ['N-Imidazole','2-(1H-Imidazole)','4-(1H-Imidazole)', '5-(1H-Imidazole)', '2-(N-Me-Imidazole)','4-(N-Me-Imidazole)', '5-(N-Me-Imidazole)']),
                    ('Indole', ['N-Indole', '2-Indole', '3-Indole', '4-Indole', '5-Indole', '6-Indole', '7-Indole' ]),
                    ('Indoline', ['N-Indoline', '2-Indoline', '3-Indoline', '4-Indoline', '5-Indoline', '6-Indoline', '7-Indoline'])])




