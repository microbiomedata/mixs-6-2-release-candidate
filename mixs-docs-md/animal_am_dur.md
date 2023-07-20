# Slot: animal_am_dur


_The duration of time (days) that the antimicrobial was administered to the food animal_



URI: [MIXS:0001244](https://w3id.org/mixs/0001244)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 3 days |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | value |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: animal_am_dur
annotations:
  Expected_value:
    tag: Expected_value
    value: value
description: The duration of time (days) that the antimicrobial was administered to
  the food animal
title: food animal antimicrobial duration
notes:
- animal
- antimicrobial
- duration
- food
- period
examples:
- value: 3 days
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {day}'
slot_uri: MIXS:0001244
multivalued: false
alias: animal_am_dur
domain_of:
- FoodAnimalAndAnimalFeed
range: string
required: false
recommended: false

```
</details>