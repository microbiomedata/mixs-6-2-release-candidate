# Slot: abs_air_humidity


_Actual mass of water vapor - mh20 - present in the air water vapor mixture_



URI: [MIXS:0000122](https://w3id.org/mixs/0000122)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 9 gram per gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram per gram, kilogram per kilogram, kilogram, pound |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: abs_air_humidity
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram per gram, kilogram per kilogram, kilogram, pound
description: Actual mass of water vapor - mh20 - present in the air water vapor mixture
title: absolute air humidity
notes:
- absolute
- air
- humidity
examples:
- value: 9 gram per gram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000122
multivalued: false
alias: abs_air_humidity
domain_of:
- BuiltEnvironment
range: string
required: true
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>