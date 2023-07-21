# Slot: food_clean_proc


_The process of cleaning food to separate other environmental materials from the food source. Multiple terms can be separated by pipes_



URI: [MIXS:0001182](https://w3id.org/mixs/0001182)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [FOODCLEANPROCENUM](FOODCLEANPROCENUM.md)






## Examples

| Value |
| --- |
| rinsed with water |
| scrubbed with brush |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_clean_proc
description: The process of cleaning food to separate other environmental materials
  from the food source. Multiple terms can be separated by pipes
title: food cleaning process
notes:
- food
- process
examples:
- value: rinsed with water
  description: was rinsed with water|scrubbed with brush
- value: scrubbed with brush
  description: was rinsed with water|scrubbed with brush
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001182
alias: food_clean_proc
domain_of:
- FoodFarmEnvironment
range: FOOD_CLEAN_PROC_ENUM
required: false
recommended: false

```
</details>