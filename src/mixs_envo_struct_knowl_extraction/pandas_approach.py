import math
import pprint
import re
from typing import List

import pandas as pd
import requests
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import Annotation, SchemaDefinition, SlotDefinition, ClassDefinition

pd.set_option('display.max_columns', None)

base_url = 'https://github.com/GenomicsStandardsConsortium/mixs/raw/main/mixs/excel/'
file_path = 'mixs_v6.xlsx'

# prior knowledge
checklists = ['migs_ba', 'migs_eu', 'migs_org', 'migs_pl', 'migs_vi', 'mimag', 'mimarks_c', 'mimarks_s', 'mims',
              'misag', 'miuvig']

scn_key = 'Structured comment name'

consensus_annotation = Annotation(tag="consensus", value="true")

file_url = base_url + file_path

global_target_schema = SchemaDefinition(name='GSC_MIxS', id='http://example.com/GSC_MIxS')

global_target_view = SchemaView(global_target_schema)


def harmonize_sheets(url: str) -> pd.DataFrame:
    # Download the Excel file
    response = requests.get(file_url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    # Open the desired sheets into pandas data frames
    df_mixs = pd.read_excel(file_path, sheet_name='MIxS')

    # List of column names to delete
    columns_to_delete = [' ']

    # Delete the columns
    df_mixs_good_cols = df_mixs.drop(columns=columns_to_delete)

    # Dictionary with column name mappings
    column_mapping = {
        'Item (rdfs:label)': 'Item',
        'Occurence': 'Occurrence',
    }

    # Rename the columns
    df_mixs_renamed = df_mixs_good_cols.rename(columns=column_mapping)

    mixs_melted = pd.melt(df_mixs_renamed, id_vars=[scn_key], var_name='key',
                          value_name='value')

    # Extract DataFrame where values are found in column X
    mixs_checklists_requirements = mixs_melted[mixs_melted['key'].isin(checklists)]
    mixs_checklists_requirements_renamed = mixs_checklists_requirements.rename(columns={"value": "Requirement"})

    # Extract DataFrame where values are not found in column X
    mixs_constants = df_mixs_renamed.drop(columns=checklists)

    mixs_by_scn_and_class = pd.merge(mixs_checklists_requirements_renamed, mixs_constants,
                                     on=[scn_key])
    mixs_by_scn_and_class_renamed = mixs_by_scn_and_class.rename(columns={"key": "class"})

    by_scn_and_class_col_list = mixs_by_scn_and_class_renamed.columns.tolist()

    df_env_packages = pd.read_excel(file_path, sheet_name='environmental_packages')

    column_mapping = {
        'Environmental package': 'class',
        'Package item': 'Item',
        # 'Section': 'differentiator',
    }

    # Rename the columns
    df_env_packages_renamed = df_env_packages.rename(columns=column_mapping)

    env_packages_renamed_col_list = df_env_packages_renamed.columns.tolist()

    applicable_col_list = list(set(by_scn_and_class_col_list).intersection(env_packages_renamed_col_list))

    df_env_packages_renamed = df_env_packages_renamed[applicable_col_list]

    # Stack DataFrames vertically
    from_gsc = pd.concat([mixs_by_scn_and_class_renamed, df_env_packages_renamed])

    return from_gsc


harmonized_sheets = harmonize_sheets(file_url)
harmonized_sheets.to_csv('harmonized_sheets.tsv', index=False, sep='\t')


def convert_to_pascal_case(string):
    words = re.findall(r'\w+', string)
    pascal_case_words = [word.capitalize() for word in words]
    return ''.join(pascal_case_words)


def instantiate_classes(df: pd.DataFrame) -> List[str]:
    # prior knowledge
    classes_list = df['class'].unique().tolist()
    classes_list.sort()

    classes_list = [convert_to_pascal_case(string) for string in classes_list]

    for class_name in classes_list:
        new_class = ClassDefinition(name=class_name)
        global_target_schema.classes[class_name] = new_class


def process_sheet(df: pd.DataFrame) -> List[str]:
    instantiate_classes(df)
    # prior knowledge
    slots_list = df[scn_key].unique().tolist()
    slots_list.sort()

    for slot in slots_list:
        process_scn(df, slot)

    return slots_list


def process_scn(df: pd.DataFrame, scn: str) -> pd.DataFrame:
    print(scn)
    scn_sheet_original = df[df[scn_key] == scn]
    scn_sheet = scn_sheet_original.copy()
    scn_sheet.drop(scn_key, axis=1, inplace=True)
    scn_sheet.dropna(axis=1, how='all', inplace=True)
    attribute_names = scn_sheet.columns.tolist()
    attribute_names.remove('class')
    for attribute_name in attribute_names:
        process_attribute(df, scn, attribute_name)


def process_attribute(df: pd.DataFrame, scn: str, attribute_name: str) -> List[str]:
    # Filter the DataFrame based on the condition
    filtered_df = df[df[scn_key] == scn]

    # Extract the unique values from the desired column
    unique_values = filtered_df[attribute_name].unique()
    unique_values = [x for x in unique_values if not pd.isna(x)]

    # for uv in unique_values:
    #     print(f"{uv} {type(uv)}")

    if len(unique_values) == 1:
        process_consensus_value(scn, attribute_name, unique_values[0])
    else:
        print("Multiple values for " + scn + " " + attribute_name + " " + str(unique_values))
        attributes_by_class = filtered_df[[scn_key, 'class', attribute_name]]
        process_contested_value(attributes_by_class)


def process_consensus_value(scn: str, attribute_name: str, value: str) -> List[str]:
    tidied_attribute_name = re.sub(r'\W+', '_', attribute_name)
    tidied_slot_name = re.sub(r'\W+', '_', scn)
    if tidied_slot_name not in global_target_schema.slots:
        # print("Adding slot: " + tidied_slot_name)
        global_target_schema.slots[tidied_slot_name] = SlotDefinition(name=tidied_slot_name)
    else:
        pass
        # print("Slot already exists: " + tidied_slot_name)
    new_annotation = Annotation(tag=tidied_attribute_name, value=value)
    global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation


def process_contested_value(attributes_by_class: pd.DataFrame) -> List[str]:
    scn = attributes_by_class[scn_key].iloc[0]
    abc = attributes_by_class.copy()
    abc.drop(scn_key, axis=1, inplace=True)

    remaining_columns = abc.columns.tolist()
    value_name = (set(remaining_columns) - set(['class'])).pop()

    class_counts = abc['class'].value_counts()
    # Filter values with count greater than 1
    duplicated_classes = class_counts[class_counts > 1].index.tolist()
    if len(duplicated_classes) > 0:
        print(f"Classes {duplicated_classes} has/have duplicate values in {value_name} for {scn}: {duplicated_classes}")
        dupe_frame = abc[abc['class'].isin(duplicated_classes)]
        dupe_frame[scn_key] = scn
        print(dupe_frame)

    # duplicated_classes = abc[abc.duplicated(subset='class', keep=False)]['class'].unique()
    # if len(duplicated_classes) > 0:
    #     print("Multiple values for " + scn + " " + str(duplicated_classes))

    # print(abc)


process_sheet(harmonized_sheets)
# print(yaml_dumper.dumps(global_target_schema))
yaml_dumper.dump(global_target_schema, 'target_schema.yaml')

# from_gsc['scn_tidied'] = from_gsc['Structured comment name'].str.replace(r'\W', '_')
#
# from_gsc_melt = pd.melt(from_gsc, id_vars=['scn_tidied', 'class'], var_name='key', value_name='value')
#
# from_gsc_melt['class_key'] = from_gsc_melt['class'] + " " + from_gsc_melt['key']
#
# from_gsc_melt['class_key'] = from_gsc_melt['class_key'].str.replace(r'[\W\s]', '_', regex=True)
#
# unique_keys = from_gsc_melt['key'].unique().tolist()
# unique_keys = [string.replace(' ', '_') for string in unique_keys]
# # print(unique_keys)
#
# # Optionally, remove the downloaded file
# # import os
# # os.remove(file_path)
#
# from_gsc_melt_list_of_dicts = from_gsc_melt.to_dict('records')
#
# slot_defs = {}
#
# for row in from_gsc_melt_list_of_dicts:
#     if pd.notna(row['value']):
#
#         checklist_match = ""
#         unique_key_match = ""
#         for checklist in checklists:
#             for unique_key in unique_keys:
#                 if checklist in row['class_key'] and unique_key in row['class_key']:
#                     checklist_match = checklist
#                     unique_key_match = unique_key
#                     # print(f"Combination: {row['class_key']}, checklist: {checklist}, unique_key: {unique_key}")
#                     break  # Exit the inner loop
#             else:
#                 continue  # Continue to the next iteration of the outer loop
#             break  # Exit the outer loop
#
#         if row['scn_tidied'] not in slot_defs:
#             slot_defs[row['scn_tidied']] = {}
#             slot_defs[row['scn_tidied']]['annotations'] = {}
#
#         class_key = row['class_key']
#         suffix = 1
#         while class_key in slot_defs[row['scn_tidied']]['annotations']:
#             class_key = f"{row['class_key']}_{suffix}"
#             suffix += 1
#
#         slot_defs[row['scn_tidied']]['annotations'][class_key] = {
#             "tag": class_key,
#             "value": row['value'],
#             "annotations": {
#                 "class": row['class'],
#                 "key": row['key'],
#             }
#         }
#
# GSC_MIxS = {
#     'name': 'GSC_MIxS',
#     'id': 'http://example.com/GSC_MIxS',
#     'slots': slot_defs
# }
#
# yaml.dump(GSC_MIxS, open('GSC_MIxS_raw.yaml', 'w'), sort_keys=False)
#
# sv = SchemaView('GSC_MIxS_raw.yaml')
#
# sv_slots = sv.all_slots()
#
# for slot_key, slot_obj in sv_slots.items():
#     slot_annotations = slot_obj.annotations
#     temp_list = []
#     for o_annotation_key, o_annotation_value in slot_annotations.items():
#         temp = {"slot": slot_key, "value": o_annotation_value.value}
#         if o_annotation_value.annotations:
#             for i_annotation_key, i_annotation_value in o_annotation_value.annotations.items():
#                 temp[i_annotation_key] = i_annotation_value.value
#                 # print(f"{i_annotation_key} = {i_annotation_value.value} for {slot_key} of {o_annotation_value.value}")
#         # pprint.pprint(temp)
#         temp_list.append(temp)
#     # pprint.pprint(temp_list)
#     temp_frame = pd.DataFrame(temp_list)
#     try:
#         temp_pivot = temp_frame.pivot(index='class', columns='key', values='value')
#         # print(temp_pivot)
#         temp_pivot_col_list = temp_pivot.columns.tolist()
#         temp_pivot_index_list = temp_pivot.index.tolist()
#         for col in temp_pivot_col_list:
#             temp_uniques = temp_pivot[col].unique().tolist()
#             temp_uniques_len = len(temp_uniques)
#             if temp_uniques_len == 1:
#                 print(f"{slot_key} only has one {col} value, {temp_uniques[0]}")
#                 # print(temp_pivot_index_list)
#                 temp_annotation = Annotation(tag=col, value=temp_uniques[0], annotations=[consensus_annotation])
#                 slot_obj.annotations[col] = temp_annotation
#                 for index in temp_pivot_index_list:
#                     # want to delete annotations like mimarks_c_Expected_value if appropriate
#                     target = f"{index} {col}"
#                     target = re.sub(r'\W+', '_', target)
#                     # print(f"Will delete {target} annotation")
#                     del slot_obj.annotations[target]
#                 # print(yaml_dumper.dumps(slot_obj))
#             else:
#                 print(f"{slot_key} has {temp_uniques_len} {col} values")
#     except ValueError:
#         print(f"Cannot pivot {slot_key} {col}")
#     print(yaml_dumper.dumps(slot_obj))
#
# # yaml_dumper.dump(sv.schema, 'GSC_MIxS_LinkML.yaml')
