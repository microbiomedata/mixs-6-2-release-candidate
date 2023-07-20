# Slot: animal_am


_The name(s) (generic or brand) of the antimicrobial(s) given to the food animal within the last 30 days_



URI: [MIXS:0001243](https://w3id.org/mixs/0001243)



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
| tetracycline |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: animal_am
description: The name(s) (generic or brand) of the antimicrobial(s) given to the food
  animal within the last 30 days
title: food animal antimicrobial
notes:
- animal
- antimicrobial
- food
examples:
- value: tetracycline
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001243
multivalued: false
alias: animal_am
domain_of:
- FoodAnimalAndAnimalFeed
range: string
required: false
recommended: false

```
</details>