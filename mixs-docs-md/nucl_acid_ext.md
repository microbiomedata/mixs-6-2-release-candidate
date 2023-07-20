# Slot: nucl_acid_ext


_A link to a literature reference, electronic resource or a standard operating procedure (SOP), that describes the material separation to recover the nucleic acid fraction from a sample_



URI: [MIXS:0000037](https://w3id.org/mixs/0000037)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsOrg](MigsOrg.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[Mimag](Mimag.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: nucl_acid_ext
description: A link to a literature reference, electronic resource or a standard operating
  procedure (SOP), that describes the material separation to recover the nucleic acid
  fraction from a sample
title: nucleic acid extraction
examples:
- value: https://mobio.com/media/wysiwyg/pdfs/protocols/12888.pdf
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000037
multivalued: false
alias: nucl_acid_ext
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
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
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}'
  interpolated: true
  partial_match: true

```
</details>