# Slot: indoor_surf


_Type of indoor surface_



URI: [MIXS:0000764](https://w3id.org/mixs/0000764)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |







## Properties

* Range: [INDOORSURFENUM](INDOORSURFENUM.md)






## Examples

| Value |
| --- |
| wall |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: indoor_surf
description: Type of indoor surface
title: indoor surface
notes:
- indoor
- surface
examples:
- value: wall
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000764
multivalued: false
alias: indoor_surf
domain_of:
- BuiltEnvironment
- FoodFoodProductionFacility
range: INDOOR_SURF_ENUM

```
</details>