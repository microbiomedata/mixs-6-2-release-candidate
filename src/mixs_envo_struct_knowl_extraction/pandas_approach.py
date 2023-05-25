import math
import pprint
import re
from typing import List

import pandas as pd
import requests
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import Annotation, SchemaDefinition, SlotDefinition, ClassDefinition, Example, \
    SubsetDefinition
from linkml_runtime.linkml_model.units import UnitOfMeasure

# import unicodedata

# https://github.com/GenomicsStandardsConsortium/mixs/wiki/5.-MIxS-checklists
# section: indicates which section (should be one of: investigation, environment, mixs extension,
#   nucleic acid sequence source, sequencing) a descriptor belongs to
# "mixs extension" doesn't appear anywhere in mixs_v6.xlsx

# todo get class uris from external source

# todo create combination classes
#   checklists should be mixins

# GSC is saying that any slots from any checklist of environmental package can be combined together in any submission
#   and even that submissions with non-MIxS slots should be accepted

# todo add some string tidying? unless we also kept original strings, it might be harder to do diffs against the
#  Excel model

# todo replace non-ascii characters with whitespace or placeholder character?

# todo is everything being considered a string at this point?

# todo check for many to many slot names/ids

pd.set_option('display.max_columns', None)

debug_mode = False

non_ascii_replacement = ' '

base_url = 'https://github.com/GenomicsStandardsConsortium/mixs/raw/main/mixs/excel/'
file_path = 'mixs_v6.xlsx'

# prior knowledge
checklists = ['migs_ba', 'migs_eu', 'migs_org', 'migs_pl', 'migs_vi', 'mimag', 'mimarks_c', 'mimarks_s', 'mims',
              'misag', 'miuvig']

# prior knowledge
scn_key = 'Structured comment name'

consensus_annotation = Annotation(tag="consensus", value="true")

file_url = base_url + file_path

global_target_schema = SchemaDefinition(name='GSC_MIxS', id='http://example.com/GSC_MIxS', source=file_url, )


def harmonize_sheets(url: str) -> pd.DataFrame:
    # Download the Excel file
    response = requests.get(url)
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
    }

    # Rename the columns
    df_env_packages_renamed = df_env_packages.rename(columns=column_mapping)

    env_packages_renamed_col_list = df_env_packages_renamed.columns.tolist()

    applicable_col_list = list(set(by_scn_and_class_col_list).intersection(env_packages_renamed_col_list))

    df_env_packages_renamed = df_env_packages_renamed[applicable_col_list]

    # Stack DataFrames vertically
    from_gsc = pd.concat([mixs_by_scn_and_class_renamed, df_env_packages_renamed])

    from_gsc = from_gsc.drop_duplicates()

    return from_gsc


harmonized_sheets = harmonize_sheets(file_url)
harmonized_sheets.to_csv('harmonized_sheets.tsv', index=False, sep='\t')


def convert_to_pascal_case(string):
    words = re.findall(r'\w+', string)
    pascal_case_words = [word.capitalize() for word in words]
    return ''.join(pascal_case_words)


def remove_non_ascii(text):
    return ''.join([i if ord(i) < 128 else non_ascii_replacement for i in text])


def instantiate_classes(df: pd.DataFrame) -> None:
    # prior knowledge
    classes_list = df['class'].unique().tolist()
    classes_list.sort()

    for class_name in classes_list:
        if class_name in checklists:
            if "Checklist" not in global_target_schema.classes:
                new_super = ClassDefinition(name="Checklist")
                global_target_schema.classes["Checklist"] = new_super
            class_name = convert_to_pascal_case(class_name)
            new_class = ClassDefinition(name=class_name, is_a="Checklist")
            global_target_schema.classes[class_name] = new_class
        else:
            if "EnvironmentalPackage" not in global_target_schema.classes:
                new_super = ClassDefinition(name="EnvironmentalPackage")
                global_target_schema.classes["EnvironmentalPackage"] = new_super
            class_name = convert_to_pascal_case(class_name)
            new_class = ClassDefinition(name=class_name, is_a="EnvironmentalPackage")
            global_target_schema.classes[class_name] = new_class


