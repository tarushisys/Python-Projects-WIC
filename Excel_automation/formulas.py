import openpyxl

excel_files = ['./pokemon.xlsx', './pokemon_1.xlsx']

for files in excel_files:
    wb = openpyxl.load_workbook(file)
    worksheet = wb["Pokemon"]
    worksheet['K26'] = 'AVERAGE(K3:K27)'
    wb.save(file)
