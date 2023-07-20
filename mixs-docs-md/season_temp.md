# Slot: season_temp


_Mean seasonal temperature_



URI: [MIXS:0000643](https://w3id.org/mixs/0000643)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[Soil](Soil.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 18 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: season_temp
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: Mean seasonal temperature
title: mean seasonal temperature
notes:
- mean
- season
- temperature
examples:
- value: 18 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000643
multivalued: false
alias: season_temp
domain_of:
- Agriculture
- FoodFarmEnvironment
- Soil
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>