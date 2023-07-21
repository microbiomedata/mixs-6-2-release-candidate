# Slot: soil_texture_class


_One of the 12 soil texture classes use to describe soil texture based on the relative proportion of different grain sizes  of mineral particles [sand (50 um to 2 mm), silt (2 um to 50 um), and clay (<2 um)] in a soil_



URI: [MIXS:0001164](https://w3id.org/mixs/0001164)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [SOILTEXTURECLASSENUM](SOILTEXTURECLASSENUM.md)






## Examples

| Value |
| --- |
| silty clay loam |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: soil_texture_class
description: One of the 12 soil texture classes use to describe soil texture based
  on the relative proportion of different grain sizes  of mineral particles [sand
  (50 um to 2 mm), silt (2 um to 50 um), and clay (<2 um)] in a soil
title: soil texture classification
notes:
- classification
- soil
- texture
examples:
- value: silty clay loam
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001164
multivalued: false
alias: soil_texture_class
domain_of:
- FoodFarmEnvironment
range: SOIL_TEXTURE_CLASS_ENUM
required: false
recommended: false

```
</details>