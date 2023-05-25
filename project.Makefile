.PHONY: all clean squeaky_clean check-jsonschema

RUN = poetry run

DEST_DIR = generated

all: squeaky_clean \
generated/GSC_MIxS_6_usage.tsv generated/mixs_v6.xlsx.harmonized.tsv.dtm.tsv generated/GSC_MIxS_6.yaml.schema.json \
generated/exhaustion_report.yaml \
check-jsonschema

generated/GSC_MIxS_6.yaml:
	$(RUN) python src/mixs_envo_struct_knowl_extraction/mixs_linkml_from_xlsx.py

generated/GSC_MIxS_6.yaml.schema.json: generated/GSC_MIxS_6.yaml
	$(RUN) gen-json-schema \
		--closed $< > $@

generated/GSC_MIxS_6_usage.tsv: generated/GSC_MIxS_6.yaml
	$(RUN) generate_and_populate_template \
		 --base-class enum_definition \
		 --base-class permissible_value \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert enum \
		 --columns-to-insert slot \
		 --columns-to-insert permissible_value \
		 --destination-template $@ \
		 --meta-model-excel-file generated/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

clean:
	#rm -rf generated/mixs_v6.xlsx
	rm -rf generated/GSC_MIxS_6_usage.tsv
	rm -rf generated/GSC_MIxS_6_usage_populated_raw.tsv
	rm -rf generated/meta.xlsx

squeaky_clean: clean
	rm -rf generated/*
	mkdir -p generated
	touch generated/.gitkeep

generated/mixs_v6.xlsx.harmonized.tsv.dtm.tsv:
	$(RUN) python src/mixs_envo_struct_knowl_extraction/mixs_dtm.py

check-jsonschema: generated/GSC_MIxS_6.yaml.schema.json data/ExhaustiveTestClassCollection-example-data.yaml
	$(RUN) check-jsonschema  --schemafile $^

generated/single-exhaustive_test-record.yaml: data/ExhaustiveTestClassCollection-example-data.yaml
	yq e '.exhaustive_test_set[0]' $< | tee $@.raw
	poetry run pretty-sort-yaml \
		-i $@.raw \
		-o $@
	rm -rf $@.raw

generated/exhaustion_report.yaml: generated/single-exhaustive_test-record.yaml
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $< \
		--output-yaml-file $@ \
		--schema-path generated/GSC_MIxS_6.yaml