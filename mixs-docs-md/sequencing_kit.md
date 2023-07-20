# Slot: sequencing_kit


_Pre-filled, ready-to-use reagent cartridges. Used to produce improved chemistry, cluster density and read length as well as improve quality (Q) scores. Reagent components are encoded to interact with the sequencing system to validate compatibility with user-defined applications. Indicate name of the sequencing kit_



URI: [MIXS:0001155](https://w3id.org/mixs/0001155)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| NextSeq 500/550 High Output Kit v2.5 (75 Cycles) |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | name of sequencing kit used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: sequencing_kit
annotations:
  Expected_value:
    tag: Expected_value
    value: name of sequencing kit used
description: Pre-filled, ready-to-use reagent cartridges. Used to produce improved
  chemistry, cluster density and read length as well as improve quality (Q) scores.
  Reagent components are encoded to interact with the sequencing system to validate
  compatibility with user-defined applications. Indicate name of the sequencing kit
title: sequencing kit
notes:
- kit
examples:
- value: NextSeq 500/550 High Output Kit v2.5 (75 Cycles)
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001155
multivalued: false
alias: sequencing_kit
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