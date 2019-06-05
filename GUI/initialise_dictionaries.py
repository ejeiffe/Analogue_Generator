from collections import OrderedDict

functional_groups = {'H': ('[H]',), 'Me': ('C',), 'Et': ('CC',), 'n-Pr': ('CCC',), 'i-Pr': ('C(C)(C)',), 'n-Bu': ('CCCC',), 'sec-Bu': ('C(C)(CC)',), 'i-Bu': ('CC(C)C',), 't-Bu': ('C(C)(C)(C)',),
                    'OH': ('O',), 'OMe': ('O(C)',), 'OEt': ('O(CC)',),
                    'NH2': ('N',), 'NHMe': ('N(C)',), 'N(Me)2': ('N(C)C',),
                    'F': ('F',), 'Cl': ('Cl',), 'Br': ('Br',), 'I': ('I',),
                    'CF3': ('C(F)(F)(F)',), 'NO2': ('[N+](=O)([O-])',), 'CN': ('[CN]',),
                    'CHO': ('C(=O)',), 'COMe': ('C(=O)(C)',), 'COOH': ('C(=O)(O)',), 'COOMe': ('C(=O)(OC)',), 'CONH2': ('C(=O)(N)',), 'CONHMe': ('C(=O)(NC)',), 'CON(Me)2': ('C(=O)(N(C)C)',),
                    'SO2NH2': ('S(=O)(=O)(N)',), 'SO2NHMe': ('S(=O)(=O)(NC)',), 'SO2N(Me)2': ('S(=O)(=O)(N(C)C)',),
                    '-C-': ('C',), '-N-': ('N',), '-O-': ('O',), '-S-': ('S',), '-C=O-': ('C(=O)',), '-NMe-': ('N(C)',),
                    '-CH2-': ('C',), '-CH2CH2-': ('CC',), '-CH2CH2CH2-': ('CCC',), '-CH2CH2CH2CH2-': ('CCCC',),
                    '-CONH-': ('C(=O)N',), '-NHCO-': ('NC(=O)',), '-COO-': ('C(=O)O',), '-OCO-': ('OC(=O)',), '-SO2NH-': ('S(=O)(=O)N',), '-NHSO2-': ('NS(=O)(=O)',),
                    'Cyclohexyl': ('C%10CCCCC%10',), 'Cyclopentyl': ('C%10CCCC%10',), 'Cyclobutyl': ('C%10CCC%10',), 'Cyclopropyl': ('C%10CC%10',),
                    'N-Piperidine': ('N%10CCCCC%10','C%10CCCCN%10'), 'N-(4H-Piperazine)': ('N%10CCNCC%10','C%10CNCCN%10'), 'N-(4-Me-Piperazine)': ('N%10CCN(C)CC%10','C%10CN(C)CCN%10'),
                    'N-Morpholine': ('N%10CCOCC%10','C%10COCCN%10'), 'N-Pyrrolidine': ('N%10CCCC%10','C%10CCCN%10'),
                    'Ph': ('C%10=CC=CC=C%10',), 'Bn': ('C(C%10=CC=CC=C%10)',), 
                    '1-Naphthyl': ('C%10=C%20C(C=CC=C%20)=CC=C%10', 'C%10=CC=C%20C(C=CC=C%20)=C%10'), '2-Naphthyl': ('C%10=CC=C%20C(C=CC=C%20)=C%10','C%10=C%20C(C=CC=C%20)=CC=C%10'),
                    '-o-Ph-': ('C%10=CC=CC=C%10',), '-m-Ph-': ('C%10=CC=CC(=C%10)',), '-p-Ph-': ('C%10=CC=C(C=C%10)',),
                    '2-Pyridine': ('C%10=NC=CC=C%10', 'C%10=CC=CN=C%10'), '3-Pyridine': ('C%10=CN=CC=C%10', 'C%10=CC=NC=C%10'), '4-Pyridine': ('C%10=CC=NC=C%10','C%10=CN=CC=C%10'),
                    '3-Pyridazine': ('C%10=NN=CC=C%10', 'C%10=CC=NN=C%10'), '4-Pyridazine': ('C%10=CN=NC=C%10', 'C%10=CN=NC=C%10'),
                    '2-Pyrimidine': ('C%10=NC=CC=N%10', 'N%10=CC=CN=C%10'), '4-Pyrimidine': ('C%10=NC=NC=C%10', 'C%10=CN=CN=C%10'), '5-Pyrimidine': ('C%10=CN=CN=C%10', 'C%10=NC=NC=C%10'),
                    'Pyrazine': ('C%10=NC=CN=C%10',),
                    'N-Pyrrole': ('N%10C=CC=C%10', 'C%10=CC=CN%10'), '2-Pyrrole': ('C%10=CC=CN%10', 'N%10C=CC=C%10'), '3-Pyrrole': ('C%10=CNC=C%10',),
                    '2-(N-Me-Pyrrole)': ('C%10=CC=CN(C)%10', 'N(C)%10C=CC=C%10'), '3-(N-Me-Pyrrole)': ('C%10=CN(C)C=C%10',), 
                    '2-Furan': ('C%10=CC=CO%10', 'O%10C=CC=C%10'), '3-Furan': ('C%10=COC=C%10',), '2-Thiophene': ('C%10=CC=CS%10', 'S%10C=CC=C%10'), '3-Thiophene': ('C%10=CSC=C%10',),
                    'N-Imidazole': ('N%10C=NC=C%10', 'C%10=CN=CN%10'),'2-(1H-Imidazole)':('C%10=NC=CN%10', 'N%10C=CN=C%10'),
                    '4-(1H-Imidazole)': ('C%10=CNC=N%10', 'N%10=CNC=C%10'), '5-(1H-Imidazole)': ('C%10=CN=CN%10', 'N%10C=NC=C%10'), 
                    '2-(N-Me-Imidazole)':('C%10=NC=CN(C)%10','N(C)%10C=CN=C%10'),'4-(N-Me-Imidazole)': ('C%10=CN(C)C=N%10', 'N%10=CN(C)C=C%10'), 
                    '5-(N-Me-Imidazole)': ('C%10=CN=CN(C)%10', 'N(C)%10C=NC=C%10'),
                    '2-Oxazole':('C%10=NC=CO%10', 'O%10C=CN=C%10'),'4-Oxazole': ('C%10=COC=N%10', 'N%10=COC=C%10'), '5-Oxazole': ('C%10=CN=CO%10', 'O%10C=NC=C%10'),
                    '2-Thiazole':('C%10=NC=CS%10', 'S%10C=CN=C%10'),'4-Thiazole': ('C%10=CSC=N%10', 'N%10=CSC=C%10'), '5-Thiazole': ('C%10=CN=CS%10', 'S%10C=NC=C%10'),
                    'N-Pyrazole': ('N%10N=CC=C%10', 'C%10=CC=NN%10'), '3-(1H-Pyrazole)': ('C%10=NNC=C%10','C%10=CNN=C%10'), '4-(1H-Pyrazole)': ('C%10=CNN=C%10','C%10=NNC=C%10'), '5-(1H-Pyrazole)': ('C%10=CC=NN%10', 'N%10N=CC=C%10'),
                    '3-(N-Me-Pyrazole)': ('C%10=NN(C)C=C%10','C%10=CN(C)N=C%10'), '4-(N-Me-Pyrazole)': ('C%10=CN(C)N=C%10','C%10=NN(C)C=C%10'), '5-(N-Me-Pyrazole)': ('C%10=CC=NN(C)%10', 'N(C)%10N=CC=C%10'),
                    '3-Isoxazole': ('C%10=NOC=C%10','C%10=CON=C%10'), '4-Isoxazole': ('C%10=CON=C%10','C%10=NOC=C%10'), '5-Isoxazole': ('C%10=CC=NO%10', 'O%10N=CC=C%10'),
                    '3-Isothiazole': ('C%10=NSC=C%10','C%10=CSN=C%10'), '4-Isothiazole': ('C%10=CSN=C%10','C%10=NSC=C%10'), '5-Isothiazole': ('C%10=CC=NS%10', 'S%10N=CC=C%10'),
                    '2-Quinoline': ('C%10=CC=C%20C(C=CC=C%20)=N%10','N%10=C%20C(C=CC=C%20)=CC=C%10'), '3-Quinoline': ('C%10=CN=C%20C(C=CC=C%20)=C%10','C%10=C%20C(C=CC=C%20)=NC=C%10'), 
                    '4-Quinoline': ('C%10=C%20C(C=CC=C%20)=NC=C%10', 'C%10=CN=C%20C(C=CC=C%20)=C%10'), '5-Quinoline': ('C%10=C%20C(N=CC=C%20)=CC=C%10', 'C%10=CC=C%20C(C=CC=N%20)=C%10'), 
                    '6-Quinoline': ('C%10=CC=C%20C(C=CC=N%20)=C%10','C%10=C%20C(N=CC=C%20)=CC=C%10'), '7-Quinoline': ('C%10=CC=C%20C(N=CC=C%20)=C%10','C%10=C%20C(C=CC=N%20)=CC=C%10'), '8-Quinoline': ('C%10=C%20C(C=CC=N%20)=CC=C%10', 'C%10=CC=C%20C(N=CC=C%20)=C%10'),
                    '1-Isoquinoline': ('C%10=C%20C(C=CC=C%20)=CC=N%10', 'N%10=CC=C%20C(C=CC=C%20)=C%10'), '3-Isoquinoline': ('C%10=NC=C%20C(C=CC=C%20)=C%10','C%10=C%20C(C=CC=C%20)=CN=C%10'), 
                    '4-Isoquinoline': ('C%10=C%20C(C=CC=C%20)=CN=C%10', 'C%10=NC=C%20C(C=CC=C%20)=C%10'), '5-Isoquinoline': ('C%10=C%20C(C=NC=C%20)=CC=C%10', 'C%10=CC=C%20C(C=CN=C%20)=C%10'), 
                    '6-Isoquinoline': ('C%10=CC=C%20C(C=CN=C%20)=C%10','C%10=C%20C(C=NC=C%20)=CC=C%10'), '7-Isoquinoline': ('C%10=CC=C%20C(C=NC=C%20)=C%10','C%10=C%20C(C=CN=C%20)=CC=C%10'), '8-Isoquinoline': ('C%10=C%20C(C=CN=C%20)=CC=C%10', 'C%10=CC=C%20C(C=NC=C%20)=C%10'), 
                    'N-Indole': ('N%10C=CC%20=CC=CC=C%20%10', 'C%20%10=CC=CC=C%20C=CN%10' ), '2-Indole': ('C%10=CC%20=CC=CC=C%20N%10', 'N%10C%20=CC=CC=C%20C=C%10'), 
                    '3-Indole': ('C%10=CNC%20=CC=CC=C%20%10','C%20%10=CC=CC=C%20NC=C%10'), '4-Indole': ('C%10=C(C=CN%20)C%20=CC=C%10','C%10=CC=C%20C(C=CN%20)=C%10'), 
                    '5-Indole': ('C%10=CC=C%20C(C=CN%20)=C%10','C%10=C(C=CN%20)C%20=CC=C%10'), '6-Indole': ('C%10=CC=C(C=CN%20)C%20=C%10','C%10=C%20C(C=CN%20)=CC=C%10'), 
                    '7-Indole': ('C%10=C%20C(C=CN%20)=CC=C%10','C%10=CC=C(C=CN%20)C%20=C%10'),
                    '2-Benzofuran': ('C%10=CC%20=CC=CC=C%20O%10', 'O%10C%20=CC=CC=C%20C=C%10'), '3-Benzofuran': ('C%10=COC%20=CC=CC=C%20%10','C%20%10=CC=CC=C%20OC=C%10'), 
                    '4-Benzofuran': ('C%10=C(C=CO%20)C%20=CC=C%10','C%10=CC=C%20C(C=CO%20)=C%10'), '5-Benzofuran': ('C%10=CC=C%20C(C=CO%20)=C%10','C%10=C(C=CO%20)C%20=CC=C%10'), 
                    '6-Benzofuran': ('C%10=CC=C(C=CO%20)C%20=C%10','C%10=C%20C(C=CO%20)=CC=C%10'), '7-Benzofuran': ('C%10=C%20C(C=CO%20)=CC=C%10','C%10=CC=C(C=CO%20)C%20=C%10'),
                    'N-Indoline': ('N%10CCC%20=CC=CC=C%20%10', 'C%20%10=CC=CC=C%20CCN%10'), '2-Indoline': ('C%10CC%20=CC=CC=C%20N%10', 'N%10C%20=CC=CC=C%20CC%10'), 
                    '3-Indoline': ('C%10CNC%20=CC=CC=C%20%10','C%20%10=CC=CC=C%20NCC%10'), '4-Indoline': ('C%10=C(CCN%20)C%20=CC=C%10','C%10=CC=C%20C(CCN%20)=C%10'), 
                    '5-Indoline': ('C%10=CC=C%20C(CCN%20)=C%10','C%10=C(CCN%20)C%20=CC=C%10'), '6-Indoline': ('C%10=CC=C(CCN%20)C%20=C%10','C%10=C%20C(CCN%20)=CC=C%10'), 
                    '7-Indoline': ('C%10=C%20C(CCN%20)=CC=C%10','C%10=CC=C(CCN%20)C%20=C%10'),
                    '2-Dihydrobenzofuran': ('C%10CC%20=CC=CC=C%20O%10', 'O%10C%20=CC=CC=C%20CC%10'), '3-Dihydrobenzofuran': ('C%10COC%20=CC=CC=C%20%10','C%20%10=CC=CC=C%20OCC%10'), 
                    '4-Dihydrobenzofuran': ('C%10=C(CCO%20)C%20=CC=C%10','C%10=CC=C%20C(CCO%20)=C%10'), '5-Dihydrobenzofuran': ('C%10=CC=C%20C(CCO%20)=C%10','C%10=C(CCO%20)C%20=CC=C%10'), 
                    '6-Dihydrobenzofuran': ('C%10=CC=C(CCO%20)C%20=C%10','C%10=C%20C(CCO%20)=CC=C%10'), '7-Dihydrobenzofuran': ('C%10=C%20C(CCO%20)=CC=C%10','C%10=CC=C(CCO%20)C%20=C%10')}
                    
                    

