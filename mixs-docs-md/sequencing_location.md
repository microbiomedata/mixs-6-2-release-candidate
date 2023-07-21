# Slot: sequencing_location


_The location the sequencing run was performed. Indicate the name of the lab or core facility where samples were sequenced_



URI: [MIXS:0001156](https://w3id.org/mixs/0001156)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| University of Maryland Genomics Resource Center |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sequencing_location
description: The location the sequencing run was performed. Indicate the name of the
  lab or core facility where samples were sequenced
title: sequencing location
notes:
- location
examples:
- value: University of Maryland Genomics Resource Center
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001156
multivalued: false
alias: sequencing_location
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>