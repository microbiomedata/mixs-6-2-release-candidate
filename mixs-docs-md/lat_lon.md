# Slot: lat_lon


_The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in WGS84 system_



URI: [MIXS:0000009](https://w3id.org/mixs/0000009)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
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
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True






## Examples

| Value |
| --- |
| 50.586825 6.408977 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: lat_lon
description: The geographical origin of the sample as defined by latitude and longitude.
  The values should be reported in decimal degrees and in WGS84 system
title: geographic location (latitude and longitude)
notes:
- geographic
- location
examples:
- value: 50.586825 6.408977
in_subset:
- environment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {float}'
slot_uri: MIXS:0000009
multivalued: false
alias: lat_lon
domain_of:
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
- SymbiontAssociated
range: string
required: true

```
</details>