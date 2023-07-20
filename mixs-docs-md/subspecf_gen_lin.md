# Slot: subspecf_gen_lin


_Information about the genetic distinctness of the sequenced organism below the subspecies level, e.g., serovar, serotype, biotype, ecotype, or any relevant genetic typing schemes like Group I plasmid. Subspecies should not be recorded in this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage rank separated by a colon, e.g., biovar:abc123_



URI: [MIXS:0000020](https://w3id.org/mixs/0000020)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsOrg](MigsOrg.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| serovar:Newport |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: subspecf_gen_lin
description: Information about the genetic distinctness of the sequenced organism
  below the subspecies level, e.g., serovar, serotype, biotype, ecotype, or any relevant
  genetic typing schemes like Group I plasmid. Subspecies should not be recorded in
  this term, but in the NCBI taxonomy. Supply both the lineage name and the lineage
  rank separated by a colon, e.g., biovar:abc123
title: subspecific genetic lineage
notes:
- lineage
examples:
- value: serovar:Newport
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{rank name}:{text}'
slot_uri: MIXS:0000020
multivalued: false
alias: subspecf_gen_lin
domain_of:
- FoodFoodProductionFacility
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- MimarksC
range: string

```
</details>