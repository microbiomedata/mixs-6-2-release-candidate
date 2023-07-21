# Slot: surf_humidity


_Surfaces: water activity as a function of air and material moisture_



URI: [MIXS:0000123](https://w3id.org/mixs/0000123)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [Float](Float.md)

* Recommended: True






## Examples

| Value |
| --- |
| 0.1 |

## Comments

* percent or float?

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: surf_humidity
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: 'Surfaces: water activity as a function of air and material moisture'
title: surface humidity
notes:
- humidity
- surface
comments:
- percent or float?
examples:
- value: '0.1'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000123
alias: surf_humidity
domain_of:
- BuiltEnvironment
range: float
recommended: true

```
</details>