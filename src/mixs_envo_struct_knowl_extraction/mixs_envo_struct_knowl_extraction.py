import csv
import pprint

from openpyxl import load_workbook

import requests

url = 'https://github.com/GenomicsStandardsConsortium/mixs/raw/main/mixs/excel/mixs_v6.xlsx'
file_path = 'mixs_v6.xlsx'

# Download the Excel file
response = requests.get(url)
with open(file_path, 'wb') as file:
    file.write(response.content)

# Load the Excel file
workbook = load_workbook(file_path)

# Read the "MIxS" sheet
sheet_mixs = workbook['MIxS']
headers_mixs = [cell.value for cell in sheet_mixs[1]]

data_mixs = [dict(zip(headers_mixs, [cell.value for cell in row])) for row in sheet_mixs.iter_rows(min_row=2)]

# Read the "environmental_packages" sheet
sheet_env_packages = workbook['environmental_packages']

# Optionally, close the workbook
workbook.close()

headers_env_packages = [cell.value for cell in sheet_env_packages[1]]

data_env_packages = [dict(zip(headers_env_packages, [cell.value for cell in row])) for row in
                     sheet_env_packages.iter_rows(min_row=2)]

mixs_only = list(set(headers_mixs) - set(headers_env_packages))

env_packages_only = list(set(headers_env_packages) - set(headers_mixs))

# Use data_mixs and data_env_packages for further analysis or processing

deletables = [
    " ",
    "Requirement",
    'migs_ba',
    'migs_eu'
    'migs_org',
    'migs_pl',
    'migs_vi',
    'mimag',
    'mimarks_c',
    'mimarks_s',
    'mims',
    'misag',
    'miuvig',
    None,
]

for row in data_mixs:
    if 'Occurence' in row:
        row['Occurrence'] = row.pop('Occurence')
    if 'Item (rdfs:label)' in row:
        row['Item'] = row.pop('Item (rdfs:label)')
    for d in deletables:
        if d in row:
            del row[d]

for row in data_env_packages:
    if 'Package item' in row:
        row['Item'] = row.pop('Package item')
    for d in deletables:
        if d in row:
            del row[d]

combined_sheets = data_mixs + data_env_packages

fieldnames = set()
for row in combined_sheets:
    fieldnames.update(row.keys())

fieldnames = list(fieldnames - set(deletables))
fieldnames.sort()

pprint.pprint(fieldnames)

tsv_file = 'combined_data.tsv'

with open(tsv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, delimiter='\t', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(combined_sheets)

# Optionally, remove the downloaded file
# import os
# os.remove(file_path)
