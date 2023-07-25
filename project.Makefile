
##only if running the postgres queries
#include local/.env # for PGPASSWORD, BIOSAMPLE_DB_USER etc
#export $(shell sed 's/=.*//'  local/.env)

.PHONY: all clean squeaky-clean conflicts-cleanup conflicts-all

RUN = poetry run

SOURCE_SCHEMA_PATH = generated-schema/$(PROPOSAL).yaml

DOCDIR = mixs-docs-md
TEMPLATEDIR = mixs-docs-templates

PROPOSAL=mixs_6_2_rc
LEGACY=mixs_v6.xlsx


all: squeaky-clean $(SOURCE_SCHEMA_PATH) \
other-reports/curated-data-coverage-report.yaml other-reports/extracted-data-coverage-report.yaml \
linkml-validate-exhaustive linkml-validate-extracted \
text-mining-results/mixs-v6-repaired-term-title-token-matrix.tsv \
schemasheets-to-usage/$(PROPOSAL).yaml.exhaustive.usage-report.tsv schemasheets-to-usage/$(PROPOSAL).yaml.concise.usage-report.tsv \
conflicts-all other-reports/mixs-scns-vs-ncbi-harmonized-attributes.yaml \
schema-derivatives/$(PROPOSAL).owl.ttl schema-derivatives/$(PROPOSAL).schema.json \
schema-derivatives/$(PROPOSAL).form.xlsx schema-derivatives/$(PROPOSAL).json \
final-deletions generated-schema/final-$(PROPOSAL).yaml \
validate-multiple-mims-soil converted-data/MimsSoil-example.csv converted-data/MimsSoil-example.ttl \
other-reports/slot-usage-report.tsv other-reports/schema-lint-report.tsv

clean:
	rm -rf generated-schema/$(PROPOSAL)-usage-populated-raw.tsv
	rm -rf generated-schema/meta.xlsx
	rm -rf schemasheets-to-usage/$(PROPOSAL)-usage.tsv
	rm -rf curated-data/MimsSoil-example.csv

