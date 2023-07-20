# Slot: food_additive


_A substance or substances added to food to maintain or improve safety and freshness, to improve or maintain nutritional value, or improve taste, texture and appearance.  This field accepts terms listed under food additive (http://purl.obolibrary.org/obo/FOODON_03412972). Multiple terms can be separated by one or more pipes, but please consider limiting this list to the top 5 ingredients listed in order as on the food label.  See also, https://www.fda.gov/food/food-ingredients-packaging/overview-food-ingredients-additives-colors_



URI: [MIXS:0001200](https://w3id.org/mixs/0001200)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03412972 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_additive
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03412972
description: A substance or substances added to food to maintain or improve safety
  and freshness, to improve or maintain nutritional value, or improve taste, texture
  and appearance.  This field accepts terms listed under food additive (http://purl.obolibrary.org/obo/FOODON_03412972).
  Multiple terms can be separated by one or more pipes, but please consider limiting
  this list to the top 5 ingredients listed in order as on the food label.  See also,
  https://www.fda.gov/food/food-ingredients-packaging/overview-food-ingredients-additives-colors
title: food additive
notes:
- food
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001200
multivalued: true
alias: food_additive
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>