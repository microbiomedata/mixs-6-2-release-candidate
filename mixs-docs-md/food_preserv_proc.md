# Slot: food_preserv_proc


_The methods contributing to the prevention or retardation of microbial, enzymatic or oxidative spoilage and thus to the extension of shelf life. This field accepts terms listed under food preservation process (http://purl.obolibrary.org/obo/FOODON_03470107)_



URI: [MIXS:0001135](https://w3id.org/mixs/0001135)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
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
| food slow freezing [FOODON:03470128] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03470107 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_preserv_proc
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03470107
description: The methods contributing to the prevention or retardation of microbial,
  enzymatic or oxidative spoilage and thus to the extension of shelf life. This field
  accepts terms listed under food preservation process (http://purl.obolibrary.org/obo/FOODON_03470107)
title: food preservation process
notes:
- food
- process
examples:
- value: food slow freezing [FOODON:03470128]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001135
multivalued: true
alias: food_preserv_proc
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>