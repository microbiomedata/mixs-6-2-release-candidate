# Slot: food_pack_integrity


_A term label and term id to describe the state of the packing material and text to explain the exact condition.  This field accepts terms listed under food packing medium integrity (http://purl.obolibrary.org/obo/FOODON_03530218)_



URI: [MIXS:0001209](https://w3id.org/mixs/0001209)



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
| food packing medium compromised [FOODON:00002517] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03530218 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_pack_integrity
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03530218
description: A term label and term id to describe the state of the packing material
  and text to explain the exact condition.  This field accepts terms listed under
  food packing medium integrity (http://purl.obolibrary.org/obo/FOODON_03530218)
title: food packing medium integrity
notes:
- food
examples:
- value: food packing medium compromised [FOODON:00002517]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001209
multivalued: true
alias: food_pack_integrity
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>