# Slot: seq_meth


_Sequencing machine used. Where possible the term should be taken from the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103)_



URI: [MIXS:0000050](https://w3id.org/mixs/0000050)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |
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
| 454 Genome Sequencer FLX [OBI:0000702] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | Text or OBI |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: seq_meth
annotations:
  Expected_value:
    tag: Expected_value
    value: Text or OBI
description: Sequencing machine used. Where possible the term should be taken from
  the OBI list of DNA sequencers (http://purl.obolibrary.org/obo/OBI_0400103)
title: sequencing method
notes:
- method
examples:
- value: 454 Genome Sequencer FLX [OBI:0000702]
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}]|{text}'
slot_uri: MIXS:0000050
multivalued: false
alias: seq_meth
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
required: true

```
</details>