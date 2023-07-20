# Slot: cons_food_stor_dur


_The storage duration of the food commodity by the consumer, prior to onset of illness or sample collection.  Indicate the timepoint written in ISO 8601 format_



URI: [MIXS:0001195](https://w3id.org/mixs/0001195)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$`






## Examples

| Value |
| --- |
| P5D |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | hours or days |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: cons_food_stor_dur
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: hours or days
description: The storage duration of the food commodity by the consumer, prior to
  onset of illness or sample collection.  Indicate the timepoint written in ISO 8601
  format
title: food stored by consumer (storage duration)
notes:
- consumer
- duration)
- food
- storage
examples:
- value: P5D
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001195
multivalued: false
alias: cons_food_stor_dur
domain_of:
- FoodAnimalAndAnimalFeed
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$

```
</details>