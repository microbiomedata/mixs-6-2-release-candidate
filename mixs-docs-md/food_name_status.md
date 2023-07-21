# Slot: food_name_status


_A datum indicating that use of a food product name is regulated in some legal jurisdiction. This field accepts terms listed under food product name legal status (http://purl.obolibrary.org/obo/FOODON_03530087)_



URI: [MIXS:0001206](https://w3id.org/mixs/0001206)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| protected geographic indication [FOODON:03530256] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_name_status
description: A datum indicating that use of a food product name is regulated in some
  legal jurisdiction. This field accepts terms listed under food product name legal
  status (http://purl.obolibrary.org/obo/FOODON_03530087)
title: food product name legal status
notes:
- food
- product
- status
examples:
- value: protected geographic indication [FOODON:03530256]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001206
multivalued: false
alias: food_name_status
domain_of:
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>