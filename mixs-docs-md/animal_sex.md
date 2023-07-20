# Slot: animal_sex


_The sex and reproductive status of the food animal_



URI: [MIXS:0001249](https://w3id.org/mixs/0001249)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |







## Properties

* Range: [ANIMALSEXENUM](ANIMALSEXENUM.md)






## Examples

| Value |
| --- |
| castrated male |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: animal_sex
description: The sex and reproductive status of the food animal
title: food animal source sex category
notes:
- animal
- food
- source
examples:
- value: castrated male
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001249
multivalued: false
alias: animal_sex
domain_of:
- FoodAnimalAndAnimalFeed
range: ANIMAL_SEX_ENUM
required: false
recommended: false

```
</details>