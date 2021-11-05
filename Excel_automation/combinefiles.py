import pandas as pd

excel_files = ['./pokemon.xlsx', './pokemon_1.xlsx' ]

merge = pd.DataFrame()

for files in excel_files:
    df = pd.read_excel(file, skiprows= 1)
    merge = merge.append(df, ignore_index = True)

merge.to_excel('Merged_files.xlsx')