# might not want to automatically clean/delete slow-to generate ncbi-biosample-sql/results files
squeaky-clean: clean
	@for dir in onflict-reports converted-data downloads extracted-data generated-schema GSC-excel-harmonized-repaired \
		mixs-docs-md other-reports schema-derivatives schemasheets-to-usage text-mining-results ; do \
		rm -rf $$dir/*; \
		mkdir -p $$dir; \
		touch $$dir/.gitkeep; \
	done
	rm -rf curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml

generated-schema/mixs_6_2_rc.yaml:
	$(RUN) write-mixs-linkml \
		 --gsc-excel-input 'https://github.com/only1chunts/mixs-cih-fork/raw/main/mixs/excel/mixs_v6.xlsx' \
		 --gsc-excel-output-dir downloads \
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
		 --minimal-combos \
		 --non-ascii-replacement '' \
		 --schema-name $(PROPOSAL) \
		 --textual-key 'Structured comment name' \
		 --linkml-stage-mods-file config/linkml-stage-mixs-modifications.yaml \
		 --range-pattern-inference-file config/mixs-stringsers-expvals-to-linkml-ranges-patterns.tsv \
		 --tables-stage-mods-file config/mixs-tables-stage-modifications.tsv \
		 --harmonized-mixs-tables-file GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv \
		 --repaired-mixs-tables-file GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv \
		 --extracted-examples-out extracted-data/$(PROPOSAL).extracted-examples.yaml \
		 --repair-report conflict-reports/conflict-repair-report.tsv \
		 --unmapped-report other-reports/un-handled-stringsers-expvals.tsv \
		 --schema-file-out $@

$(SOURCE_SCHEMA_PATH).notated.yaml: text-mining-results/mixs-v6-repaired-term-title-token-matrix.tsv

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/63
text-mining-results/mixs-v6-repaired-term-title-token-matrix.tsv: config/curated-slot-notes-by-text-mining.tsv \
$(SOURCE_SCHEMA_PATH) schemasheets-to-usage/$(PROPOSAL)-concise-usage.tsv
	$(RUN) add-notes-from-text-mining \
		--dtm-input-slot title \
		--input-col-vals-file text-mining-results/mixs-v6-repaired-term-title-token-list.tsv \
		--input-dtm-notes-mapping $(word 1,$^) \
		--input-schema-file $(word 2,$^) \
		--input-usage-report $(word 3,$^) \
		--output-schema-file generated-schema/$(PROPOSAL).yaml.notated.yaml \
		--dtm-output $@

other-reports/curated-data-coverage-report.yaml: curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml $(SOURCE_SCHEMA_PATH)
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

other-reports/extracted-data-coverage-report.yaml: extracted-data/unwrapped.$(PROPOSAL).extracted-examples.yaml $(SOURCE_SCHEMA_PATH)
	poetry run exhaustion-check \
		--class-name "ExhaustiveTestClass" \
		--instance-yaml-file $(word 1,$^) \
		--output-yaml-file $@ \
		--schema-path $(word 2,$^)

linkml-validate-exhaustive: $(SOURCE_SCHEMA_PATH) curated-data/ExhaustiveTestClassCollection-wrapped-example-data.yaml
	$(RUN) linkml-validate --target-class ExhaustiveTestClassCollection --schema $^

linkml-validate-extracted: $(SOURCE_SCHEMA_PATH) extracted-data/$(PROPOSAL).extracted-examples.yaml
	$(RUN) linkml-validate --target-class ExhaustiveTestClassCollection --schema $^

curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml: curated-data/ExhaustiveTestClassCollection-wrapped-example-data.yaml
	$(RUN) get-first-of-first \
		--input_data $< \
		--output_data $@.temp
	$(RUN) pretty-sort-yaml \
		-i $@.temp \
		-o $@
	rm -rf $@.temp

extracted-data/unwrapped.$(PROPOSAL).extracted-examples.yaml: extracted-data/$(PROPOSAL).extracted-examples.yaml
	$(RUN) get-first-of-first \
		--input_data $< \
		--output_data $@.temp
	$(RUN) pretty-sort-yaml \
		-i $@.temp \
		-o $@
	rm -rf $@.temp


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/62
schemasheets-to-usage/$(PROPOSAL)-concise-usage.tsv: $(SOURCE_SCHEMA_PATH)
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other-reports/populated-generated-debug-report.yaml \
		--log-file other-reports/populated-with-generated-spec-log.txt \
		--output-path $@.tmp \
		--report-style concise \
		--source-path $<
	grep -v -e '^>' $@.tmp > $@
	rm -rf $@.tmp

schemasheets-to-usage/$(PROPOSAL).yaml.exhaustive.schemasheet.tsv: generated-schema/$(PROPOSAL).yaml.notated.yaml
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other-reports/notated-populated-generated-debug-report.yaml \
		--log-file other-reports/notated-populated-with-generated-spec-log.txt \
		--output-path $@ \
		--report-style exhaustive \
		--source-path $<

schemasheets-to-usage/$(PROPOSAL).yaml.exhaustive.usage-report.tsv: schemasheets-to-usage/$(PROPOSAL).yaml.exhaustive.schemasheet.tsv
	grep -v -e '^>' $< > $@

schemasheets-to-usage/$(PROPOSAL).yaml.concise.schemasheet.tsv: generated-schema/$(PROPOSAL).yaml.notated.yaml
	$(RUN) linkml2schemasheets-template \
		--debug-report-path other-reports/notated-populated-generated-debug-report.yaml \
		--log-file other-reports/notated-populated-with-generated-spec-log.txt \
		--output-path $@ \
		--report-style exhaustive \
		--source-path $<

schemasheets-to-usage/$(PROPOSAL).yaml.concise.usage-report.tsv: schemasheets-to-usage/$(PROPOSAL).yaml.concise.schemasheet.tsv
	grep -v -e '^>' $< > $@



# # # #

conflicts-cleanup:
	rm -rf conflict-reports/$(PROPOSAL)*conflicts*tsv

# generalize this
conflicts-all: conflicts-cleanup \
conflict-reports/$(PROPOSAL).ID.SCN.conflicts.pre.tsv \
conflict-reports/$(PROPOSAL).ID.SCN.conflicts.post.tsv \
conflict-reports/$(PROPOSAL).ID.Item.conflicts.pre.tsv \
conflict-reports/$(PROPOSAL).ID.Item.conflicts.post.tsv \
conflict-reports/$(PROPOSAL).ID.Def.conflicts.pre.tsv \
conflict-reports/$(PROPOSAL).ID.Def.conflicts.post.tsv \
conflict-reports/$(PROPOSAL).ID.Occurrence.conflicts.pre.tsv \
conflict-reports/$(PROPOSAL).ID.Occurrence.conflicts.post.tsv \
conflict-reports/$(PROPOSAL).ID.Section.conflicts.pre.tsv \
conflict-reports/$(PROPOSAL).ID.Section.conflicts.post.tsv \
conflict-reports/$(PROPOSAL).ID.prefunit.conflicts.pre.tsv \
conflict-reports/$(PROPOSAL).ID.prefunit.conflicts.post.tsv \
conflict-reports/$(PROPOSAL).SCN.Item.conflicts.pre.tsv \
conflict-reports/$(PROPOSAL).SCN.Item.conflicts.post.tsv

#https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/66
conflict-reports/$(PROPOSAL).ID.SCN.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@

# can also run the conflict check on the repaired file
conflict-reports/$(PROPOSAL).ID.SCN.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Structured comment name' \
		--output-file $@


conflict-reports/$(PROPOSAL).ID.Item.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Item' \
		--output-file $@

conflict-reports/$(PROPOSAL).ID.Item.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Item' \
		--output-file $@


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/64
conflict-reports/$(PROPOSAL).ID.Def.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Definition' \
		--output-file $@

conflict-reports/$(PROPOSAL).ID.Def.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Definition' \
		--output-file $@


# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/64
conflict-reports/$(PROPOSAL).ID.Occurrence.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Occurrence' \
		--output-file $@

conflict-reports/$(PROPOSAL).ID.Occurrence.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Occurrence' \
		--output-file $@


conflict-reports/$(PROPOSAL).ID.Section.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Section' \
		--output-file $@

conflict-reports/$(PROPOSAL).ID.Section.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Section' \
		--output-file $@


conflict-reports/$(PROPOSAL).ID.prefunit.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Preferred unit' \
		--output-file $@

conflict-reports/$(PROPOSAL).ID.prefunit.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'MIXS ID' \
		--y-column 'Preferred unit' \
		--output-file $@


conflict-reports/$(PROPOSAL).SCN.Item.conflicts.pre.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Item \
		--output-file $@

conflict-reports/$(PROPOSAL).SCN.Item.conflicts.post.tsv: GSC-excel-harmonized-repaired/$(PROPOSAL).repaired.tsv
	$(RUN) find-Xs-with-multiple-Ys \
		--input-file $< \
		--x-column 'Structured comment name' \
		--y-column Item \
		--output-file $@

# # # #

# todo how to communicate/save download date?
ncbi-biosample-sql/results/minimal.csv: ncbi-biosample-sql/queries/minimal.sql
	# ~ 5 minutes
	date
	psql --csv \
		-U $(BIOSAMPLE_DB_USER) \
		-h $(BIOSAMPLE_DB_HOST) -p $(BIOSAMPLE_DB_PORT) \
		-d $(BIOSAMPLE_DB_DB_NAME) \
		-f $< > $@
	date

ncbi-biosample-sql/results/ncbi-biosample-harmonized-attribute-usage.csv: ncbi-biosample-sql/queries/harmonized-name-usage-counts.sql
	# ~ 5 minutes
	date
	psql --csv \
		-U $(BIOSAMPLE_DB_USER) \
		-h $(BIOSAMPLE_DB_HOST) -p $(BIOSAMPLE_DB_PORT) \
		-d $(BIOSAMPLE_DB_DB_NAME) \
		-f $< > $@
	date

GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv: $(SOURCE_SCHEMA_PATH)

# note one TSV and one CSV
other-reports/mixs-scns-vs-ncbi-harmonized-attributes.yaml: GSC-excel-harmonized-repaired/$(LEGACY).harmonized.tsv \
ncbi-biosample-sql/results/ncbi-biosample-harmonized-attribute-usage.csv
	$(RUN) mixs-scns-vs-ncbi-harmonized-attributes \
		--mixs-scns-file $(word 1,$^) \
		--ncbi-harmonized-names-file $(word 2,$^) \
		--output-file $@

schema-derivatives/$(PROPOSAL).owl.ttl: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-owl \
		--output $@ \
		--format ttl \
		--metadata-profile rdfs $<

schema-derivatives/$(PROPOSAL).schema.json: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-json-schema --closed $< > $@

schema-derivatives/$(PROPOSAL).form.xlsx: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-excel --output $@ $<

# --materialize-patterns
# --materialize-attributes / --no-materialize-attributes
schema-derivatives/$(PROPOSAL).json: $(SOURCE_SCHEMA_PATH)
	$(RUN) gen-linkml \
		--materialize-patterns \
		--materialize-attributes \
		--output $@ $<
	cp $@ data_harmonizer/schemas

final-deletions:
	rm -rf curated-data/unwrapped-curated-data-for-slot-coverage-check.yaml
	rm -rf extracted-data/unwrapped.$(PROPOSAL).extracted-examples.yaml
	rm -rf schemasheets-to-usage/$(PROPOSAL)-concise-usage.tsv

generated-schema/final-$(PROPOSAL).yaml: generated-schema/$(PROPOSAL).yaml.notated.yaml
	$(RUN) remove-exhaustive-elements-validation-conveniences \
		--input-schema $< \
		--output-schema $@
	rm -rf $<
	mv $@ $(SOURCE_SCHEMA_PATH)

.PHONY: validate-multiple-mims-soil

validate-multiple-mims-soil: $(SOURCE_SCHEMA_PATH) curated-data/MimsSoil-example.yaml
	$(RUN) linkml-validate \
		--schema $^

converted-data/MimsSoil-example.csv: $(SOURCE_SCHEMA_PATH) curated-data/MimsSoil-example.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class MixsCompliantData \
		--index-slot mims_soil_data \
		--schema $^

# https://github.com/turbomam/mixs-envo-struct-knowl-extraction/issues/76
converted-data/MimsSoil-example.ttl: $(SOURCE_SCHEMA_PATH) curated-data/MimsSoil-example.yaml
	$(RUN) linkml-convert \
		--output $@ \
		--target-class MixsCompliantData \
		--index-slot mims_soil_data \
		--schema $^

$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
#	# copying of images and static content
#	cp $(SRC)/docs/*md $(DOCDIR) ; \
#	cp -r $(SRC)/docs/images $(DOCDIR) ;
	$(RUN) gen-doc -d $(DOCDIR) --template-directory $(TEMPLATEDIR)  --use-slot-uris $(SOURCE_SCHEMA_PATH)
	#mv $(DOCDIR)/TEMP.md $(DOCDIR)/temp.md

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

testdoc: gendoc serve

# Test documentation locally
serve: mkd-serve

# Test data harmonizer locally
dh-dev: schema-derivatives/$(PROPOSAL).json
	cd data_harmonizer && npm run dev

# GH pages deployment including data harmonizer is handled by .github/workflows/deploy-docs.yaml

# some mkdocs commands create a site directory
#  which is gitignored
# so removed unnecessary mixs-docs-html

other-reports/slot-usage-report.tsv:
	$(RUN) usage-detector \
		--ignore-attributes 'annotations' \
		--ignore-attributes 'examples' \
		--ignore-attributes 'name' \
		--ignore-attributes 'recommended' \
		--ignore-attributes 'required' \
		--ignore-attributes string_serialization \
		--report-tsv-file $@ \
		--schema-file $(SOURCE_SCHEMA_PATH)

other-reports/schema-lint-report.tsv: $(SOURCE_SCHEMA_PATH)
	- $(RUN) linkml-lint --format tsv \
		--output $@ $<