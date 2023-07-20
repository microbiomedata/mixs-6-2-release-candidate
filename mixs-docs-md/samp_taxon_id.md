# Slot: samp_taxon_id


_NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa sample. Use 'synthetic metagenome for mock community/positive controls, or 'blank sample' for negative controls_



URI: [MIXS:0001320](https://w3id.org/mixs/0001320)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  no  |
[MigsEu](MigsEu.md) |  |  no  |
[MigsOrg](MigsOrg.md) |  |  no  |
[MigsPl](MigsPl.md) |  |  no  |
[MigsVi](MigsVi.md) |  |  no  |
[Mimag](Mimag.md) |  |  no  |
[MimarksC](MimarksC.md) |  |  no  |
[MimarksS](MimarksS.md) |  |  no  |
[Mims](Mims.md) |  |  no  |
[Misag](Misag.md) |  |  no  |
[Miuvig](Miuvig.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True






## Examples

| Value |
| --- |
| Gut Metagenome [NCBI:txid749906] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | Taxonomy ID |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_taxon_id
annotations:
  Expected_value:
    tag: Expected_value
    value: Taxonomy ID
description: NCBI taxon id of the sample.  Maybe be a single taxon or mixed taxa sample.
  Use 'synthetic metagenome for mock community/positive controls, or 'blank sample'
  for negative controls
title: taxonomy ID of DNA sample
notes:
- dna
- identifier
- sample
- taxon
examples:
- value: Gut Metagenome [NCBI:txid749906]
in_subset:
- investigation
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text} [NCBI:txid]'
slot_uri: MIXS:0001320
multivalued: false
alias: samp_taxon_id
domain_of:
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- MimarksC
- MimarksS
- Mims
- Misag
- Miuvig
range: string
required: true

```
</details>