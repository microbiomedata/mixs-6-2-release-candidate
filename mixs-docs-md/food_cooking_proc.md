# Slot: food_cooking_proc


_The transformation of raw food by the application of heat. This field accepts terms listed under food cooking (http://purl.obolibrary.org/obo/FOODON_03450002)_



URI: [MIXS:0001202](https://w3id.org/mixs/0001202)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| food blanching [FOODON:03470175] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03450002 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_cooking_proc
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03450002
description: The transformation of raw food by the application of heat. This field
  accepts terms listed under food cooking (http://purl.obolibrary.org/obo/FOODON_03450002)
title: food cooking process
notes:
- food
- process
examples:
- value: food blanching [FOODON:03470175]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001202
multivalued: true
alias: food_cooking_proc
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>