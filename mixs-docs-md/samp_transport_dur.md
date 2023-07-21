# Slot: samp_transport_dur


_The duration of time from when the sample was collected until processed. Indicate the duration for which the sample was stored written in ISO 8601 format_



URI: [MIXS:0001231](https://w3id.org/mixs/0001231)



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
| P10D |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | days |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_transport_dur
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: days
description: The duration of time from when the sample was collected until processed.
  Indicate the duration for which the sample was stored written in ISO 8601 format
title: sample transport duration
notes:
- duration
- period
- sample
- transport
examples:
- value: P10D
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001231
multivalued: false
alias: samp_transport_dur
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