fg_sets_dict = OrderedDict([('Hydrogen', ['H']),
                    ('Alkyl', ['Me', 'Et', 'n-Pr', 'i-Pr', 'n-Bu', 'sec-Bu', 'i-Bu', 't-Bu']),
                    ('Oxy', ['OH', 'OMe', 'OEt']),
                    ('Amino', ['NH2', 'NHMe', 'N(Me)2']),
                    ('Halo', ['F', 'Cl', 'Br', 'I']),
                    ('EWG', ['CF3', 'NO2', 'CN']),
                    ('Carbonyl', ['CHO', 'COMe', 'COOH', 'COOMe', 'CONH2', 'CONHMe', 'CON(Me)2']),
                    ('Sulphonamide', ['SO2NH2', 'SO2NHMe', 'SO2N(Me)2']),
                    ('Ring Atom/Linker', ['-C-', '-N-', '-O-', '-S-','-C=O-','-NMe-']),
                    ('Alkyl Linker', ['-CH2-', '-CH2CH2-', '-CH2CH2CH2-', '-CH2CH2CH2CH2-']),
                    ('Heteroatom Linker', ['-CONH-', '-NHCO-', '-COO-', '-OCO-', '-SO2NH-', '-NHSO2-']),
                    ('Cycloalkyl', ['Cyclohexyl', 'Cyclopentyl', 'Cyclobutyl', 'Cyclopropyl']),
                    ('Saturated N-Heterocycles', ['N-Piperidine', 'N-(4H-Piperazine)', 'N-(4-Me-Piperazine)', 'N-Morpholine', 'N-Pyrrolidine']),
                    ('Aromatic Carbocycles', ['Ph', 'Bn', '1-Naphthyl', '2-Naphthyl']),
                    ('Phenyl Linker', ['-o-Ph-', '-m-Ph-', '-p-Ph-']), 
                    ('Pyridine', ['2-Pyridine', '3-Pyridine', '4-Pyridine']),
                    ('Diazines', ['3-Pyridazine', '4-Pyridazine', '2-Pyrimidine', '4-Pyrimidine', '5-Pyrimidine', 'Pyrazine']),
                    ('Pyrrole', ['N-Pyrrole', '2-Pyrrole', '3-Pyrrole', '2-(N-Me-Pyrrole)', '3-(N-Me-Pyrrole)']),
                    ('Furan', ['2-Furan', '3-Furan']),
                    ('Thiophene', ['2-Thiophene', '3-Thiophene']),
                    ('Imidazole', ['N-Imidazole','2-(1H-Imidazole)','4-(1H-Imidazole)', '5-(1H-Imidazole)', '2-(N-Me-Imidazole)','4-(N-Me-Imidazole)', '5-(N-Me-Imidazole)']),
                    ('Oxazole', ['2-Oxazole', '4-Oxazole', '5-Oxazole']),
                    ('Thiazole', ['2-Thiazole', '4-Thiazole', '5-Thiazole']),
                    ('Pyrazole', ['N-Pyrazole', '3-(1H-Pyrazole)', '4-(1H-Pyrazole)', '5-(1H-Pyrazole)', '3-(N-Me-Pyrazole)', '4-(N-Me-Pyrazole)', '5-(N-Me-Pyrazole)']),
                    ('Isoxazole', ['3-Isoxazole', '4-Isoxazole', '5-Isoxazole']),
                    ('Isothiazole', ['3-Isothiazole', '4-Isothiazole', '5-Isothiazole']),
                    ('Quinoline', ['2-Quinoline', '3-Quinoline', '4-Quinoline', '5-Quinoline', '6-Quinoline', '7-Quinoline', '8-Quinoline']),
                    ('Isoquinoline', ['1-Isoquinoline', '3-Isoquinoline', '4-Isoquinoline', '5-Isoquinoline', '6-Isoquinoline', '7-Isoquinoline', '8-Isoquinoline']),
                    ('Indole', ['N-Indole', '2-Indole', '3-Indole', '4-Indole', '5-Indole', '6-Indole', '7-Indole' ]),
                    ('Benzofuran', ['2-Benzofuran', '3-Benzofuran', '4-Benzofuran', '5-Benzofuran', '6-Benzofuran', '7-Benzofuran']),
                    ('Indoline', ['N-Indoline', '2-Indoline', '3-Indoline', '4-Indoline', '5-Indoline', '6-Indoline', '7-Indoline']),
                    ('Dihydrobenzofuran', ['2-Dihydrobenzofuran', '3-Dihydrobenzofuran', '4-Dihydrobenzofuran', '5-Dihydrobenzofuran', '6-Dihydrobenzofuran','7-Dihydrobenzofuran'])])