def process_sheet(df: pd.DataFrame) -> List[str]:
    instantiate_classes(df)
    slots_list = df[scn_key].unique().tolist()
    slots_list.sort()

    for slot in slots_list:
        process_scn(df, slot)

    return slots_list


def process_scn(df: pd.DataFrame, scn: str) -> None:
    scn_sheet_original = df[df[scn_key] == scn]
    scn_sheet = scn_sheet_original.copy()
    scn_sheet.drop(scn_key, axis=1, inplace=True)
    scn_sheet.dropna(axis=1, how='all', inplace=True)
    attribute_names = scn_sheet.columns.tolist()
    attribute_names.remove('class')
    for attribute_name in attribute_names:
        process_attribute(df, scn, attribute_name)


def process_attribute(df: pd.DataFrame, scn: str, attribute_name: str) -> None:
    # Filter the DataFrame based on the condition
    filtered_df = df[df[scn_key] == scn]

    # Extract the unique values from the desired column
    unique_values = filtered_df[attribute_name].unique()
    unique_values = [x for x in unique_values if not pd.isna(x)]

    sanitized_values = []
    for value in unique_values:
        if isinstance(value, str):  # Check if the value is a string
            sanitized_value = value.strip()
            sanitized_value = sanitized_value.rstrip('.')  # Remove trailing periods
            sanitized_value = sanitized_value.strip()
            sanitized_value = remove_non_ascii(sanitized_value)
            sanitized_values.append(sanitized_value)
            # also want to collapse multiple spaces into one
        else:
            sanitized_values.append(value)

        sanitized_values = list(set(sanitized_values))

    if len(sanitized_values) == 1:
        process_consensus_value(scn, attribute_name, sanitized_values[0])
    else:
        attributes_by_class = filtered_df[[scn_key, 'class', attribute_name]]
        process_contested_value(attributes_by_class)


def process_consensus_value(scn: str, attribute_name: str, value: str) -> None:
    tidied_attribute_name = re.sub(r'\W+', '_', attribute_name)
    tidied_slot_name = re.sub(r'\W+', '_', scn)
    new_annotation = Annotation(tag=tidied_attribute_name, value=value)

    if tidied_slot_name not in global_target_schema.slots:
        global_target_schema.slots[tidied_slot_name] = SlotDefinition(name=tidied_slot_name)

    if tidied_attribute_name == "Item":
        global_target_schema.slots[tidied_slot_name].title = value
    elif tidied_attribute_name == "Definition":
        global_target_schema.slots[tidied_slot_name].description = value
    elif tidied_attribute_name == "Example":
        new_example = Example(value=value)
        global_target_schema.slots[tidied_slot_name].examples = [new_example]
    elif tidied_attribute_name == "Section":
        if value not in global_target_schema.subsets:
            global_target_schema.subsets[value] = SubsetDefinition(name=value)
        global_target_schema.slots[tidied_slot_name].in_subset = [value]
    elif tidied_attribute_name == "Occurrence":
        if value == "m":
            global_target_schema.slots[tidied_slot_name].multivalued = True
        else:
            global_target_schema.slots[tidied_slot_name].multivalued = False
    elif tidied_attribute_name == "MIXS_ID":
        global_target_schema.slots[tidied_slot_name].slot_uri = value
    elif tidied_attribute_name == "Value_syntax":
        global_target_schema.slots[tidied_slot_name].string_serialization = value
    elif tidied_attribute_name == "Requirement":
        if value == "-":
            # print(f"Slot {tidied_slot_name} has a true consensus {tidied_attribute_name} value of {value}")
            global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation
        elif value == "C":
            global_target_schema.slots[tidied_slot_name].recommended = True
            global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation
        elif value == "E":
            global_target_schema.slots[tidied_slot_name].recommended = True
            global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation
            # take some slot usage action if the class is an environmental package???
        elif value == "M":
            global_target_schema.slots[tidied_slot_name].required = True
        elif value == "X":
            global_target_schema.slots[tidied_slot_name].recommended = False
            global_target_schema.slots[tidied_slot_name].required = False
    # elif tidied_attribute_name == "Preferred_unit":
    #     # we are using the unit.symbol slot VERY LIBERALLY here
    #     # and I doubt that UOMs will show up in linkml2sheets output
    #     new_uom = UnitOfMeasure(symbol=value)
    #     global_target_schema.slots[tidied_slot_name].unit = new_uom
    else:
        global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation


