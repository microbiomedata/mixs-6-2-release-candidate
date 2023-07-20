# Slot: area_samp_size


_The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected_



URI: [MIXS:0001255](https://w3id.org/mixs/0001255)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 12 centimeter x 12 centimeter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value || Preferred_unit | centimeter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: area_samp_size
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: centimeter
description: The total amount or size (volume (ml), mass (g) or area (m2) ) of sample
  collected
title: area sampled size
notes:
- area
- sample
- size
examples:
- value: 12 centimeter x 12 centimeter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{integer} {unit} x {integer} {unit}'
slot_uri: MIXS:0001255
multivalued: false
alias: area_samp_size
domain_of:
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>