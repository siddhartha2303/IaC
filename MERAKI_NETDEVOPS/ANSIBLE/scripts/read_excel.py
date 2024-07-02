import openpyxl
import json
import sys

# Check if the worksheet name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 read_excel.py <worksheet_name>")
    sys.exit(1)

worksheet_name = sys.argv[1]

wb = openpyxl.load_workbook('../variables/golden_sheet.xlsx')
try:
    sheet = wb[worksheet_name]
except KeyError:
    print(f"Worksheet '{worksheet_name}' not found.")
    sys.exit(1)

data = []

header_row = sheet[1]  # Assuming the headers are in the first row

for row in sheet.iter_rows(min_row=2, values_only=True):
    item = {}
    for idx, value in enumerate(row):
        header = header_row[idx].value
        item[f"{header}"] = value
    data.append(item)

print(json.dumps(data))
