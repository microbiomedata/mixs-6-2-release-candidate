# Slot: animal_am_use


_The prescribed intended use of or the condition treated by the antimicrobial given to the food animal by any route of administration_



URI: [MIXS:0001247](https://w3id.org/mixs/0001247)



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
| shipping fever |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: animal_am_use
description: The prescribed intended use of or the condition treated by the antimicrobial
  given to the food animal by any route of administration
title: food animal antimicrobial intended use
notes:
- animal
- antimicrobial
- food
- use
examples:
- value: shipping fever
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001247
multivalued: false
alias: animal_am_use
domain_of:
- FoodAnimalAndAnimalFeed
range: string
required: false
recommended: false

```
</details>