# https://github.com/GenomicsStandardsConsortium/mixs/wiki/5.-MIxS-checklists
# - not applicable (-): descriptor is not applicable for a given checklist type
# C conditional mandatory (C): descriptor must be present for compliance with the checklist, but only when applicable to the study, i.e. if this item is not applicable for the study the metadata data will still be checklist compliant even if it is left out
# E environment-dependent (E): descriptor must be present depending on the environment the original sample was obtained from
# M mandatory (M): descriptor must be present for compliance with the checklist_
# X optional (X): descriptor may be present, not mandatory for compliance with checklist


def process_contested_value(attributes_by_class: pd.DataFrame) -> None:
    scn = attributes_by_class[scn_key].iloc[0]
    abc = attributes_by_class.copy()
    abc.drop(scn_key, axis=1, inplace=True)

    remaining_columns = abc.columns.tolist()
    value_name = (set(remaining_columns) - {'class'}).pop()

    class_counts = abc['class'].value_counts()

    duplicated_classes = class_counts[class_counts > 1].index.tolist()
    if len(duplicated_classes) > 0:
        dupe_frame = abc[abc['class'].isin(duplicated_classes)].copy()
        dupe_frame[scn_key] = scn
        all_values = dupe_frame[value_name].unique().tolist()
        duplication_comment = f"Classes {duplicated_classes} has/have duplicate values in {value_name} for {scn}: {all_values}"
        print(duplication_comment)
        print(dupe_frame)
        global_target_schema.comments.append(duplication_comment)
    else:
        abc_dict = abc.to_dict('records')
        for slot_usage_dict in abc_dict:
            tidied_attribute_name = re.sub(r'\W+', '_', value_name)
            tidied_slot_name = re.sub(r'\W+', '_', scn)

            current_class = convert_to_pascal_case(slot_usage_dict['class'])

            value = slot_usage_dict[value_name]

            new_annotation = Annotation(tag=tidied_attribute_name, value=value)

            if tidied_slot_name not in global_target_schema.classes[current_class].slot_usage:
                new_slot_usage = SlotDefinition(name=tidied_slot_name)
                global_target_schema.classes[current_class].slot_usage[tidied_slot_name] = new_slot_usage

            if tidied_attribute_name == "Item":
                global_target_schema.classes[current_class].slot_usage[tidied_slot_name].title = value
            elif tidied_attribute_name == "Definition":
                global_target_schema.classes[current_class].slot_usage[tidied_slot_name].description = value
            elif tidied_attribute_name == "Example":
                new_example = Example(value=value)
                global_target_schema.classes[current_class].slot_usage[tidied_slot_name].examples = [new_example]
            elif tidied_attribute_name == "Section":
                if value not in global_target_schema.subsets:
                    global_target_schema.subsets[value] = SubsetDefinition(name=value)
                global_target_schema.classes[current_class].slot_usage[tidied_slot_name].in_subset = [value]
            elif tidied_attribute_name == "Occurrence":
                if value == "m":
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].multivalued = True
                else:
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].multivalued = False
            elif tidied_attribute_name == "MIXS_ID":
                global_target_schema.classes[current_class].slot_usage[tidied_slot_name].slot_uri = value
            elif tidied_attribute_name == "Value_syntax":
                global_target_schema.classes[current_class].slot_usage[tidied_slot_name].string_serialization = value
            elif tidied_attribute_name == "Requirement":
                # TODO needs modified logic for value "-" and ("E", when the class is a environmental package)
                if value == "-":
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].annotations[
                        tidied_attribute_name] = new_annotation
                elif value == "C":
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].recommended = True
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].annotations[
                        tidied_attribute_name] = new_annotation
                elif value == "E":
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].recommended = True
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].annotations[
                        tidied_attribute_name] = new_annotation
                    # take some slot usage action if the class is an environmental package???
                elif value == "M":
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].required = True
                elif value == "X":
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].recommended = False
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].required = False
                # elif tidied_attribute_name == "Preferred_unit":
                #     # we are using the unit.symbol slot VERY LIBERALLY here
                #     # and I doubt that UOMs will show up in linkml2sheets output
                #     new_uom = UnitOfMeasure(symbol=value)
                #     global_target_schema.slots[tidied_slot_name].unit = new_uom
                else:
                    global_target_schema.classes[current_class].slot_usage[tidied_slot_name].annotations[
                        tidied_attribute_name] = new_annotation


