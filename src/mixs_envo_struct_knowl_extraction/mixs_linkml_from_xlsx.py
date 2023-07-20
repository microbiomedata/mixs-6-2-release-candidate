# import ast
# import pprint
import os
import pprint
import re
from typing import List, Tuple, Union, Any

import click
import numpy as np
import pandas as pd
import requests
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.linkml_model import Annotation, SchemaDefinition, SlotDefinition, ClassDefinition, Example, \
    SubsetDefinition, EnumDefinition, PermissibleValue, Prefix
from linkml_runtime.linkml_model.meta import PatternExpression
from collections import Counter

from distutils.util import strtobool

from pandas import DataFrame, Series

pd.set_option('display.max_columns', None)

root_class_name = "MixsCompliantData"


# TODO do we have a term that could take the identifier role?


# todo switch from printing to logging


# todo: modify slot names if the begin with a number
#  Chris M's fix: prepend with x
#  there was some discussion at some point that number first slot names would be tolerated
#  in at least some subset of linkml functionality
#  but now they don't pass validation
#  How extensively have these slots like 16s_recover_software been used in a INSDC database?
#  see https://portal.nersc.gov/project/m3513/biosample/?C=M;O=D last updated 2022-11-08
#  MAM has a more recent database locally
#  16S recovered attribute name present, but not harmonized


def liberally_convert_to_boolean(value):
    try:
        converted_value = bool(strtobool(str(value)))
        return converted_value
    except ValueError:
        return value


def return_as_is(value):
    return value


def convert_to_pascal_case(string):
    words = re.findall(r'\w+', string.replace('_', ' '))
    pascal_case_words = [word.capitalize() for word in words]
    return ''.join(pascal_case_words)


def pascal_case_to_lower_snake_case(pascal_string):
    # Use regular expression to split the string by uppercase letters
    words = re.findall(r'[A-Z][a-z0-9]*', pascal_string)
    # Join the words with underscores and convert to lowercase
    return '_'.join(words).lower()


def convert_to_upper_snake_case(string):
    words = re.findall(r'\w+', string.replace('_', ' '))
    pascal_case_words = [word.upper() for word in words]
    return '_'.join(pascal_case_words)


def remove_non_ascii(text, non_ascii_replacement):
    return ''.join([i if ord(i) < 128 else non_ascii_replacement for i in text])


def instantiate_classes(df: pd.DataFrame, checklists, global_target_schema, minimal_combos) -> None:
    classes_list = df['class'].unique().tolist()
    classes_list.sort()

    # presumably environmental packages
    non_checklist_classes = list(set(classes_list) - set(checklists))

    class_name = root_class_name
    new_class = ClassDefinition(
        name=class_name,
        title="MIxS compliant data",
        description="A collection of data that complies with some combination of a MIxS checklist and environmental package",
        tree_root=True,
    )
    global_target_schema.classes[class_name] = new_class

    for class_name in classes_list:
        if class_name in checklists:
            if "Checklist" not in global_target_schema.classes:
                new_super = ClassDefinition(name="Checklist")
                global_target_schema.classes["Checklist"] = new_super
                class_title = class_name
            class_name = convert_to_pascal_case(class_name)
            new_class = ClassDefinition(name=class_name, title=class_title, is_a="Checklist", mixin=True)
            global_target_schema.classes[class_name] = new_class
        else:
            if "EnvironmentalPackage" not in global_target_schema.classes:
                new_super = ClassDefinition(name="EnvironmentalPackage")
                global_target_schema.classes["EnvironmentalPackage"] = new_super
            class_name = convert_to_pascal_case(class_name)
            class_title = class_name
            new_class = ClassDefinition(name=class_name, title=class_title, is_a="EnvironmentalPackage", mixin=False)
            global_target_schema.classes[class_name] = new_class

    if minimal_combos:
        selected_checklists = ["Mims"]
        selected_eps = ["Soil"]
    else:
        selected_checklists = checklists
        selected_eps = non_checklist_classes

    # todo validation (and other steps) are slow with all of the combination classes
    for checklist in selected_checklists:
        for ep in selected_eps:
            checklist_name = convert_to_pascal_case(checklist)
            ep_name = convert_to_pascal_case(ep)
            combo_name = f"{checklist_name}{ep_name}"
            combo_title = f"{checklist_name} combined with {ep_name}"

            new_class = ClassDefinition(name=combo_name, title=combo_title, is_a=ep_name, mixins=[checklist_name])
            global_target_schema.classes[combo_name] = new_class

            slot_name = f"{pascal_case_to_lower_snake_case(combo_name)}_data"

            # range is getting assigned as or modified to string!
            new_slot = SlotDefinition(
                description=f"Data that complies with {checklist_name} combined with {ep_name}",
                domain=root_class_name,
                inlined=True,
                inlined_as_list=True,
                multivalued=True,
                name=slot_name,
                range=combo_name,
                title=f"{combo_name} data",
                slot_uri=f"MIXS:{slot_name}",
            )
            global_target_schema.slots[slot_name] = new_slot

            global_target_schema.classes[root_class_name].slots.append(slot_name)


