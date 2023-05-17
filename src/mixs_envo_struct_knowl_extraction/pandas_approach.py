import pandas as pd
import requests

url = 'https://github.com/GenomicsStandardsConsortium/mixs/raw/main/mixs/excel/mixs_v6.xlsx'
file_path = 'mixs_v6.xlsx'

# Download the Excel file
response = requests.get(url)
with open(file_path, 'wb') as file:
    file.write(response.content)

# Open the desired sheets into pandas data frames
df_mixs = pd.read_excel(file_path, sheet_name='MIxS')
df_env_packages = pd.read_excel(file_path, sheet_name='environmental_packages')

# Use df_mixs and df_env_packages data frames for further analysis or processing

# Optionally, remove the downloaded file
# import os
# os.remove(file_path)
