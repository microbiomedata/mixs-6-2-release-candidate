# Slot: food_prior_contact


_The material the food contacted (e.g., was processed in) prior to packaging. This field accepts terms listed under material of contact prior to food packaging (http://purl.obolibrary.org/obo/FOODON_03530077). If the proper descriptor is not listed please use text to describe the material of contact prior to food packaging_



URI: [MIXS:0001210](https://w3id.org/mixs/0001210)



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
| processed in stainless steel container [FOODON:03530081] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03530077 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_prior_contact
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03530077
description: The material the food contacted (e.g., was processed in) prior to packaging.
  This field accepts terms listed under material of contact prior to food packaging
  (http://purl.obolibrary.org/obo/FOODON_03530077). If the proper descriptor is not
  listed please use text to describe the material of contact prior to food packaging
title: material of contact prior to food packaging
notes:
- food
- material
- prior
examples:
- value: processed in stainless steel container [FOODON:03530081]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001210
multivalued: true
alias: food_prior_contact
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>