def del_and_rename_cols(df, columns_to_delete, column_mapping):
    return df.drop(columns=columns_to_delete).rename(columns=column_mapping)


def harmonize_sheets(url: str, excel_file_path, scn_key, checklists) -> pd.DataFrame:
    # todo parameterize the column dropping and renaming

    checklists = list(checklists)

    # Download the Excel file
    response = requests.get(url)
    with open(excel_file_path, 'wb') as file:
        file.write(response.content)

    # Open the desired sheets into pandas data frames
    df_mixs_raw = pd.read_excel(excel_file_path, sheet_name='MIxS')

    # Dictionary with column name mappings
    column_mapping = {
        'Item (rdfs:label)': 'Item',
        'Occurence': 'Occurrence',
    }

    # previously needed to delete ' '
    df_mixs_renamed = del_and_rename_cols(df_mixs_raw, [], column_mapping)

    # # # #

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

    mixs_sheet_col_list = mixs_by_scn_and_class_renamed.columns.tolist()

    # # # #

    df_env_packages = pd.read_excel(excel_file_path, sheet_name='environmental_packages')

    column_mapping = {
        'Environmental package': 'class',
        'Package item': 'Item',
    }

    df_env_packages_renamed = del_and_rename_cols(df_env_packages, [], column_mapping)

    # # # #

    env_packages_renamed_col_list = df_env_packages_renamed.columns.tolist()

    applicable_col_list = list(set(mixs_sheet_col_list).intersection(env_packages_renamed_col_list))

    env_pack_only = set(env_packages_renamed_col_list) - set(mixs_sheet_col_list)

    mixs_sheet_only = set(mixs_sheet_col_list) - set(env_packages_renamed_col_list)

    print(f"Columns only found in the MIxS sheet: {list(mixs_sheet_only)}")

    print(f"Columns only found in the environmental_packages sheet: {list(env_pack_only)}")

    print("\n")

    df_env_packages_renamed = df_env_packages_renamed[applicable_col_list]

    # # # #

    # Stack DataFrames vertically
    from_gsc = pd.concat([mixs_by_scn_and_class_renamed, df_env_packages_renamed])

    from_gsc = from_gsc.drop_duplicates()

    return from_gsc


def apply_jit_fixes(fixes_file: str, df: pd.DataFrame) -> tuple[DataFrame, Union[Union[Series, DataFrame, None], Any]]:
    fixes_sheet = pd.read_csv(fixes_file, sep='\t')
    fixes_lod = fixes_sheet.to_dict('records')
    reports = []
    for fix in fixes_lod:
        if fix['apply']:
            reportable = df.loc[df[fix['key']] == fix['key_val']].copy()

            reportable = reportable[['class', fix['key'], fix['target']]]
            reportable.columns = ['class', 'key_value', 'original_target_value']
            reportable['key'] = fix['key']
            reportable['target'] = fix['target']
            reportable = reportable[['class', 'key', 'key_value', 'target', 'original_target_value']]
            reportable['replacement_target_value'] = fix['target_val']

            reportable = reportable[
                reportable['original_target_value'].astype(str) != reportable['replacement_target_value'].astype(str)]
            reports.append(reportable)

            df.loc[df[fix['key']] == fix['key_val'], fix['target']] = fix['target_val']
        else:
            pass

    if len(reports) > 0:
        reports_df = pd.concat(reports)
    else:
        reports_df = None

    return df, reports_df


