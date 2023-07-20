# Slot: soil_porosity


_Porosity of soil or deposited sediment is volume of voids divided by the total volume of sample_



URI: [MIXS:0001162](https://w3id.org/mixs/0001162)



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
| 0.2 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | percent porosity || Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: soil_porosity
annotations:
  Expected_value:
    tag: Expected_value
    value: percent porosity
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: Porosity of soil or deposited sediment is volume of voids divided by
  the total volume of sample
title: soil sediment porosity
notes:
- porosity
- sediment
- soil
examples:
- value: '0.2'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{percentage}'
slot_uri: MIXS:0001162
multivalued: false
alias: soil_porosity
domain_of:
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>