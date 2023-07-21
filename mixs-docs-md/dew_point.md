# Slot: dew_point


_The temperature to which a given parcel of humid air must be cooled, at constant barometric pressure, for water vapor to condense into water_



URI: [MIXS:0000129](https://w3id.org/mixs/0000129)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 22 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: dew_point
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: The temperature to which a given parcel of humid air must be cooled,
  at constant barometric pressure, for water vapor to condense into water
title: dew point
examples:
- value: 22 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000129
multivalued: false
alias: dew_point
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>