# Slot: cons_qty_purchased


_The quantity of food purchased by consumer_



URI: [MIXS:0001198](https://w3id.org/mixs/0001198)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[1-9][0-9]* \S.*\S+$`






## Examples

| Value |
| --- |
| 5 cans |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: cons_qty_purchased
description: The quantity of food purchased by consumer
title: quantity purchased
notes:
- quantity
examples:
- value: 5 cans
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001198
multivalued: false
alias: cons_qty_purchased
domain_of:
- FoodAnimalAndAnimalFeed
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^[1-9][0-9]* \S.*\S+$

```
</details>