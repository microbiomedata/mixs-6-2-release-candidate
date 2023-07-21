# Slot: tax_class


_Method used for taxonomic classification, along with reference database used, classification rank, and thresholds used to classify new genomes_



URI: [MIXS:0000064](https://w3id.org/mixs/0000064)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsOrg](MigsOrg.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[Mimag](Mimag.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| vConTACT vContact2 (references from NCBI RefSeq v83, genus rank classification, default parameters) |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: tax_class
description: Method used for taxonomic classification, along with reference database
  used, classification rank, and thresholds used to classify new genomes
title: taxonomic classification
notes:
- classification
- taxon
examples:
- value: vConTACT vContact2 (references from NCBI RefSeq v83, genus rank classification,
    default parameters)
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000064
multivalued: false
alias: tax_class
domain_of:
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- Mims
- Misag
- Miuvig
range: string

```
</details>