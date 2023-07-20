# Slot: hygienic_area


_The subdivision of areas within a food production facility according to hygienic requirements. This field accepts terms listed under hygienic food production area (http://purl.obolibrary.org/obo/ENVO). Please add a term that most accurately indicates the hygienic area your sample was taken from according to the definitions provided_



URI: [MIXS:0001253](https://w3id.org/mixs/0001253)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Low Hygiene Area |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: hygienic_area
description: The subdivision of areas within a food production facility according
  to hygienic requirements. This field accepts terms listed under hygienic food production
  area (http://purl.obolibrary.org/obo/ENVO). Please add a term that most accurately
  indicates the hygienic area your sample was taken from according to the definitions
  provided
title: hygienic food production area
notes:
- area
- food
- production
examples:
- value: Low Hygiene Area
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001253
multivalued: false
alias: hygienic_area
domain_of:
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>