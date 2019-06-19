# Analogue_Generator

Rapidly generate a list of chemical analogues via a graphical user interface built using Python 3 and PyQt5.

## Usage

1. Run analogue_generator.py and input a SMILES string with numbered R groups.

![Example Input](screenshots/input_smiles.png?raw=true "Example Input")

![Generate Analogues Tab: Input](screenshots/generate_analogues_tab_1.png?raw=true "Generate Analogues Tab: Input")

2. Choose functional groups to replace each R group. 

![Select Substituents for R Group](screenshots/select_substituents.png?raw=true "Select Substituents for R Group")

3. Add the new analogues (as SMILES strings) to a csv file. You can then add more structures with different R groups or a different SMILES input string. View file contents to see how many structures have been added to the file. 

![Generate Analogues Tab: Generate CSV File](screenshots/generate_analogues_tab_2.png?raw=true "Generate Analogues Tab: View File Contents")

4. Click "Save CSV File" to save the output file. An example of the output file is below, along with the corresponding structures.

![Example Output](screenshots/output_smiles.png?raw=true "Example Output")

5. The program is pre-loaded with over 150 functional groups. Custom groups can be added by the user from the Manage Functional Groups tab. 

![Manage Functional Groups Tab](screenshots/manage_functional_groups_tab.png?raw=true "Manage Functional Groups Tab")

6. Functional groups are organised into sets for quick selection (e.g. Alkyl, Halo, Amino). The user can save custom sets for later use. Sets can be created, edited, and reordered from the Manage Sets tab.

![Manage Sets Tab](screenshots/manage_sets_tab.png?raw=true "Manage Sets Tab")

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.