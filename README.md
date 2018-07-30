# Analogue_Generator

Rapidly generate a list of chemical analogues via a command line interface.

## Usage

1. Run analogue_generator.py and input a SMILES string with numbered R groups.

![Example Input](screenshots/input_smiles.png?raw=true "Example Input")

2. Choose functional groups to replace each R group. 

The program is pre-loaded with 53 functional groups; custom groups can be added by the user. Functional groups are organised into sets for quick selection (e.g. alkyl, halo, amino) or can be selected individually. The user can save custom sets for later use.

3. The program generates a csv file containing SMILES strings for the newly generated analogues. An example is below, along with the corresponding structures.

![Example Output](screenshots/output_smiles.png?raw=true "Example Output")

