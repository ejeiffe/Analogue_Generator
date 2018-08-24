# Analogue_Generator

Rapidly generate a list of chemical analogues via a graphical user interface built using PyQt5.

A simplified command line version is also available.

## Usage

1. Run analogue_generator_gui.py and input a SMILES string with numbered R groups.

![Example Input](screenshots/input_smiles.png?raw=true "Example Input")

![Generate Analogues Tab: Input](screenshots/generate_analogues_tab_1.png?raw=true "Generate Analogues Tab: Input")

2. Choose functional groups to replace each R group. 

![Select Substituents for R Group](screenshots/select_substituents.png?raw=true "Select Substituents for R Group")

3. The program generates a csv file containing SMILES strings for the newly generated analogues. An example is below, along with the corresponding structures.

![Generate Analogues Tab: Generate CSV File](screenshots/generate_analogues_tab_2.png?raw=true "Generate Analogues Tab: Generate CSV File")

![Example Output](screenshots/output_smiles.png?raw=true "Example Output")

4. The program is pre-loaded with 53 functional groups. Custom groups can be added by the user from the Manage Functional Groups tab. 

![Manage Functional Groups Tab](screenshots/manage_functional_groups_tab.png?raw=true "Manage Functional Groups Tab")

5. Functional groups are organised into sets for quick selection (e.g. Alkyl, Halo, Amino). The user can save custom sets for later use. Sets can be created, edited, and reordered from the Manage Sets tab.

![Manage Sets Tab](screenshots/manage_sets_tab.png?raw=true "Manage Sets Tab")

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.