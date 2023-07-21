# Slot: food_trace_list


_The FDA is proposing to establish additional traceability recordkeeping requirements (beyond what is already required in existing regulations) for persons who manufacture, process, pack, or hold foods the Agency has designated for inclusion on the Food Traceability List. The Food Traceability List (FTL) identifies the foods for which the additional traceability records described in the proposed rule would be required. The term Food Traceability List (FTL) refers not only to the foods specifically listed (https://www.fda.gov/media/142303/download), but also to any foods that contain listed foods as ingredients_



URI: [MIXS:0001214](https://w3id.org/mixs/0001214)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [FOODTRACELISTENUM](FOODTRACELISTENUM.md)






## Examples

| Value |
| --- |
| tropical tree fruits |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_trace_list
description: The FDA is proposing to establish additional traceability recordkeeping
  requirements (beyond what is already required in existing regulations) for persons
  who manufacture, process, pack, or hold foods the Agency has designated for inclusion
  on the Food Traceability List. The Food Traceability List (FTL) identifies the foods
  for which the additional traceability records described in the proposed rule would
  be required. The term Food Traceability List (FTL) refers not only to the foods
  specifically listed (https://www.fda.gov/media/142303/download), but also to any
  foods that contain listed foods as ingredients
title: food traceability list category
notes:
- food
examples:
- value: tropical tree fruits
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001214
multivalued: false
alias: food_trace_list
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: FOOD_TRACE_LIST_ENUM
required: false
recommended: false

```
</details>