def process_sheet(df: pd.DataFrame, checklists, global_target_schema, scn_key, non_ascii_replacement, minimal_combos) -> \
        List[str]:
    instantiate_classes(df, checklists, global_target_schema, minimal_combos=minimal_combos)
    slots_list = df[scn_key].unique().tolist()

    for s in slots_list:
        if type(s) is not str:
            # todo how would a nan/float "slot" get in here?
            print(f"Ignoring slot '{s}' with type {s.__class__.__name__}")
            slots_list.remove(s)
    print("\n")

    slots_list.sort()

    for slot in slots_list:
        process_scn(df, slot, scn_key, global_target_schema, non_ascii_replacement)

    return slots_list


def process_scn(df: pd.DataFrame, scn: str, scn_key, global_target_schema, non_ascii_replacement) -> None:
    scn_sheet_original = df[df[scn_key] == scn]
    scn_sheet = scn_sheet_original.copy()
    scn_sheet.drop(scn_key, axis=1, inplace=True)
    scn_sheet.dropna(axis=1, how='all', inplace=True)
    attribute_names = scn_sheet.columns.tolist()
    attribute_names.remove('class')
    for attribute_name in attribute_names:
        process_attribute(df, scn, attribute_name, non_ascii_replacement, scn_key, global_target_schema)


def process_attribute(df: pd.DataFrame, scn: str, attribute_name: str, non_ascii_replacement, scn_key,
                      global_target_schema) -> None:
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
            sanitized_value = remove_non_ascii(sanitized_value, non_ascii_replacement)
            sanitized_values.append(sanitized_value)
            # also want to collapse multiple spaces into one
        else:
            sanitized_values.append(value)

        sanitized_values = list(set(sanitized_values))

    if len(sanitized_values) == 1:
        process_consensus_value(scn, attribute_name, sanitized_values[0], global_target_schema)
    else:
        attributes_by_class = filtered_df[[scn_key, 'class', attribute_name]]
        process_contested_value(attributes_by_class, scn_key, global_target_schema)


def process_consensus_value(scn: str, attribute_name: str, value: str, global_target_schema) -> None:
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
            global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation
        elif value == "C":
            global_target_schema.slots[tidied_slot_name].recommended = True
            global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation
        elif value == "E":
            global_target_schema.slots[tidied_slot_name].recommended = True
            global_target_schema.slots[tidied_slot_name].annotations[tidied_attribute_name] = new_annotation
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


def process_contested_value(attributes_by_class: pd.DataFrame, scn_key, global_target_schema) -> None:
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
        duplication_comment = f"Classes {', '.join(duplicated_classes)} has/have duplicate values in {value_name} for {scn}: {', '.join(all_values)}"
        print(f"duplication_comment: {duplication_comment}")
        print(f"dupe_frame: {dupe_frame}")
        print("\n")
        if global_target_schema.comments:
            global_target_schema.comments.append(duplication_comment)
        else:
            global_target_schema.comments = [duplication_comment]
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


