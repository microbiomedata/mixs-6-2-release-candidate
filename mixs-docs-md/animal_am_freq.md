# Slot: animal_am_freq


_The frequency per day that the antimicrobial was adminstered to the food animal_



URI: [MIXS:0001245](https://w3id.org/mixs/0001245)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |







## Properties

* Range: [Float](Float.md)






## Examples

| Value |
| --- |
| 1.5 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: animal_am_freq
description: The frequency per day that the antimicrobial was adminstered to the food
  animal
title: food animal antimicrobial frequency
notes:
- animal
- antimicrobial
- food
- frequency
examples:
- value: '1.5'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001245
alias: animal_am_freq
domain_of:
- FoodAnimalAndAnimalFeed
range: float
required: false
recommended: false

```
</details>