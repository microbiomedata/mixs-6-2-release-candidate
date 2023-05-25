usage_template.tsv: src/mixs_envo_struct_knowl_extraction/target_schema.yaml
	poetry run generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert slot \
		 --columns-to-insert class \
		 --destination-template $@ \
		 --meta-model-excel-file meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<