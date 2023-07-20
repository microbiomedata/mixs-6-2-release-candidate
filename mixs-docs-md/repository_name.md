# Slot: repository_name


_The name of the institution where the sample or DNA extract is held or "sample not available" if the sample was used in its entirety for analysis or otherwise not retained_



URI: [MIXS:0001152](https://w3id.org/mixs/0001152)



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
| FDA CFSAN Microbiology Laboratories |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: repository_name
description: The name of the institution where the sample or DNA extract is held or
  "sample not available" if the sample was used in its entirety for analysis or otherwise
  not retained
title: repository name
examples:
- value: FDA CFSAN Microbiology Laboratories
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001152
multivalued: true
alias: repository_name
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