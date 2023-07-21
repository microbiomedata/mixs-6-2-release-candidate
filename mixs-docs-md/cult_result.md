# Slot: cult_result


_Any result of a bacterial culture experiment reported as a binary assessment such as positive/negative, active/inactive_



URI: [MIXS:0001117](https://w3id.org/mixs/0001117)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [CULTRESULTENUM](CULTRESULTENUM.md)






## Examples

| Value |
| --- |
| positive |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: cult_result
description: Any result of a bacterial culture experiment reported as a binary assessment
  such as positive/negative, active/inactive
title: culture result
notes:
- culture
examples:
- value: positive
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001117
multivalued: false
alias: cult_result
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: CULT_RESULT_ENUM
required: false
recommended: false

```
</details>