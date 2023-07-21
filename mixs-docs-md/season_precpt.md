# Slot: season_precpt


_The average of all seasonal precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps_



URI: [MIXS:0000645](https://w3id.org/mixs/0000645)



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

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 75 millimeters |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | millimeter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: season_precpt
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: millimeter
description: The average of all seasonal precipitation values known, or an estimated
  equivalent value derived by such methods as regional indexes or Isohyetal maps
title: mean seasonal precipitation
notes:
- mean
- season
examples:
- value: 75 millimeters
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000645
alias: season_precpt
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