# Slot: food_contact_surf


_The specific container or coating materials in direct contact with the food. Multiple values can be assigned.  This field accepts terms listed under food contact surface (http://purl.obolibrary.org/obo/FOODON_03500010)_



URI: [MIXS:0001131](https://w3id.org/mixs/0001131)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| cellulose acetate [FOODON:03500034] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03500010 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_contact_surf
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03500010
description: The specific container or coating materials in direct contact with the
  food. Multiple values can be assigned.  This field accepts terms listed under food
  contact surface (http://purl.obolibrary.org/obo/FOODON_03500010)
title: food contact surface
notes:
- food
- surface
examples:
- value: cellulose acetate [FOODON:03500034]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001131
multivalued: true
alias: food_contact_surf
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string

```
</details>