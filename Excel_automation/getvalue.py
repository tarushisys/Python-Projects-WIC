import openpyxl

excel_files = ['pokemon.xlsx, pokemon_1.xlsx']

values = []

for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['Pokemon']
    cell_value = worksheet['K26'].value
    values.append(cell_value)

    print(cell_value)