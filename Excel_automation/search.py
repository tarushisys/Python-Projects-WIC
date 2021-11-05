import pandas as pd
import numpy as np

files = ['./pokemon.xlsx', './pokemon_1.xlsx']

for file in files:
    df = pd.read_excel(files)
    name = df['Rep'].where(df['Name'] == 'Pikachu').dropna()
    print(file)
    print(name)