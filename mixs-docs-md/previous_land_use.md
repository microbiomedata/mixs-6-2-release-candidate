# Slot: previous_land_use


_Previous land use and dates_



URI: [MIXS:0000315](https://w3id.org/mixs/0000315)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| fallow; 2018-05-11:T14:30Z |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | land use name;date |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: previous_land_use
annotations:
  Expected_value:
    tag: Expected_value
    value: land use name;date
description: Previous land use and dates
title: history/previous land use
notes:
- history
- land
- use
examples:
- value: fallow; 2018-05-11:T14:30Z
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{timestamp}'
slot_uri: MIXS:0000315
multivalued: false
alias: previous_land_use
domain_of:
- Agriculture
- FoodFarmEnvironment
- Soil
range: string

```
</details>