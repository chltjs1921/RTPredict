from rdkit import Chem
from rdkit.Chem import AllChem


smi_enter = input('SMILES: ')
mol = Chem.MolFromSmiles(smi_enter)
smi_standard = Chem.MolToSmiles(mol)
print(smi_standard)

