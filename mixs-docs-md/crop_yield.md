# Slot: crop_yield


_Amount of crop produced per unit or area of land_



URI: [MIXS:0001116](https://w3id.org/mixs/0001116)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 570 kilogram per metre square |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | kilogram per metre square |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: crop_yield
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: kilogram per metre square
description: Amount of crop produced per unit or area of land
title: crop yield
notes:
- crop
examples:
- value: 570 kilogram per metre square
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001116
multivalued: false
alias: crop_yield
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>