def requirement_followup(sheet: pd.DataFrame, global_target_schema, debug_mode):
    """
    Iterate over the slot/scn and class columns in the sheet.
    Check if there is already a slot usage for that combination.
    If the requirement variable in the usage is "-", remove the slot usage.
    Otherwise, associate the slot with the class.
    """

    # todo parameterize
    relevant_columns = ['Structured comment name', 'class', 'Requirement']

    relevant_sheet = sheet[relevant_columns].copy()

    relevant_sheet.drop_duplicates(inplace=True)

    relevant_dicts = relevant_sheet.to_dict('records')

    for relevant_dict in relevant_dicts:
        if type(relevant_dict['Structured comment name']) is not str:
            print("Requirement specification is lacking a string-typed Structured comment name:")
            pprint.pprint(relevant_dict)
            continue
        tidied_scn = re.sub(r'\W+', '_', relevant_dict['Structured comment name'])
        tidied_class = convert_to_pascal_case(relevant_dict['class'])
        requirement = relevant_dict['Requirement']

        global_target_schema.classes[tidied_class].slots.append(tidied_scn)

        if requirement == "-":
            reckless_slots = global_target_schema.classes[tidied_class].slots
            reckless_slots = list(set(reckless_slots) - {tidied_scn})
            global_target_schema.classes[tidied_class].slots = reckless_slots
            if tidied_scn in global_target_schema.classes[tidied_class].slot_usage:
                # deleting usage of slot that has "-" requirement on a class
                #   see https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/35
                del global_target_schema.classes[tidied_class].slot_usage[tidied_scn]
            else:
                if debug_mode:
                    print(f"Can't remove {tidied_scn} slot usage on {tidied_class}")

        elif requirement == "C":
            if tidied_scn in global_target_schema.classes[tidied_class].slot_usage:
                if "Requirement" in global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations:
                    # deleting requirement annotation from slot usage,
                    #   since it has been implemented as a LinkML recommended or required attribute
                    #   I have made judgements about the interpretation of C and E
                    #   see https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/35
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
                        # deleting requirement annotation from slot usage,
                        #   since it has been implemented as a LinkML recommended or required attribute
                        #   I have made judgements about the interpretation of C and E
                        #   see https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/35
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
                        # deleting requirement annotation from slot usage,
                        #   since it has been implemented as a LinkML recommended or required attribute
                        #   I have made judgements about the interpretation of C and E
                        #   see https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/35
                        del global_target_schema.classes[tidied_class].slot_usage[tidied_scn].annotations['Requirement']
                    else:
                        if debug_mode:
                            print(
                                f"{tidied_class} has {tidied_scn} usage but that doesn't have a Requirement annotation")
                else:
                    if debug_mode:
                        print(f"{tidied_class} does not have {tidied_scn} usage")

        if "Requirement" in global_target_schema.slots[tidied_scn].annotations:
            # deleting requirement annotation from slot usage,
            #   since it has been implemented as a LinkML recommended or required attribute
            #   I have made judgements about the interpretation of C and E
            #   see https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/35
            del global_target_schema.slots[tidied_scn].annotations['Requirement']
    print("\n")