process_sheet(harmonized_sheets)


def remove_forbidden_or_associate(sheet: pd.DataFrame):
    """
    Iterate over the slot/scn and class columns in the sheet.
    Check if there is already a slot usage for that combination.
    If the requirement variable in the usage is "-", remove the slot usage.
    Otherwise, associate the slot with the class.
    """
    relevant_columns = ['Structured comment name', 'class', 'Requirement']
    relevant_sheet = sheet[relevant_columns].copy()
    relevant_sheet.drop_duplicates(inplace=True)

    relevant_dicts = relevant_sheet.to_dict('records')

    for relevant_dict in relevant_dicts:
        tidied_scn = re.sub(r'\W+', '_', relevant_dict['Structured comment name'])
        tidied_class = convert_to_pascal_case(relevant_dict['class'])
        requirement = relevant_dict['Requirement']

        global_target_schema.classes[tidied_class].slots.append(tidied_scn)

        if requirement == "-":
            reckless_slots = global_target_schema.classes[tidied_class].slots
            reckless_slots = list(set(reckless_slots) - {tidied_scn})
            global_target_schema.classes[tidied_class].slots = reckless_slots
            if tidied_scn in global_target_schema.classes[tidied_class].slot_usage:
                del global_target_schema.classes[tidied_class].slot_usage[tidied_scn]
            else:
                if debug_mode:
                    print(f"Can't remove {tidied_scn} slot usage on {tidied_class}")

        elif requirement == "C":
            if tidied_scn in global_target_schema.classes[tidied_class].slot_usage:
                if "Requirement" in global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations:
                    del global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations['Requirement']
                else:
                    if debug_mode:
                        print(f"{tidied_class} has {tidied_scn} usage but that doesn't have a Requirement annotation")
            else:
                if debug_mode:
                    print(f"{tidied_class} does not have {tidied_scn} usage")

        elif requirement == "E":
            is_a_parent = global_target_schema.classes[tidied_class].is_a

            if is_a_parent == "EnvironmentalPackage":
                if tidied_scn in global_target_schema.classes[tidied_class].slot_usage:
                    global_target_schema.classes[tidied_class].slot_usage[tidied_scn].required = True
                    if "Requirement" in global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations:
                        del global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations['Requirement']
                    else:
                        if debug_mode:
                            print(
                                f"{tidied_class} has {tidied_scn} usage but that doesn't have a Requirement annotation")
                else:
                    if debug_mode:
                        print(f"{tidied_class} does not have {tidied_scn} usage")

            elif is_a_parent == "Checklist":
                if tidied_scn in global_target_schema.classes[tidied_class].slot_usage:
                    if "Requirement" in global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations:
                        del global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations['Requirement']
                    else:
                        if debug_mode:
                            print(
                                f"{tidied_class} has {tidied_scn} usage but that doesn't have a Requirement annotation")
                else:
                    if debug_mode:
                        print(f"{tidied_class} does not have {tidied_scn} usage")

        if "Requirement" in global_target_schema.slots[tidied_scn].annotations:
            del global_target_schema.slots[tidied_scn].annotations['Requirement']


remove_forbidden_or_associate(harmonized_sheets)

yaml_dumper.dump(global_target_schema, 'target_schema.yaml')
