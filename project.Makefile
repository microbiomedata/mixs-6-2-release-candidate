include local/.env # for PGPASSWORD, BIOSAMPLE_DB_USER etc
export $(shell sed 's/=.*//'  local/.env)

.PHONY: all clean squeaky-clean conflicts-cleanup conflicts-all

RUN = poetry run

SOURCE_SCHEMA_PATH = generated_schema/GSC_MIxS_6.yaml

DOCDIR = mixs-docs-md
TEMPLATEDIR = mixs-docs-templates

all: squeaky-clean $(SOURCE_SCHEMA_PATH) \
linkml-validate-exhaustive linkml-validate-extracted \
other_reports/curated_data_coverage_report.yaml other_reports/extracted_data_coverage_report.yaml \
text_mining_results/mixs_v6_repaired_term_title_token_matrix.tsv \
schemasheets_to_usage/GSC_MIxS_6.yaml.exhaustive.usage-report.tsv schemasheets_to_usage/GSC_MIxS_6.yaml.concise.usage-report.tsv \
conflicts-all other_reports/mixs-scns-vs-ncbi-harmonized-attributes.yaml \
schema_derivatives/GSC_MIxS_6.owl.ttl schema_derivatives/GSC_MIxS_6.schema.json schema_derivatives/GSC_MIxS_6.form.xlsx \
final_deletions generated_schema/final_GSC_MIxS_6.yaml \
validate_multiple_mims_soil \
converted_data/MimsSoil_example.csv converted_data/MimsSoil_example.ttl \
deploy

# converted_data/MimsSoil_example.ttl

clean:
	rm -rf generated_schema/GSC_MIxS_6_usage_populated_raw.tsv
	rm -rf generated_schema/meta.xlsx
	rm -rf schemasheets_to_usage/GSC_MIxS_6_usage.tsv
	rm -rf curated_data/MimsSoil_example.csv

