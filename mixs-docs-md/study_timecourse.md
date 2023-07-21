# Slot: study_timecourse


_For time-course research studies involving samples of the food commodity, indicate the total duration of the time-course study_



URI: [MIXS:0001239](https://w3id.org/mixs/0001239)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 2 days post inoculation |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | dpi |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: study_timecourse
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: dpi
description: For time-course research studies involving samples of the food commodity,
  indicate the total duration of the time-course study
title: time-course duration
notes:
- duration
- period
- time
examples:
- value: 2 days post inoculation
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001239
multivalued: false
alias: study_timecourse
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>