def construct_assign_simple_enumerations(sheet: pd.DataFrame, debug_mode: bool, global_target_schema) -> None:
    relevant_columns = ['Structured comment name', 'Value syntax']

    relevant_sheet = sheet[relevant_columns].copy()

    relevant_sheet.drop_duplicates(inplace=True)

    relevant_sheet['Value syntax'] = relevant_sheet['Value syntax'].astype(str)

    possible_enums_sheet = relevant_sheet[relevant_sheet['Value syntax'].str.contains(r'^\[.*\|.*\]$') &
                                          ~relevant_sheet['Value syntax'].str.contains(r'[,;\'(){}]')]

    scn_val_counts = possible_enums_sheet['Structured comment name'].value_counts()

    duplicated_scn_val_counts = scn_val_counts[scn_val_counts > 1]

    duplicated_scns = duplicated_scn_val_counts.index.tolist()

    contradictory_enums = possible_enums_sheet[possible_enums_sheet['Structured comment name'].isin(duplicated_scns)]
    print(f"{contradictory_enums = }")
    print("\n")

    # add a comment to the schema
    scns_with_contradictory_enums = contradictory_enums['Structured comment name'].unique().tolist()
    scns_with_contradictory_enums = [re.sub(r'\W+', '_', scn) for scn in scns_with_contradictory_enums]
    scns_with_contradictory_enums.sort()
    if len(scns_with_contradictory_enums) > 0:
        global_target_schema.comments.append(
            f"The following slots have  contradictory Value syntaxes so enumerations can not be created for their ranges: {', '.join(scns_with_contradictory_enums)}")

    possible_enums_no_scn_dupes = possible_enums_sheet[
        ~possible_enums_sheet['Structured comment name'].isin(duplicated_scns)]

    val_syntax_val_counts = possible_enums_no_scn_dupes['Value syntax'].value_counts()

    duplicated_val_syntax_val_counts = val_syntax_val_counts[val_syntax_val_counts > 1]

    duplicated_val_syntaxes = duplicated_val_syntax_val_counts.index.tolist()

    shared_enums = possible_enums_sheet[possible_enums_sheet['Value syntax'].isin(duplicated_val_syntaxes)]

    singleton_enums = possible_enums_sheet[~possible_enums_sheet['Value syntax'].isin(duplicated_val_syntaxes)]
    singleton_enum_dict_list = singleton_enums.to_dict('records')

    slot_to_enums_dict = {}

    for singleton_enum_dict in singleton_enum_dict_list:
        tidied_scn = tidied_scn = re.sub(r'\W+', '_', singleton_enum_dict['Structured comment name'])
        name_for_enum = f"{convert_to_upper_snake_case(singleton_enum_dict['Structured comment name'])}_ENUM"
        slot_to_enums_dict[tidied_scn] = name_for_enum
        pvs = [x.strip() for x in singleton_enum_dict['Value syntax'].strip('[]').split('|')]
        pvs.sort()
        current_enum = EnumDefinition(name=name_for_enum)
        for pv in pvs:
            current_pv = PermissibleValue(text=pv)
            current_enum.permissible_values[pv] = current_pv
        global_target_schema.enums[name_for_enum] = current_enum

    for k, v in slot_to_enums_dict.items():
        global_target_schema.slots[k].range = v
        # deleting temporary LinkML string_serialization since a range was assigned
        del global_target_schema.slots[k].string_serialization
        if "Expected_value" in global_target_schema.slots[k].annotations:
            expected_val = global_target_schema.slots[k].annotations["Expected_value"]
            expected_val_val = expected_val.value
            if expected_val_val == "enumeration":
                # deleting Expected value since a range was assigned
                del global_target_schema.slots[k].annotations["Expected_value"]
        else:
            if debug_mode:
                print(f"{k} has no Expected_value annotation")

    index = 0
    # pprint.pprint(duplicated_val_syntaxes)
    for val_syntax in duplicated_val_syntaxes:
        subset_frame = shared_enums[shared_enums['Value syntax'] == val_syntax]
        pvs = [x.strip() for x in val_syntax.strip('[]').split('|')]
        pvs.sort()
        scns = subset_frame['Structured comment name'].tolist()

        name_for_enum = f"SHARED_ENUM_{index}"
        current_enum = EnumDefinition(name=name_for_enum)
        for pv in pvs:
            current_pv = PermissibleValue(text=pv)
            current_enum.permissible_values[pv] = current_pv
        global_target_schema.enums[name_for_enum] = current_enum

        for scn in scns:
            tidied_scn = re.sub(r'\W+', '_', scn)
            global_target_schema.slots[tidied_scn].range = name_for_enum
            # deleting temporary LinkML string_serialization since a range was assigned
            del global_target_schema.slots[tidied_scn].string_serialization
            if "Expected_value" in global_target_schema.slots[tidied_scn].annotations:
                expected_val = global_target_schema.slots[tidied_scn].annotations["Expected_value"]
                expected_val_val = expected_val.value
                if expected_val_val == "enumeration":
                    # deleting Expected value since a range was assigned
                    del global_target_schema.slots[tidied_scn].annotations["Expected_value"]
            else:
                if debug_mode:
                    print(f"{scn} has no Expected_value annotation")
        index += 1


