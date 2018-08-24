from collections import OrderedDict

functional_groups = {'H': ('[H]',), 'Me': ('C',), 'Et': ('CC',), 'n-Pr': ('CCC',), 'i-Pr': ('C(C)(C)',), 'n-Bu': ('CCCC',), 'sec-Bu': ('C(C)(CC)',), 'i-Bu': ('CC(C)C',), 't-Bu': ('C(C)(C)(C)',),
                    'OH': ('O',), 'OMe': ('O(C)',), 'OEt': ('O(CC)',),
                    'NH2': ('N',), 'NHMe': ('N(C)',), 'N(Me)2': ('N(C)C',),
                    'F': ('F',), 'Cl': ('Cl',), 'Br': ('Br',), 'I': ('I',),
                    'CF3': ('C(F)(F)(F)',), 'NO2': ('[N+](=O)([O-])',), 'CN': ('[CN]',),
                    'CHO': ('C(=O)',), 'COMe': ('C(=O)(C)',), 'COOH': ('C(=O)(O)',), 'COOMe': ('C(=O)(OC)',), 'COONH2': ('C(=O)(ON)',), 'COONHMe': ('C(=O)(ONC)',), 'COON(Me)2': ('C(=O)(ON(C)C)',),
                    'Cyclohexyl': ('C1CCCCC1',), 'Cyclopentyl': ('C1CCCC1',), 'Cyclobutyl': ('C1CCC1',), 'Cyclopropyl': ('C1CC1',),
                    'Ph': ('C1=CC=CC=C1',), 'Bn': ('C(C1=CC=CC=C1)',), '1-Naphthyl': ('C1=C2C(C=CC=C2)=CC=C1', 'C1=CC=C2C(C=CC=C2)=C1'), '2-Naphthyl': ('C1=CC=C2C(C=CC=C2)=C1','C1=C2C(C=CC=C2)=CC=C1'),
                    '2-Py': ('C1=NC=CC=C1', 'C1=CC=CN=C1'), '3-Py': ('C1=CN=CC=C1', 'C1=CC=NC=C1'), '4-Py': ('C1=CC=NC=C1','C1=CN=CC=C1'),
                    '2-Pyrrole': ('C1=CC=CN1', 'N1C=CC=C1'), '3-Pyrrole': ('C1=CNC=C1',), '2-Furan': ('C1=CC=CO1', 'O1C=CC=C1'), '3-Furan': ('C1=COC=C1',), '2-Thiophene': ('C1=CC=CS1', 'S1C=CC=C1'), '3-Thiophene': ('C1=CSC=C1',),
                    'N-Imidazole': ('N1C=NC=C1', 'C1=CN=CN1'),'2-(1H-Imidazole)':('C1=NC=CN1', 'N1C=CN=C1'),'4-(1H-Imidazole)': ('C1=CNC=N1', 'N1=CNC=C1'), '5-(1H-Imidazole)': ('C1=CN=CN1', 'N1C=NC=C1'), '2-(N-Me-Imidazole)':('C1=NC=CN(C)1','N(C)1C=CN=C1'),'4-(N-Me-Imidazole)': ('C1=CN(C)C=N1', 'N1=CN(C)C=C1'), '5-(N-Me-Imidazole)': ('C1=CN=CN(C)1', 'N(C)1C=NC=C1')}

fg_sets_dict = OrderedDict([('Hydrogen', ['H']),
                    ('Alkyl', ['Me', 'Et', 'n-Pr', 'i-Pr', 'n-Bu', 'sec-Bu', 'i-Bu', 't-Bu']),
                    ('Oxy', ['OH', 'OMe', 'OEt']),
                    ('Amino', ['NH2', 'NHMe', 'N(Me)2']),
                    ('Halo', ['F', 'Cl', 'Br', 'I']),
                    ('EWG', ['CF3', 'NO2', 'CN']),
                    ('Carbonyl', ['CHO', 'COMe', 'COOH', 'COOMe', 'COONH2', 'COONHMe', 'COON(Me)2']),
                    ('Cycloalkyl', ['Cyclohexyl', 'Cyclopentyl', 'Cyclobutyl', 'Cyclopropyl']),
                    ('Aromatic', ['Ph', 'Bn', '1-Naphthyl', '2-Naphthyl']),
                    ('Pyridyl', ['2-Py', '3-Py', '4-Py']),
                    ('5-Membered Heteroaromatic', ['2-Pyrrole', '3-Pyrrole', '2-Furan', '3-Furan', '2-Thiophene', '3-Thiophene']),
                    ('Imidazole', ['N-Imidazole','2-(1H-Imidazole)','4-(1H-Imidazole)', '5-(1H-Imidazole)', '2-(N-Me-Imidazole)','4-(N-Me-Imidazole)', '5-(N-Me-Imidazole)'])])




