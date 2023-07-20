# Slot: intended_consumer


_Food consumer type, human or animal, for which the food product is produced and marketed. This field accepts terms listed under food consumer group (http://purl.obolibrary.org/obo/FOODON_03510136) or NCBI taxid_



URI: [MIXS:0001144](https://w3id.org/mixs/0001144)



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
| 9606 o rsenior as food consumer [FOODON:03510254] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON_03510136 or NCBI taxid |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: intended_consumer
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON_03510136 or NCBI taxid
description: Food consumer type, human or animal, for which the food product is produced
  and marketed. This field accepts terms listed under food consumer group (http://purl.obolibrary.org/obo/FOODON_03510136)
  or NCBI taxid
title: intended consumer
notes:
- consumer
examples:
- value: 9606 o rsenior as food consumer [FOODON:03510254]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{integer}|{termLabel} [{termID}]'
slot_uri: MIXS:0001144
multivalued: true
alias: intended_consumer
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string

```
</details>