def string_ser_exp_val_to_range_patterns(tsv_file: str, global_target_schema):
    """
    Assigns ranges and patterns to slots in the target schema based on the string serialization and expected value annotations.

    Args:
        tsv_file: The path to the TSV file containing the string serialization and expected value annotations.
        global_target_schema: The target schema to update.

    Returns:
        A dictionary of unmapped string serialization and expected value pairs.
    """

    df = pd.read_csv(tsv_file, sep='\t')
    df.fillna('', inplace=True)

    slots = global_target_schema.slots
    unmapped = {}

    for k, v in slots.items():
        if v.range:
            continue
        ss = v.string_serialization or ''
        ev = v.annotations.get('Expected_value')
        if ev:
            ev = ev.value
        else:
            ev = ''
        # if ss == '{text}':
        #     print(f"Processing slot {k} with string serialization <{ss}> and expected value <{ev}>")

        row = df[(df['string_serialization'] == ss) & (df['Expected_value'] == ev)]
        row_count = row.shape[0]

        if row_count == 1:
            r = row.iloc[0]['range']
            p = row.iloc[0]['pattern']
            sp = row.iloc[0]['structured_pattern']

            if r != '':
                v.range = r
            if p != '':
                v.pattern = p
            if sp != '':
                v.structured_pattern = PatternExpression(syntax=sp, interpolated=True, partial_match=True)

            # Delete the Expected_value annotation since a range was assigned.
            if 'Expected_value' in v.annotations:
                del v.annotations['Expected_value']

            # Delete the temporary LinkML string_serialization since a range was assigned.
            if v.string_serialization:
                del v.string_serialization

        elif row_count > 1:
            print(
                f"There are {row_count} different mappings for string serialization of <{ss}> and expected value of <{ev}>")

        elif row_count == 0:
            if ss == '' and ev == '':
                # if ss == '{text}':
                #     print("assigning range string to slot")
                v.range = 'string'
            else:
                # if ss == '{text}':
                #     print("no mapping found")
                unmapped[(ss, ev)] = unmapped.get((ss, ev), 0) + 1
    unmapped_lod = []
    for i in unmapped:
        unmapped_lod.append(
            {
                'string_serialization': i[0],
                'Expected_value': i[1],
                'count': unmapped[i]
            }
        )

    return unmapped_lod


def add_exhasutive_test_class(global_target_schema):
    ExhaustiveTestClass = ClassDefinition(
        name="ExhaustiveTestClass",
    )
    all_slots = global_target_schema.slots
    for slot_k, slot_v in all_slots.items():
        ExhaustiveTestClass.slots.append(slot_k)

    exhaustive_test_set = SlotDefinition(
        inlined=True,
        inlined_as_list=True,
        multivalued=True,
        name="exhaustive_test_set",
        range="ExhaustiveTestClass",
    )

    ExhaustiveTestClassCollection = ClassDefinition(
        name="ExhaustiveTestClassCollection",
        # tree_root=True,
    )

    ExhaustiveTestClassCollection.slots.append("exhaustive_test_set")

    global_target_schema.classes["ExhaustiveTestClass"] = ExhaustiveTestClass
    global_target_schema.classes["ExhaustiveTestClassCollection"] = ExhaustiveTestClassCollection
    global_target_schema.slots["exhaustive_test_set"] = exhaustive_test_set


def dupe_property_report(property_name: str, global_target_schema):
    slots = global_target_schema.slots
    property_vals = []
    for slot_k, slot_v in slots.items():
        if slot_v[property_name]:
            property_vals.append(slot_v[property_name])

    counter = Counter(property_vals)
    sorted_elements = counter.most_common()
    dupe_values = []
    for element, count in sorted_elements:
        if count > 1:
            # print(f"{property_name} {element}: {count}")
            dupe_values.append(element)
    dupe_values.sort()
    return dupe_values


