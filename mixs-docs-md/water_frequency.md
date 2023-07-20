# Slot: water_frequency


_Number of water delivery events within a given period of time_



URI: [MIXS:0001174](https://w3id.org/mixs/0001174)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 2 per day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | rate || Preferred_unit | per day, per week, per month |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: water_frequency
annotations:
  Expected_value:
    tag: Expected_value
    value: rate
  Preferred_unit:
    tag: Preferred_unit
    value: per day, per week, per month
description: Number of water delivery events within a given period of time
title: water delivery frequency
notes:
- delivery
- frequency
- water
examples:
- value: 2 per day
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float}{unit}'
slot_uri: MIXS:0001174
multivalued: false
alias: water_frequency
domain_of:
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>