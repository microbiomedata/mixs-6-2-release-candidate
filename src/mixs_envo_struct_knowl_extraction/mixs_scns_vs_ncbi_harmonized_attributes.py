import pprint

import pandas as pd
import csv

df = pd.read_csv('../../ncbi_biosample_sql/20230705_harmonized_attribute_usage.csv', sep=',', header=0)

# read ../../20230705_harmonized_attribute_usage.csv with csv dictreader into a dictionary using harmonized_name as the key and count as the value`
# https://stackoverflow.com/questions/21572175/convert-csv-file-to-list-of-dictionaries

with open('../../ncbi_biosample_sql/20230705_harmonized_attribute_usage.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]: rows[1] for rows in reader if rows[0] != ''}  # exclude counts if the key is ''

with open('../../generated/mixs_v6.xlsx.harmonized.tsv', mode='r') as infile:
    reader = csv.DictReader(infile, delimiter="\t")
    mixs_scns = set()
    for row in reader:
        if 'Structured comment name' in row:
            mixs_scns.add(row['Structured comment name'])

mixs_scns = list(mixs_scns)
mixs_scns.sort()

ncbi_harmonized_names = list(mydict.keys())
ncbi_harmonized_names.sort()

mixs_only = list(set(mixs_scns) - set(ncbi_harmonized_names))

mixs_only.sort()
pprint.pprint(mixs_only)

print(len(mixs_scns))
print(len(mixs_only))

ncbi_only = list(set(ncbi_harmonized_names) - set(mixs_scns))
ncbi_only.sort()
pprint.pprint(ncbi_only)

print(len(ncbi_harmonized_names))
print(len(ncbi_only))
