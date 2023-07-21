import csv
import pprint

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

schema_file = "../../generated_schema/mixs_6_2_proposal.yaml"

ignore_attributes = [
    'annotations',  # might want to put more in here
    'examples',
    'name',
    'recommended',
    'required',
    'string_serialization',  # might want to put in an annotations
]

report_yaml_file = "../../other_reports/slot_usage_report.yaml"
report_tsv_file = "../../other_reports/slot_usage_report.tsv"

report_rows = []

schema_view = SchemaView(schema_file)

schema_classes = schema_view.all_classes()

for sck, scv in schema_classes.items():
    su = scv.slot_usage
    for suk, suv in su.items():
        suvd = suv.__dict__
        for suvdk, suvdv in suvd.items():
            if suvdv and suvdk not in ignore_attributes:
                report_rows.append({"class": sck, "slot": suk, "attribute": suvdk, "value": suvdv})

yaml_dumper.dump(report_rows, report_yaml_file)

with open(report_tsv_file, 'w', newline='') as tsvfile:
    writer = csv.DictWriter(tsvfile, fieldnames=report_rows[0].keys(), delimiter='\t')
    writer.writeheader()
    writer.writerows(report_rows)
