import openpyxl
import os

def read_excel(path, sheet_name):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]

    rows = list(sheet.values)
    headers = rows[0]
    data_rows = rows[1:]

    data = []
    for row in data_rows:
        row_dict = {headers[i]: row[i] for i in range(len(headers))}
        data.append(row_dict)

    return data

