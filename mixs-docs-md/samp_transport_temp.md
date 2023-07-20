# Slot: samp_transport_temp


_Temperature at which sample was transported, e.g. -20 or 4 degree Celsius_



URI: [MIXS:0001232](https://w3id.org/mixs/0001232)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 4 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | text or measurement value || Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_transport_temp
annotations:
  Expected_value:
    tag: Expected_value
    value: text or measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: Temperature at which sample was transported, e.g. -20 or 4 degree Celsius
title: sample transport temperature
notes:
- sample
- temperature
- transport
examples:
- value: 4 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {unit} {text}'
slot_uri: MIXS:0001232
multivalued: false
alias: samp_transport_temp
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>