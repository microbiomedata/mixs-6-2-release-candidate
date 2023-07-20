# Slot: food_trav_vehic


_A descriptor for the mobile machine which is used to transport food commodities along the food distribution system.  This field accepts terms listed under vehicle (http://purl.obolibrary.org/obo/ENVO_01000604). If the proper descrptor is not listed please use text to describe the mode of travel. Multiple terms can be separated by one or more pipes_



URI: [MIXS:0001138](https://w3id.org/mixs/0001138)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| aircraft [ENVO:01001488]|car [ENVO:01000605] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | ENVO:01000604 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_trav_vehic
annotations:
  Expected_value:
    tag: Expected_value
    value: ENVO:01000604
description: A descriptor for the mobile machine which is used to transport food commodities
  along the food distribution system.  This field accepts terms listed under vehicle
  (http://purl.obolibrary.org/obo/ENVO_01000604). If the proper descrptor is not listed
  please use text to describe the mode of travel. Multiple terms can be separated
  by one or more pipes
title: food shipping transportation vehicle
notes:
- food
- transport
examples:
- value: aircraft [ENVO:01001488]|car [ENVO:01000605]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001138
multivalued: true
alias: food_trav_vehic
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>