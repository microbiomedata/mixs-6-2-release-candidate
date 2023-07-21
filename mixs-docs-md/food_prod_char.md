# Slot: food_prod_char


_Descriptors of the food production system such as wild caught, free-range, organic, free-range, industrial, dairy, beef_



URI: [MIXS:0001136](https://w3id.org/mixs/0001136)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| wild caught |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_prod_char
description: Descriptors of the food production system such as wild caught, free-range,
  organic, free-range, industrial, dairy, beef
title: food production characteristics
notes:
- food
- production
examples:
- value: wild caught
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001136
multivalued: true
alias: food_prod_char
domain_of:
- FoodFarmEnvironment
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>