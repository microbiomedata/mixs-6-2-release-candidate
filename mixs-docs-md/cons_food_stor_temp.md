# Slot: cons_food_stor_temp


_Temperature at which food commodity was stored by the consumer, prior to onset of illness or sample collection_



URI: [MIXS:0001196](https://w3id.org/mixs/0001196)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 4 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | text or measurement value || Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: cons_food_stor_temp
annotations:
  Expected_value:
    tag: Expected_value
    value: text or measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: Temperature at which food commodity was stored by the consumer, prior
  to onset of illness or sample collection
title: food stored by consumer (storage temperature)
notes:
- consumer
- food
- storage
- temperature
examples:
- value: 4 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} {unit}|{text}'
slot_uri: MIXS:0001196
multivalued: false
alias: cons_food_stor_temp
domain_of:
- FoodAnimalAndAnimalFeed
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>