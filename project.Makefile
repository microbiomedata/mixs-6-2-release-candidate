.PHONY: all clean squeaky-clean conflicts-cleanup conflicts-all

RUN = poetry run

all: squeaky-clean generated/GSC_MIxS_6.yaml linkml-validate-exhaustive linkml-validate-extracted \
generated/GSC_MIxS_6_usage.tsv generated/exhaustion_report.yaml generated/mixs_v6.repaired.dtm.tsv \
generated/GSC_MIxS_6.yaml.notated_usage.tsv \
conflicts-all

clean:
	rm -rf generated/GSC_MIxS_6_usage.tsv
	rm -rf generated/GSC_MIxS_6_usage_populated_raw.tsv
	rm -rf generated/meta.xlsx

squeaky-clean: clean
	rm -rf generated/*
	mkdir -p generated
	touch generated/.gitkeep

generated/GSC_MIxS_6.yaml:
	$(RUN) write_mixs_linkml

generated/GSC_MIxS_6_usage_populated_no_blank_cols.tsv: generated/GSC_MIxS_6_usage.tsv

## add back in at some point?
# --base-class enum_definition \
# --base-class permissible_value
# --columns-to-insert enum
# --columns-to-insert permissible_value
generated/GSC_MIxS_6_usage.tsv: generated/GSC_MIxS_6.yaml
	$(RUN) generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert slot \
		 --destination-template $@ \
		 --meta-model-excel-file generated/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

## may still conatin some good ideas for vectorizing
#generated/mixs_v6.repaired.dtm.tsv:
#	$(RUN) python src/mixs_envo_struct_knowl_extraction/mixs_dtm.py

generated/GSC_MIxS_6.yaml.notated.yaml: generated/mixs_v6.repaired.dtm.tsv

generated/mixs_v6.repaired.dtm.tsv: config/dtm_to_slot_notes.tsv \
generated/GSC_MIxS_6.yaml generated/GSC_MIxS_6_usage_populated_no_blank_cols.tsv
	$(RUN) add_dtm_slot_notes \
		--dtm-input-slot title \
		--input-dtm-notes-mapping $(word 1,$^) \
		--input-schema-file $(word 2,$^) \
		--input-usage-report $(word 3,$^) \
		--dtm-output $@ \
		--output-schema-file generated/GSC_MIxS_6.yaml.notated.yaml \
		--input-col-vals-file generated/title_values.txt

#generated/GSC_MIxS_6.yaml.schema.json: generated/GSC_MIxS_6.yaml
#	$(RUN) gen-json-schema \
#		--closed $< > $@

generated/exhaustion_report.yaml: generated/single-exhaustive_test-record.yaml generated/GSC_MIxS_6.yaml
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

#check-jsonschema-exhaustive: generated/GSC_MIxS_6.yaml.schema.json data/ExhaustiveTestClassCollection-example-data.yaml
#	$(RUN) check-jsonschema  --schemafile $^
#
#check-jsonschema-extracted: generated/GSC_MIxS_6.yaml.schema.json generated/mixs_v6.xlsx.examples.yaml
#	- $(RUN) check-jsonschema  --schemafile $^

linkml-validate-exhaustive: generated/GSC_MIxS_6.yaml data/ExhaustiveTestClassCollection-example-data.yaml
	$(RUN) linkml-validate --schema $^

linkml-validate-extracted: generated/GSC_MIxS_6.yaml generated/mixs_v6.xlsx.examples.yaml
	$(RUN) linkml-validate --schema $^

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
		 --columns-to-insert slot \
		 --destination-template $@ \
		 --meta-model-excel-file generated/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

# # # #

conflicts-cleanup:
	rm -rf generated/mixs_v6.xlsx*conflicts*tsv

conflicts-all: conflicts-cleanup \
generated/mixs_v6.xlsx.ID.SCN.conflicts.pre.tsv \
generated/mixs_v6.xlsx.ID.SCN.conflicts.post.tsv \
generated/mixs_v6.xlsx.ID.Item.conflicts.pre.tsv \
generated/mixs_v6.xlsx.ID.Item.conflicts.post.tsv \
generated/mixs_v6.xlsx.ID.Def.conflicts.pre.tsv \
generated/mixs_v6.xlsx.ID.Def.conflicts.post.tsv \
generated/mixs_v6.xlsx.ID.Occurrence.conflicts.pre.tsv \
generated/mixs_v6.xlsx.ID.Occurrence.conflicts.post.tsv \
generated/mixs_v6.xlsx.ID.Section.conflicts.pre.tsv \
generated/mixs_v6.xlsx.ID.Section.conflicts.post.tsv \
generated/mixs_v6.xlsx.ID.prefunit.conflicts.pre.tsv \
generated/mixs_v6.xlsx.ID.prefunit.conflicts.post.tsv \
generated/mixs_v6.xlsx.SCN.Item.conflicts.pre.tsv \
generated/mixs_v6.xlsx.SCN.Item.conflicts.post.tsv


# todo: Expected value,Value syntax
# primary key: MIXS ID
# class indicator: class (environmental package or checklist)
# invariant between classes: Structured comment name, Item, Definition, Occurrence, Section
# allowed to vary between classes: Requirement, Example

generated/mixs_v6.xlsx.ID.SCN.conflicts.pre.tsv: generated/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@

# can also run the conflict check on the repaired file
generated/mixs_v6.xlsx.ID.SCN.conflicts.post.tsv: generated/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@


generated/mixs_v6.xlsx.ID.Item.conflicts.pre.tsv: generated/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Item' \
		--output-file $@

generated/mixs_v6.xlsx.ID.Item.conflicts.post.tsv: generated/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Item' \
		--output-file $@


# inter-class definitional differences should be expressed with LinkML comments
# these may include the nams of ontologies whose terns are acceptable values
#   or root terms from an ontology
#   keep/ditch version information?
generated/mixs_v6.xlsx.ID.Def.conflicts.pre.tsv: generated/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Definition' \
		--output-file $@

generated/mixs_v6.xlsx.ID.Def.conflicts.post.tsv: generated/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Definition' \
		--output-file $@


# there are null Occurrences!
generated/mixs_v6.xlsx.ID.Occurrence.conflicts.pre.tsv: generated/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Occurrence' \
		--output-file $@

generated/mixs_v6.xlsx.ID.Occurrence.conflicts.post.tsv: generated/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Occurrence' \
		--output-file $@


generated/mixs_v6.xlsx.ID.Section.conflicts.pre.tsv: generated/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Section' \
		--output-file $@


generated/mixs_v6.xlsx.ID.Section.conflicts.post.tsv: generated/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Section' \
		--output-file $@

generated/mixs_v6.xlsx.ID.prefunit.conflicts.pre.tsv: generated/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Preferred unit' \
		--output-file $@

generated/mixs_v6.xlsx.ID.prefunit.conflicts.post.tsv: generated/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Preferred unit' \
		--output-file $@


generated/mixs_v6.xlsx.SCN.Item.conflicts.pre.tsv: generated/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Item \
		--output-file $@

generated/mixs_v6.xlsx.SCN.Item.conflicts.post.tsv: generated/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Item \
		--output-file $@