def extract_or_substitute_examples_etc(supplementary_file: str, global_target_schema):
    # requires explicit handlers for each attribute of a slot
    proposal_view = SchemaView(supplementary_file)

    # print(yaml_dumper.dumps(proposal_view.schema))

    proposal_schema = proposal_view.schema

    excel_slots = global_target_schema.slots

    # todo make a report file instead of printing
    #  or maybe this is just restating the obvious from the supplementary_file?
    for proposed_k, proposed_v in proposal_schema.slots.items():
        if proposed_k in excel_slots:
            if proposed_v.comments:
                for comment in proposed_v.comments:
                    # print(global_target_schema.slots[proposed_k].comments)
                    # print(f"attempting to ADD comment {comment} to {proposed_k}")
                    global_target_schema.slots[proposed_k].comments.append(comment)
            if proposed_v.examples:
                global_target_schema.slots[proposed_k].examples = proposed_v.examples
            if proposed_v.multivalued != global_target_schema.slots[proposed_k].multivalued:
                global_target_schema.slots[proposed_k].multivalued = proposed_v.multivalued
            if proposed_v.pattern:
                # print(
                #     f"attempting to update {proposed_k}'s pattern from {global_target_schema.slots[proposed_k].pattern} to {proposed_v.pattern} and range to string")
                global_target_schema.slots[proposed_k].pattern = proposed_v.pattern
                global_target_schema.slots[proposed_k].range = "string"
            if proposed_v.range:
                global_target_schema.slots[proposed_k].range = proposed_v.range
                if proposed_v.range != "string" and global_target_schema.slots[proposed_k].pattern:
                    # print(f"attempting to remove {proposed_k}'s pattern from {proposed_v.range} slot")
                    del global_target_schema.slots[proposed_k].pattern

        else:
            print(f"{proposed_k} is not in the target schema")
    print("\n")

    extracted_examples = {}

    for excel_k, excel_v in excel_slots.items():
        if excel_v["examples"]:
            the_examples = excel_v["examples"]
            examples_len = len(the_examples)
            if examples_len != 1:
                print(f"{excel_k} has {examples_len} examples")
            # else:
            the_example = the_examples[0].value
            the_range = global_target_schema.slots[excel_k].range

            if global_target_schema.slots[excel_k].multivalued:
                values = [the_example]
            else:
                values = the_example

            if the_range == "integer":
                convert_func = int
            elif the_range == "float":
                convert_func = float
            elif the_range == "boolean":
                convert_func = liberally_convert_to_boolean
            else:
                convert_func = return_as_is

            try:
                if isinstance(values, list):
                    extracted_examples[excel_k] = [convert_func(val) for val in values]
                else:
                    extracted_examples[excel_k] = convert_func(values)
            except ValueError:
                print(f"Couldn't convert {excel_k} with value {the_example} to {the_range}")

    return extracted_examples


@click.command()
@click.option('--debug/--no-debug', default=False, help='Enable debug mode')
@click.option('--minimal-combos/--all-combos', default=False,
              help='Should we just generate a minimal set of checklist/environmental package combinationss (or generate all combos)')
@click.option('--extracted-examples-out', default='generated/mixs_v6.xlsx.examples.yaml')
@click.option('--repair-report', default='conflict_reports/repair_report.tsv')
@click.option('--unmapped-report', default='other_reports/unmapped_report.tsv')
@click.option('--linkml-stage-mods-file', default='config/linkml_stage_mixs_modifications.yaml')
@click.option('--harmonized-mixs-tables-file', default='generated/mixs_v6.xlsx.harmonized.tsv')
@click.option('--repaired-mixs-tables-file', default='generated/mixs_v6.xlsx.repaired.tsv')
@click.option('--mixs-excel-output-file', default='generated/mixs_v6.xlsx')
@click.option('--non-ascii-replacement', default=' ')
@click.option('--schema-file-out', default='generated/GSC_MIxS_6.yaml')
@click.option('--schema-name', default='GSC_MIxS_6')
@click.option('--scn-key', default='Structured comment name')
@click.option('--base-url', default='https://github.com/only1chunts/mixs-cih-fork/raw/main/mixs/excel/',
              help='Base URL for the MIxS Excel file. Last release = https://github.com/GenomicsStandardsConsortium/mixs/raw/main/mixs/excel/')
@click.option('--checklists', multiple=True, help='Requires prior knowledge about current MIxS checklists',
              default=['migs_ba', 'migs_eu', 'migs_org', 'migs_pl', 'migs_vi', 'mimag', 'mimarks_c', 'mimarks_s',
                       'mims', 'misag', 'miuvig'])
@click.option('--range-pattern-inference-file',
              default='config/mixs_stringsers_expvals_to_linkml_ranges_patterns.tsv')
