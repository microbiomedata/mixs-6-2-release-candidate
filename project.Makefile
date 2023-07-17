.PHONY: all clean squeaky-clean conflicts-cleanup conflicts-all

RUN = poetry run

all: squeaky-clean generated_schema/GSC_MIxS_6.yaml linkml-validate-exhaustive linkml-validate-extracted \
other_reports/curated_data_coverage_report.yaml text_mining_results/mixs_v6_repaired_term_title_token_matrix.tsv \
schemasheets_to_usage/GSC_MIxS_6.yaml.notated_usage.tsv \
conflicts-all final_cleanup

clean:
	rm -rf schemasheets_to_usage/GSC_MIxS_6_usage.tsv
	rm -rf generated_schema/GSC_MIxS_6_usage_populated_raw.tsv
	rm -rf generated_schema/meta.xlsx

squeaky-clean: clean
	@for dir in conflict_reports downloads extracted_data generated_schema mixs_excel_harmonized_repaired other_reports schemasheets_to_usage text_mining_results ; do \
		rm -rf $$dir/*; \
		mkdir -p $$dir; \
		touch $$dir/.gitkeep; \
	done

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
		 --extracted-examples-out extracted_data/mixs_v6.xlsx.extracted_examples.yaml \
		 --harmonized-mixs-tables-file mixs_excel_harmonized_repaired/mixs_v6.xlsx.harmonized.tsv \
		 --mixs-excel-output-file downloads/mixs_v6.xlsx \
		 --repair-report conflict_reports/conflict_repair_report.tsv \
		 --repaired-mixs-tables-file mixs_excel_harmonized_repaired/mixs_v6.xlsx.repaired.tsv \
		 --schema-file-out generated_schema/GSC_MIxS_6.yaml \
		 --unmapped-report other_reports/un-handled_stringsers_expvals.tsv \

schemasheets_to_usage/GSC_MIxS_6_usage_populated_no_blank_cols.tsv: schemasheets_to_usage/GSC_MIxS_6_usage.tsv
schemasheets_to_usage/GSC_MIxS_6_usage_populated_raw.tsv: schemasheets_to_usage/GSC_MIxS_6_usage.tsv

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/62
schemasheets_to_usage/GSC_MIxS_6_usage.tsv: generated_schema/GSC_MIxS_6.yaml
	$(RUN) generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert slot \
		 --destination-template $@ \
		 --meta-model-excel-file downloads/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

generated_schema/GSC_MIxS_6.yaml.notated.yaml: text_mining_results/mixs_v6_repaired_term_title_token_matrix.tsv

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/63
text_mining_results/mixs_v6_repaired_term_title_token_matrix.tsv: config/curated_slot_notes_by_text_mining.tsv \
generated_schema/GSC_MIxS_6.yaml schemasheets_to_usage/GSC_MIxS_6_usage_populated_no_blank_cols.tsv
	$(RUN) add_notes_from_text_mining \
		--dtm-input-slot title \
		--input-dtm-notes-mapping $(word 1,$^) \
		--input-schema-file $(word 2,$^) \
		--input-usage-report $(word 3,$^) \
		--dtm-output $@ \
		--output-schema-file generated_schema/GSC_MIxS_6.yaml.notated.yaml \
		--input-col-vals-file text_mining_results/mixs_v6_repaired_term_title_token_list.tsv

other_reports/curated_data_coverage_report.yaml: curated_data/unwrapped_curated_data_for_slot_coverage_check.yaml generated_schema/GSC_MIxS_6.yaml
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

linkml-validate-exhaustive: generated_schema/GSC_MIxS_6.yaml curated_data/ExhaustiveTestClassCollection-wrapped-example-data.yaml
	$(RUN) linkml-validate --schema $^

linkml-validate-extracted: generated_schema/GSC_MIxS_6.yaml extracted_data/mixs_v6.xlsx.extracted_examples.yaml
	$(RUN) linkml-validate --schema $^

yq: curated_data/ExhaustiveTestClassCollection-wrapped-example-data.yaml
	yq e '.exhaustive_test_set[0]' $< | cat > $@.raw
	poetry run pretty-sort-yaml \
		-i $@.raw \
		-o $@
	rm -rf $@.raw

schemasheets_to_usage/GSC_MIxS_6.yaml.notated_usage.tsv: generated_schema/GSC_MIxS_6.yaml.notated.yaml
	$(RUN) generate_and_populate_template \
		 --base-class slot_definition \
		 --columns-to-insert class \
		 --columns-to-insert slot \
		 --destination-template $@ \
		 --meta-model-excel-file downloads/meta.xlsx \
		 --meta-path https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml \
		 --source-schema-path $<

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


final_cleanup: schemasheets_to_usage/GSC_MIxS_6.yaml.notated_usage_populated_raw.tsv \
schemasheets_to_usage/GSC_MIxS_6.yaml.notated_usage_populated_no_blank_cols.tsv \
generated_schema/GSC_MIxS_6.yaml \
generated_schema/GSC_MIxS_6.yaml.notated.yaml \
text_mining_results/mixs_v6_repaired_term_title_token_matrix.tsv
	mv $(word 1,$^) schemasheets_to_usage/GSC_MIxS_6_partial_schemasheet.tsv
	mv $(word 2,$^) schemasheets_to_usage/GSC_MIxS_6_concise_slot_usage_report.tsv
	rm -rf downloads/meta.xlsx
	rm -rf $(word 3,$^)
	mv $(word 4,$^) $(word 3,$^)
	rm -rf schemasheets_to_usage/GSC_MIxS_6.yaml.notated_usage.tsv \
		schemasheets_to_usage/GSC_MIxS_6.yaml.notated_usage.tsv \
		schemasheets_to_usage/GSC_MIxS_6_usage.tsv \
		schemasheets_to_usage/GSC_MIxS_6_usage_populated_no_blank_cols.tsv