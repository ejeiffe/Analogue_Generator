from collections import OrderedDict

functional_groups = {'H': ('[H]',), 'Me': ('C',), 'Et': ('CC',), 'n-Pr': ('CCC',), 'i-Pr': ('C(C)(C)',), 'n-Bu': ('CCCC',), 'sec-Bu': ('C(C)(CC)',), 'i-Bu': ('CC(C)C',), 't-Bu': ('C(C)(C)(C)',),
                    'OH': ('O',), 'OMe': ('O(C)',), 'OEt': ('O(CC)',),
                    'NH2': ('N',), 'NHMe': ('N(C)',), 'N(Me)2': ('N(C)C',),
                    'F': ('F',), 'Cl': ('Cl',), 'Br': ('Br',), 'I': ('I',),
                    'CF3': ('C(F)(F)(F)',), 'NO2': ('[N+](=O)([O-])',), 'CN': ('[CN]',),
                    'CHO': ('C(=O)',), 'COMe': ('C(=O)(C)',), 'COOH': ('C(=O)(O)',), 'COOMe': ('C(=O)(OC)',), 'COONH2': ('C(=O)(ON)',), 'COONHMe': ('C(=O)(ONC)',), 'COON(Me)2': ('C(=O)(ON(C)C)',),
                    'Cyclohexyl': ('C%10CCCCC%10',), 'Cyclopentyl': ('C%10CCCC%10',), 'Cyclobutyl': ('C%10CCC%10',), 'Cyclopropyl': ('C%10CC%10',),
                    'Ph': ('C%10=CC=CC=C%10',), 'Bn': ('C(C%10=CC=CC=C%10)',), '1-Naphthyl': ('C%10=C%20C(C=CC=C%20)=CC=C%10', 'C%10=CC=C%20C(C=CC=C%20)=C%10'), '2-Naphthyl': ('C%10=CC=C%20C(C=CC=C%20)=C%10','C%10=C%20C(C=CC=C%20)=CC=C%10'),
                    '2-Py': ('C%10=NC=CC=C%10', 'C%10=CC=CN=C%10'), '3-Py': ('C%10=CN=CC=C%10', 'C%10=CC=NC=C%10'), '4-Py': ('C%10=CC=NC=C%10','C%10=CN=CC=C%10'),
                    '2-Pyrrole': ('C%10=CC=CN%10', 'N%10C=CC=C%10'), '3-Pyrrole': ('C%10=CNC=C%10',), '2-Furan': ('C%10=CC=CO%10', 'O%10C=CC=C%10'), '3-Furan': ('C%10=COC=C%10',), '2-Thiophene': ('C%10=CC=CS%10', 'S%10C=CC=C%10'), '3-Thiophene': ('C%10=CSC=C%10',),
                    'N-Imidazole': ('N%10C=NC=C%10', 'C%10=CN=CN%10'),'2-(1H-Imidazole)':('C%10=NC=CN%10', 'N%10C=CN=C%10'),'4-(1H-Imidazole)': ('C%10=CNC=N%10', 'N%10=CNC=C%10'), '5-(1H-Imidazole)': ('C%10=CN=CN%10', 'N%10C=NC=C%10'), '2-(N-Me-Imidazole)':('C%10=NC=CN(C)%10','N(C)%10C=CN=C%10'),'4-(N-Me-Imidazole)': ('C%10=CN(C)C=N%10', 'N%10=CN(C)C=C%10'), '5-(N-Me-Imidazole)': ('C%10=CN=CN(C)%10', 'N(C)%10C=NC=C%10'),
                    'Sch Frag 48': ('C(C(=O)(C%10=CC=CC=C%10))',), 'Sch Frag 56': ('C%10=C(Cl)C=CC(Cl)=C%10','C%10=C(Cl)C=CC(Cl)=C%10'), 'Sch Frag 60': ('C%10=CC=C(C)C=C%10','C%10=CC(C)=CC=C%10'), 'Sch Frag 150': ('C%10=CC=C%20C(C=CC=N%20)=C%10', 'C%10=C%20C(N=CC=C%20)=CC=C%10'), 'Sch Frag 151': ('C%10=NC=C%20C(C=CC=C%20)=C%10', 'C%10=C%20C(C=CC=C%20)=CN=C%10'),
                    'Sch Frag 170': ('O(C(=O)(C%10=CC=CC=C%10))',), 'Sch Frag 259-4': ('C%20=CC=CC%10=C%20CCC%10=O', 'O=C%10CCC%20=C%10C=CC=C%20'), 'Sch Frag 259-2': ('C(C%10)C(=O)C%20=C%10C=CC=C%20','C%20=CC=CC%10=C%20C(=O)C(C%10)'),
                    'Sch Frag 325-2': ('C%10CCC%20C(C=CC=C%20)O%10','O%10C%20C(C=CC=C%20)CCC%10'), 'Sch Frag 325-3': ('C%10COC%20C(C=CC=C%20)C%10','C%10C%20C(C=CC=C%20)OCC%10'), 'Sch Frag 330-N': ('N(C%10=CC=CC=C%10C=C%20)C%20=O','C%10(=O)C=CC%20C(C=CC=C%20)N%10'), 'Sch Frag 330-6': ('C%10=CC=C%20C(C=CC(=O)N%20(C))=C%10','C%10=C%20C(N(C)C(=O)C=C%20)=CC=C%10'), 'Sch Frag 330-7': ('C%10=CC=C%20C(N(C)C(=O)C=C%20)=C%10','C%10=C%20C(C=CC(=O)N%20(C))=CC=C%10'), 
                    'Sch Frag 334-5': ('C%10=C%20C(C(=O)N(C)C=C%20)=CC=C%10','C%10=CC=C%20C(C=CN(C)C%20(=O))=C%10'), 'Sch Frag 334-N': ('N%10C=CC%20=CC=CC=C%20C%10(=O)','O=C%10C%20=CC=CC=C%20C=CN%10')}

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
                    ('Imidazole', ['N-Imidazole','2-(1H-Imidazole)','4-(1H-Imidazole)', '5-(1H-Imidazole)', '2-(N-Me-Imidazole)','4-(N-Me-Imidazole)', '5-(N-Me-Imidazole)']),
                    ('Sch Frag RHS', ['1-Naphthyl', '2-Naphthyl', 'Sch Frag 48', 'Sch Frag 56', 'Sch Frag 60','Sch Frag 150','Sch Frag 151','Sch Frag 170','Sch Frag 259-4','Sch Frag 259-2','Sch Frag 325-2','Sch Frag 325-3','Sch Frag 330-N','Sch Frag 330-6','Sch Frag 330-7','Sch Frag 334-5','Sch Frag 334-N'])])




