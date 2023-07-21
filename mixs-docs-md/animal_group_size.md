# Slot: animal_group_size


_The number of food animals of the same species that are maintained together as a unit, i.e. a herd or flock_



URI: [MIXS:0001129](https://w3id.org/mixs/0001129)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [Integer](Integer.md)






## Examples

| Value |
| --- |
| 80 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: animal_group_size
description: The number of food animals of the same species that are maintained together
  as a unit, i.e. a herd or flock
title: food animal group size
notes:
- animal
- food
- size
examples:
- value: '80'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001129
multivalued: false
alias: animal_group_size
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
range: integer
required: false
recommended: false

```
</details>