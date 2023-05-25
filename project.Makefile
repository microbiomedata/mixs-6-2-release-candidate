.PHONY: all clean squeaky_clean

all: squeaky_clean GSC_MIxS_6_usage.tsv mixs_v6.xlsx.harmonized.tsv.dtm.tsv

GSC_MIxS_6.yaml:
	poetry run python src/mixs_envo_struct_knowl_extraction/mixs_linkml_from_xlsx.py

GSC_MIxS_6_usage.tsv: GSC_MIxS_6.yaml
	poetry run generate_and_populate_template \
		 --base-class enum_definition \
		 --base-class permissible_value \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert enum \
		 --columns-to-insert slot \
		 --columns-to-insert permissible_value \
		 --destination-template $@ \
		 --meta-model-excel-file meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

clean:
	#rm -rf mixs_v6.xlsx
	rm -rf GSC_MIxS_6_usage.tsv
	rm -rf GSC_MIxS_6_usage_populated_raw.tsv
	rm -rf meta.xlsx

squeaky_clean: clean
	rm -rf GSC_MIxS_6.yaml
	rm -rf GSC_MIxS_6_usage_populated_no_blank_cols.tsv
	rm -rf mixs_v6.xlsx
	rm -rf mixs_v6.xlsx.harmonized.tsv
	rm -rf mixs_v6.xlsx.harmonized.tsv.dtm.tsv

mixs_v6.xlsx.harmonized.tsv.dtm.tsv:
	poetry run python src/mixs_envo_struct_knowl_extraction/mixs_dtm.py
