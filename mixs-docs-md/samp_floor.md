# Slot: samp_floor


_The floor of the building, where the sampling room is located_



URI: [MIXS:0000828](https://w3id.org/mixs/0000828)



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
| 4th floor |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_floor
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: The floor of the building, where the sampling room is located
title: sampling floor
notes:
- floor
examples:
- value: 4th floor
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[1st floor|2nd floor|{integer} floor|basement|lobby]'
slot_uri: MIXS:0000828
multivalued: false
alias: samp_floor
domain_of:
- BuiltEnvironment
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>