# might not want to automatically clean/delete slow-to generate ncbi_biosample_sql/results files
squeaky-clean: clean
	@for dir in conflict_reports downloads extracted_data generated_schema mixs_excel_harmonized_repaired \
		other_reports schemasheets_to_usage text_mining_results schema_derivatives converted_data mixs-docs-html mixs-docs-md ; do \
		rm -rf $$dir/*; \
		mkdir -p $$dir; \
		touch $$dir/.gitkeep; \
	done
	rm -rf curated_data/unwrapped_curated_data_for_slot_coverage_check.yaml

generated_schema/GSC_MIxS_6.yaml:
	$(RUN) write_mixs_linkml \
		 --base-url 'https://github.com/only1chunts/mixs-cih-fork/raw/main/mixs/excel/' \
		 --schema-name GSC_MIxS_6 \
		 --checklists migs_ba \
		 --checklists migs_eu \
		 --checklists migs_org \
		 --checklists migs_pl \
		 --checklists migs_vi \
		 --checklists mimag \
		 --checklists mimarks_c \
		 --checklists mimarks_s \
		 --checklists mims \
		 --checklists misag \
		 --checklists miuvig \
		 --non-ascii-replacement '' \
		 --scn-key 'Structured comment name' \
		 --linkml-stage-mods-file config/linkml_stage_mixs_modifications.yaml \
		 --range-pattern-inference-file config/mixs_stringsers_expvals_to_linkml_ranges_patterns.tsv \
		 --tables-stage-mods-file config/mixs_tables_stage_modifications.tsv \
		 --minimal-combos \
		 --extracted-examples-out extracted_data/mixs_v6.xlsx.extracted_examples.yaml \
		 --harmonized-mixs-tables-file mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv \
		 --mixs-excel-output-file downloads/mixs_v6.xlsx \
		 --repair-report conflict_reports/conflict_repair_report.tsv \
		 --repaired-mixs-tables-file mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv \
		 --schema-file-out $(SOURCE_SCHEMA_PATH) \
		 --unmapped-report other_reports/un-handled_stringsers_expvals.tsv \

$(SOURCE_SCHEMA_PATH).notated.yaml: text_mining_results/mixs_v6_repaired_term_title_token_matrix.tsv

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/63
text_mining_results/mixs_v6_repaired_term_title_token_matrix.tsv: config/curated_slot_notes_by_text_mining.tsv \
$(SOURCE_SCHEMA_PATH) schemasheets_to_usage/GSC_MIxS_6_concise_usage.tsv
	$(RUN) add_notes_from_text_mining \
		--dtm-input-slot title \
		--input-col-vals-file text_mining_results/mixs_v6_repaired_term_title_token_list.tsv \
		--input-dtm-notes-mapping $(word 1,$^) \
		--input-schema-file $(word 2,$^) \
		--input-usage-report $(word 3,$^) \
		--output-schema-file generated_schema/GSC_MIxS_6.yaml.notated.yaml \
		--dtm-output $@

other_reports/curated_data_coverage_report.yaml: curated_data/unwrapped_curated_data_for_slot_coverage_check.yaml $(SOURCE_SCHEMA_PATH)
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

other_reports/extracted_data_coverage_report.yaml: extracted_data/unwrapped.mixs_v6.xlsx.extracted_examples.yaml $(SOURCE_SCHEMA_PATH)
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

linkml-validate-exhaustive: $(SOURCE_SCHEMA_PATH) curated_data/ExhaustiveTestClassCollection-wrapped-example-data.yaml
	$(RUN) linkml-validate --target-class ExhaustiveTestClassCollection --schema $^

linkml-validate-extracted: $(SOURCE_SCHEMA_PATH) extracted_data/mixs_v6.xlsx.extracted_examples.yaml
	$(RUN) linkml-validate --target-class ExhaustiveTestClassCollection --schema $^

curated_data/unwrapped_curated_data_for_slot_coverage_check.yaml: curated_data/ExhaustiveTestClassCollection-wrapped-example-data.yaml
	$(RUN) get-first-of-first \
		--input_data $< \
		--output_data $@.temp
	$(RUN) pretty-sort-yaml \
		-i $@.temp \
		-o $@
	rm -rf $@.temp

extracted_data/unwrapped.mixs_v6.xlsx.extracted_examples.yaml: extracted_data/mixs_v6.xlsx.extracted_examples.yaml
	$(RUN) get-first-of-first \
		--input_data $< \
		--output_data $@.temp
	$(RUN) pretty-sort-yaml \
		-i $@.temp \
		-o $@
	rm -rf $@.temp


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/62
schemasheets_to_usage/GSC_MIxS_6_concise_usage.tsv: $(SOURCE_SCHEMA_PATH)
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other_reports/populated-generated-debug-report.yaml \
		--log-file other_reports/populated-with-generated-spec-log.txt \
		--output-path $@.tmp \
		--report-style concise \
		--source-path $<
	grep -v -e '^>' $@.tmp > $@
	rm -rf $@.tmp

schemasheets_to_usage/GSC_MIxS_6.yaml.exhaustive.schemasheet.tsv: generated_schema/GSC_MIxS_6.yaml.notated.yaml
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other_reports/notated_populated-generated-debug-report.yaml \
		--log-file other_reports/notated_populated-with-generated-spec-log.txt \
		--output-path $@ \
		--report-style exhaustive \
		--source-path $<

schemasheets_to_usage/GSC_MIxS_6.yaml.exhaustive.usage-report.tsv: schemasheets_to_usage/GSC_MIxS_6.yaml.exhaustive.schemasheet.tsv
	grep -v -e '^>' $< > $@

schemasheets_to_usage/GSC_MIxS_6.yaml.concise.schemasheet.tsv: generated_schema/GSC_MIxS_6.yaml.notated.yaml
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other_reports/notated_populated-generated-debug-report.yaml \
		--log-file other_reports/notated_populated-with-generated-spec-log.txt \
		--output-path $@ \
		--report-style exhaustive \
		--source-path $<

schemasheets_to_usage/GSC_MIxS_6.yaml.concise.usage-report.tsv: schemasheets_to_usage/GSC_MIxS_6.yaml.concise.schemasheet.tsv
	grep -v -e '^>' $< > $@



# # # #

conflicts-cleanup:
	rm -rf conflict_reports/mixs_v6.xlsx*conflicts*tsv

conflicts-all: conflicts-cleanup \
conflict_reports/mixs_v6.xlsx.ID.SCN.conflicts.pre.tsv \
conflict_reports/mixs_v6.xlsx.ID.SCN.conflicts.post.tsv \
conflict_reports/mixs_v6.xlsx.ID.Item.conflicts.pre.tsv \
conflict_reports/mixs_v6.xlsx.ID.Item.conflicts.post.tsv \
conflict_reports/mixs_v6.xlsx.ID.Def.conflicts.pre.tsv \
conflict_reports/mixs_v6.xlsx.ID.Def.conflicts.post.tsv \
conflict_reports/mixs_v6.xlsx.ID.Occurrence.conflicts.pre.tsv \
conflict_reports/mixs_v6.xlsx.ID.Occurrence.conflicts.post.tsv \
conflict_reports/mixs_v6.xlsx.ID.Section.conflicts.pre.tsv \
conflict_reports/mixs_v6.xlsx.ID.Section.conflicts.post.tsv \
conflict_reports/mixs_v6.xlsx.ID.prefunit.conflicts.pre.tsv \
conflict_reports/mixs_v6.xlsx.ID.prefunit.conflicts.post.tsv \
conflict_reports/mixs_v6.xlsx.SCN.Item.conflicts.pre.tsv \
conflict_reports/mixs_v6.xlsx.SCN.Item.conflicts.post.tsv

#https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/66
conflict_reports/mixs_v6.xlsx.ID.SCN.conflicts.pre.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@

# can also run the conflict check on the repaired file
conflict_reports/mixs_v6.xlsx.ID.SCN.conflicts.post.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@


conflict_reports/mixs_v6.xlsx.ID.Item.conflicts.pre.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Item' \
		--output-file $@

conflict_reports/mixs_v6.xlsx.ID.Item.conflicts.post.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Item' \
		--output-file $@


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/64
conflict_reports/mixs_v6.xlsx.ID.Def.conflicts.pre.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Definition' \
		--output-file $@

conflict_reports/mixs_v6.xlsx.ID.Def.conflicts.post.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Definition' \
		--output-file $@


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/64
conflict_reports/mixs_v6.xlsx.ID.Occurrence.conflicts.pre.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Occurrence' \
		--output-file $@

conflict_reports/mixs_v6.xlsx.ID.Occurrence.conflicts.post.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Occurrence' \
		--output-file $@


conflict_reports/mixs_v6.xlsx.ID.Section.conflicts.pre.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Section' \
		--output-file $@

conflict_reports/mixs_v6.xlsx.ID.Section.conflicts.post.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Section' \
		--output-file $@


conflict_reports/mixs_v6.xlsx.ID.prefunit.conflicts.pre.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Preferred unit' \
		--output-file $@

conflict_reports/mixs_v6.xlsx.ID.prefunit.conflicts.post.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Preferred unit' \
		--output-file $@


conflict_reports/mixs_v6.xlsx.SCN.Item.conflicts.pre.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Item \
		--output-file $@

conflict_reports/mixs_v6.xlsx.SCN.Item.conflicts.post.tsv: mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv
	$(RUN) find_Xs_with_multiple_Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Item \
		--output-file $@

# # # #

# todo how to communicate/save download date?
ncbi_biosample_sql/results/minimal.csv: ncbi_biosample_sql/queries/minimal.sql
	# ~ 5 minutes
	date
	psql --csv \
		-U $(BIOSAMPLE_DB_USER) \
		-h $(BIOSAMPLE_DB_HOST) -p $(BIOSAMPLE_DB_PORT) \
		-d $(BIOSAMPLE_DB_DB_NAME) \
		-f $< > $@
	date

ncbi_biosample_sql/results/ncbi_biosample_harmonized_attribute_usage.csv: ncbi_biosample_sql/queries/harmonized_name_usage_counts.sql
	# ~ 5 minutes
	date
	psql --csv \
		-U $(BIOSAMPLE_DB_USER) \
		-h $(BIOSAMPLE_DB_HOST) -p $(BIOSAMPLE_DB_PORT) \
		-d $(BIOSAMPLE_DB_DB_NAME) \
		-f $< > $@
	date

mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv: $(SOURCE_SCHEMA_PATH)

# note one TSV and one CSV
other_reports/mixs-scns-vs-ncbi-harmonized-attributes.yaml: mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv \
ncbi_biosample_sql/results/ncbi_biosample_harmonized_attribute_usage.csv
	$(RUN) mixs-scns-vs-ncbi-harmonized-attributes \
		--mixs-scns-file $(word 1,$^) \
		--ncbi-harmonized-names-file $(word 2,$^) \
		--output-file $@

schema_derivatives/GSC_MIxS_6.owl.ttl: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-owl \
		--output $@ \
		--format ttl \
		--metadata-profile rdfs $<

schema_derivatives/GSC_MIxS_6.schema.json: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-json-schema --closed $< > $@

schema_derivatives/GSC_MIxS_6.form.xlsx: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-excel --output $@ $<

final_deletions:
	rm -rf curated_data/unwrapped_curated_data_for_slot_coverage_check.yaml
	rm -rf extracted_data/unwrapped.mixs_v6.xlsx.extracted_examples.yaml
	rm -rf schemasheets_to_usage/GSC_MIxS_6_concise_usage.tsv

generated_schema/final_GSC_MIxS_6.yaml: generated_schema/GSC_MIxS_6.yaml.notated.yaml
	$(RUN) remove-exhaustive-elements-validation-conveniences \
		--input-schema $< \
		--output-schema $@
	rm -rf $<
	mv $@ $(SOURCE_SCHEMA_PATH)

.PHONY: validate_multiple_mims_soil

validate_multiple_mims_soil: $(SOURCE_SCHEMA_PATH) curated_data/MimsSoil_example.yaml
	$(RUN) linkml-validate \
		--schema $^

converted_data/MimsSoil_example.csv: $(SOURCE_SCHEMA_PATH) curated_data/MimsSoil_example.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class MixsCompliantData \
		--index-slot mims_soil_data \
		--schema $^

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/76
converted_data/MimsSoil_example.ttl: $(SOURCE_SCHEMA_PATH) curated_data/MimsSoil_example.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class MixsCompliantData \
		--index-slot mims_soil_data \
		--schema $^

$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
#	# added copying of images and renaming of TEMP.md
#	cp $(SRC)/docs/*md $(DOCDIR) ; \
#	cp -r $(SRC)/docs/images $(DOCDIR) ;
	$(RUN) gen-doc -d $(DOCDIR) --template-directory $(TEMPLATEDIR) $(SOURCE_SCHEMA_PATH)
	#mv $(DOCDIR)/TEMP.md $(DOCDIR)/temp.md

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

testdoc: gendoc serve

# Test documentation locally
serve: mkd-serve

# was deploy: all mkd-gh-deploy
deploy: gendoc mkd-gh-deploy