@click.option('--tables-stage-mods-file', default='config/mixs_tables_stage_modifications.tsv',
              help="Could be considered changes to the MIxS XLSX file, like @only1chunts applied recently, although we apply them to the harmonized TSV file instead")
def create_schema(non_ascii_replacement, debug, base_url, scn_key, schema_name,
                  checklists, tables_stage_mods_file, linkml_stage_mods_file, range_pattern_inference_file,
                  mixs_excel_output_file, harmonized_mixs_tables_file, repaired_mixs_tables_file, schema_file_out,
                  extracted_examples_out, repair_report, unmapped_report, minimal_combos):
    dest_dir, excel_file_name = os.path.split(mixs_excel_output_file)
    file_url = base_url + excel_file_name

    default_prefix_name = "mixs_6_2_proposal"
    default_prefix_base = "https://turbomam.github.io/mixs-envo-struct-knowl-extraction/"

    global_target_schema = SchemaDefinition(
        default_range="string",
        id=f"{default_prefix_base}/{schema_name}",
        name=schema_name,
        source=file_url,
    )

    global_target_schema.prefixes[default_prefix_name] = Prefix(default_prefix_name, default_prefix_base)
    global_target_schema.default_prefix = default_prefix_name

    harmonized_sheets = harmonize_sheets(file_url, mixs_excel_output_file, scn_key, checklists)
    harmonized_sheets.to_csv(harmonized_mixs_tables_file, index=False, sep='\t')

    harmonized_sheets, repair_report_df = apply_jit_fixes(tables_stage_mods_file, harmonized_sheets)

    repair_report_df.to_csv(repair_report, index=False, sep='\t')

    process_sheet(harmonized_sheets, checklists, global_target_schema, scn_key,
                  non_ascii_replacement, minimal_combos=minimal_combos)

    requirement_followup(harmonized_sheets, global_target_schema, debug)

    construct_assign_simple_enumerations(harmonized_sheets, debug, global_target_schema)

    unmapped = string_ser_exp_val_to_range_patterns(range_pattern_inference_file, global_target_schema)
    unmapped_frame = pd.DataFrame(unmapped)

    unmapped_frame.to_csv(unmapped_report, index=False, sep='\t')

    harmonized_sheets.to_csv(repaired_mixs_tables_file, index=False, sep='\t')

    add_exhasutive_test_class(global_target_schema)

    # todo put these two prefix definitions into a dictionary
    linkml_prefix = Prefix(prefix_prefix="linkml", prefix_reference="https://w3id.org/linkml/")
    MIXS_prefix = Prefix(prefix_prefix="MIXS", prefix_reference="https://w3id.org/mixs/")
    global_target_schema.prefixes["linkml"] = linkml_prefix
    global_target_schema.prefixes["MIXS"] = MIXS_prefix

    global_target_schema.imports.append("linkml:types")

    dupe_titles = dupe_property_report("title", global_target_schema)
    if len(dupe_titles) > 0:
        duplication_comment = f"slot titles that are associated with more than one slot name/SCN: {', '.join(dupe_titles)}"
        if global_target_schema.comments:
            global_target_schema.comments.append(duplication_comment)
        else:
            global_target_schema.comments = [duplication_comment]

    dupe_slot_uris = dupe_property_report("slot_uri", global_target_schema)
    if len(dupe_slot_uris) > 0:
        duplication_comment = f"slot_uris that are associated with more than one slot name/SCN: {', '.join(dupe_slot_uris)}"
        if global_target_schema.comments:
            global_target_schema.comments.append(duplication_comment)
        else:
            global_target_schema.comments = [duplication_comment]

    extracted_examples_dict = extract_or_substitute_examples_etc(supplementary_file=linkml_stage_mods_file,
                                                                 global_target_schema=global_target_schema)
    extracted_examples_collection = {
        "exhaustive_test_set": [extracted_examples_dict]
    }

    yaml_dumper.dump(global_target_schema, schema_file_out)

    with open(extracted_examples_out, 'w') as file:
        yaml.safe_dump(extracted_examples_collection, file)


if __name__ == '__main__':
    create_schema()
