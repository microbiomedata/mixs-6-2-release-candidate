# Slot: food_harvest_proc


_A harvesting process is a process which takes in some food material from an individual or community of plant or animal organisms in a given context and time, and outputs a precursor or consumable food product. This may include a part of an organism or the whole, and may involve killing the organism_



URI: [MIXS:0001133](https://w3id.org/mixs/0001133)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| hand-picked |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_harvest_proc
description: A harvesting process is a process which takes in some food material from
  an individual or community of plant or animal organisms in a given context and time,
  and outputs a precursor or consumable food product. This may include a part of an
  organism or the whole, and may involve killing the organism
title: Food harvesting process
notes:
- food
- process
examples:
- value: hand-picked
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001133
multivalued: true
alias: food_harvest_proc
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>