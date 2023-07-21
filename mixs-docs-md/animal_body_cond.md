# Slot: animal_body_cond


_Body condition scoring is a production management tool used to evaluate overall health and nutritional needs of a food animal. Because there are different scoring systems, this field is restricted to three categories_



URI: [MIXS:0001248](https://w3id.org/mixs/0001248)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |







## Properties

* Range: [ANIMALBODYCONDENUM](ANIMALBODYCONDENUM.md)






## Examples

| Value |
| --- |
| under conditioned |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: animal_body_cond
description: Body condition scoring is a production management tool used to evaluate
  overall health and nutritional needs of a food animal. Because there are different
  scoring systems, this field is restricted to three categories
title: food animal body condition
notes:
- animal
- body
- condition
- food
examples:
- value: under conditioned
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001248
multivalued: false
alias: animal_body_cond
domain_of:
- FoodAnimalAndAnimalFeed
range: ANIMAL_BODY_COND_ENUM
required: false
recommended: false

```
</details>