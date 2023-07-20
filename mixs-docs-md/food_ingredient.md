# Slot: food_ingredient


_In this field, please list individual ingredients for multi-component food [FOODON:00002501] and simple foods that is not captured in food_type.  Please use terms that are present in FoodOn.  Multiple terms can be separated by one or more pipes |, but please consider limiting this list to the top 5 ingredients listed in order as on the food label.  See also, https://www.fda.gov/food/food-ingredients-packaging/overview-food-ingredients-additives-colors_



URI: [MIXS:0001205](https://w3id.org/mixs/0001205)



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
| bean (whole) [FOODON:00002753] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_ingredient
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON
description: In this field, please list individual ingredients for multi-component
  food [FOODON:00002501] and simple foods that is not captured in food_type.  Please
  use terms that are present in FoodOn.  Multiple terms can be separated by one or
  more pipes |, but please consider limiting this list to the top 5 ingredients listed
  in order as on the food label.  See also, https://www.fda.gov/food/food-ingredients-packaging/overview-food-ingredients-additives-colors
title: food ingredient
notes:
- food
- ingredient
examples:
- value: bean (whole) [FOODON:00002753]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001205
multivalued: true
alias: food_ingredient
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>