# Slot: study_inc_dur


_Sample incubation duration if unpublished or unvalidated method is used. Indicate the timepoint written in ISO 8601 format_



URI: [MIXS:0001237](https://w3id.org/mixs/0001237)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$`






## Examples

| Value |
| --- |
| PT24H |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | hours or days |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: study_inc_dur
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: hours or days
description: Sample incubation duration if unpublished or unvalidated method is used.
  Indicate the timepoint written in ISO 8601 format
title: study incubation duration
notes:
- duration
- incubation
- period
examples:
- value: PT24H
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001237
multivalued: false
alias: study_inc_dur
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$

```
</details>