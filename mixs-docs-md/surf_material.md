# Slot: surf_material


_Surface materials at the point of sampling_



URI: [MIXS:0000758](https://w3id.org/mixs/0000758)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |







## Properties

* Range: [SURFMATERIALENUM](SURFMATERIALENUM.md)






## Examples

| Value |
| --- |
| wood |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: surf_material
description: Surface materials at the point of sampling
title: surface material
notes:
- material
- surface
examples:
- value: wood
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000758
multivalued: false
alias: surf_material
domain_of:
- BuiltEnvironment
- FoodFoodProductionFacility
range: SURF_MATERIAL_ENUM

```
</details>