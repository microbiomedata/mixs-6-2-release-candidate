# Slot: avg_dew_point


_The average of dew point measures taken at the beginning of every hour over a 24 hour period on the sampling day_



URI: [MIXS:0000141](https://w3id.org/mixs/0000141)



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
| 25.5 degree Celsius |

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
name: avg_dew_point
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: The average of dew point measures taken at the beginning of every hour
  over a 24 hour period on the sampling day
title: average dew point
notes:
- average
examples:
- value: 25.5 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000141
multivalued: false
alias: avg_dew_point
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>