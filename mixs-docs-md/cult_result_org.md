# Slot: cult_result_org


_Taxonomic information about the cultured organism(s)_



URI: [MIXS:0001118](https://w3id.org/mixs/0001118)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Listeria monocytogenes [NCIT:C86502] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C14250 or NCBI taxid |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: cult_result_org
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or NCBI taxid
description: Taxonomic information about the cultured organism(s)
title: culture result organism
notes:
- culture
- organism
examples:
- value: Listeria monocytogenes [NCIT:C86502]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001118
multivalued: true
alias: cult_result_org
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>