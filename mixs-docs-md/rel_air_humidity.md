# Slot: rel_air_humidity


_Partial vapor and air pressure, density of the vapor and air, or by the actual mass of the vapor and air_



URI: [MIXS:0000121](https://w3id.org/mixs/0000121)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [Float](Float.md)

* Required: True






## Examples

| Value |
| --- |
| 0.8 |

## Comments

* percent or float?

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: rel_air_humidity
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: Partial vapor and air pressure, density of the vapor and air, or by the
  actual mass of the vapor and air
title: relative air humidity
notes:
- air
- humidity
- relative
comments:
- percent or float?
examples:
- value: '0.8'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000121
alias: rel_air_humidity
domain_of:
- BuiltEnvironment
range: float
required: true

```
</details>