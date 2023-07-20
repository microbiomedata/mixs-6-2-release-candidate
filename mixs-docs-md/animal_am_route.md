# Slot: animal_am_route


_The route by which the antimicrobial is adminstered into the body of the food animal_



URI: [MIXS:0001246](https://w3id.org/mixs/0001246)



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
| oral-feed |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: animal_am_route
description: The route by which the antimicrobial is adminstered into the body of
  the food animal
title: food animal antimicrobial route of administration
notes:
- administration
- animal
- antimicrobial
- food
- route
examples:
- value: oral-feed
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001246
multivalued: false
alias: animal_am_route
domain_of:
- FoodAnimalAndAnimalFeed
range: string
required: false
recommended: false

```
</details>