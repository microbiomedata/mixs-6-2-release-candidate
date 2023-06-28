.PHONY: all clean squeaky_clean check-jsonschema-exhaustive check-jsonschema-extracted

RUN = poetry run

all: squeaky_clean \
generated/GSC_MIxS_6_usage.tsv generated/mixs_v6.xlsx.harmonized.tsv.dtm.tsv generated/GSC_MIxS_6.yaml.schema.json \
generated/exhaustion_report.yaml \
check-jsonschema-exhaustive check-jsonschema-extracted \
generated/GSC_MIxS_6.yaml.notated_usage.tsv

clean:
	rm -rf generated/GSC_MIxS_6_usage.tsv
	rm -rf generated/GSC_MIxS_6_usage_populated_raw.tsv
	rm -rf generated/meta.xlsx

squeaky_clean: clean
	rm -rf generated/*
	mkdir -p generated
	touch generated/.gitkeep

generated/GSC_MIxS_6.yaml:
	$(RUN) python src/mixs_envo_struct_knowl_extraction/mixs_linkml_from_xlsx.py

## add back in at some point?
# --base-class enum_definition \
# --base-class permissible_value
# --columns-to-insert enum
# --columns-to-insert permissible_value \

generated/GSC_MIxS_6_usage_populated_no_blank_cols.tsv: generated/GSC_MIxS_6_usage.tsv

generated/GSC_MIxS_6_usage.tsv: generated/GSC_MIxS_6.yaml
	$(RUN) generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert slot \
		 --destination-template $@ \
		 --meta-model-excel-file generated/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

# may still conatin some good ideas for vectorizing
#generated/mixs_v6.xlsx.harmonized.tsv.dtm.tsv:
#	$(RUN) python src/mixs_envo_struct_knowl_extraction/mixs_dtm.py

generated/mixs_v6.xlsx.harmonized.tsv.dtm.tsv: generated/GSC_MIxS_6_usage_populated_no_blank_cols.tsv
	$(RUN) python src/mixs_envo_struct_knowl_extraction/click_dtm.py \
		--dtm-input-slot title \
		--input-dtm-notes-mapping config/dtm_to_slot_notes.tsv \
		--input-schema-file generated/GSC_MIxS_6.yaml \
		--input-usage-report $< \
		--dtm-output $@ \
		--output-schema-file generated/GSC_MIxS_6.yaml.notated.yaml \
		--input-col-vals-file generated/title_values.txt \

generated/GSC_MIxS_6.yaml.schema.json: generated/GSC_MIxS_6.yaml
	$(RUN) gen-json-schema \
		--closed $< > $@


generated/exhaustion_report.yaml: generated/single-exhaustive_test-record.yaml
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $< \
		--output-yaml-file $@ \
		--schema-path generated/GSC_MIxS_6.yaml

check-jsonschema-exhaustive: generated/GSC_MIxS_6.yaml.schema.json data/ExhaustiveTestClassCollection-example-data.yaml
	$(RUN) check-jsonschema  --schemafile $^

check-jsonschema-extracted: generated/GSC_MIxS_6.yaml.schema.json generated/mixs_v6.xlsx.examples.yaml
	- $(RUN) check-jsonschema  --schemafile $^

generated/single-exhaustive_test-record.yaml: data/ExhaustiveTestClassCollection-example-data.yaml
	yq e '.exhaustive_test_set[0]' $< | cat > $@.raw
	poetry run pretty-sort-yaml \
		-i $@.raw \
		-o $@
	rm -rf $@.raw

generated/GSC_MIxS_6.yaml.notated_usage.tsv: generated/GSC_MIxS_6.yaml.notated.yaml
	$(RUN) generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert enum \
		 --columns-to-insert slot \
		 --columns-to-insert permissible_value \
		 --destination-template $@ \
		 --meta-model-excel-file generated/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

