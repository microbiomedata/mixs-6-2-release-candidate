# Slot: room_dim


_The length, width and height of sampling room_



URI: [MIXS:0000192](https://w3id.org/mixs/0000192)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 4 meter x 4 meter x 4 meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value || Preferred_unit | meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: room_dim
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: meter
description: The length, width and height of sampling room
title: room dimensions
notes:
- dimensions
- room
examples:
- value: 4 meter x 4 meter x 4 meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{integer} {unit} x {integer} {unit} x {integer} {unit}'
slot_uri: MIXS:0000192
multivalued: false
alias: room_dim
domain_of:
- BuiltEnvironment
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>