# Slot: timepoint


_Time point at which a sample or observation is made or taken from a biomaterial as measured from some reference point. Indicate the timepoint written in ISO 8601 format_



URI: [MIXS:0001173](https://w3id.org/mixs/0001173)



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


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: timepoint
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: hours or days
description: Time point at which a sample or observation is made or taken from a biomaterial
  as measured from some reference point. Indicate the timepoint written in ISO 8601
  format
title: timepoint
notes:
- time
examples:
- value: PT24H
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001173
multivalued: false
alias: timepoint
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$

```
</details>