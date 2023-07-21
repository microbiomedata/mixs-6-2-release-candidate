# Slot: solar_irradiance


_The amount of solar energy that arrives at a specific area of a surface during a specific time interval_



URI: [MIXS:0000112](https://w3id.org/mixs/0000112)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[Air](Air.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 1.36 kilowatts per square meter per day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | kilowatts per square meter per day, ergs per square centimeter per second |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: solar_irradiance
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: kilowatts per square meter per day, ergs per square centimeter per second
description: The amount of solar energy that arrives at a specific area of a surface
  during a specific time interval
title: mean seasonal solar irradiance
notes:
- mean
- season
examples:
- value: 1.36 kilowatts per square meter per day
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000112
multivalued: true
alias: solar_irradiance
domain_of:
- Agriculture
- Air
- FoodFarmEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>