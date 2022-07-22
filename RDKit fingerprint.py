# 출처: https://xinhaoli74.github.io/posts/2020/04/RDKit-Cheatsheet/

from rdkit import Chem
from rdkit.Chem import AllChem, PandasTools
import pandas as pd

data = pd.read_csv("dataset_csv.csv")
#print(data['Class'])
PandasTools.AddMoleculeColumnToFrame(data, smilesCol='SMILES')

radius = 3
nBits = 1024

data_fingerprint = [AllChem.GetMorganFingerprintAsBitVect(x, radius=radius, nBits=nBits) for x in data['ROMol']]

name = [f'Bit_{i}' for i in range(nBits)]
bits = [list(l) for l in data_fingerprint]
df_fingerprint = pd.DataFrame(bits, index=data.SMILES, columns=name)
#print(df_fingerprint.head(1))
# 여기에 class column append 하기

df_fingerprint.to_csv('dataset.csv')
