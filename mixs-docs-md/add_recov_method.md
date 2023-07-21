# Slot: add_recov_method


_Additional (i.e. Secondary, tertiary, etc.) recovery methods deployed for increase of hydrocarbon recovery from resource and start date for each one of them. If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0001009](https://w3id.org/mixs/0001009)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True






## Examples

| Value |
| --- |
| Polymer Addition;2018-06-21T14:30Z |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration;timestamp |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: add_recov_method
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration;timestamp
description: Additional (i.e. Secondary, tertiary, etc.) recovery methods deployed
  for increase of hydrocarbon recovery from resource and start date for each one of
  them. If "other" is specified, please propose entry in "additional info" field
title: secondary and tertiary recovery methods and start date
notes:
- date
- method
- recover
- secondary
- start
examples:
- value: Polymer Addition;2018-06-21T14:30Z
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[Water Injection|Dump Flood|Gas Injection|Wag Immiscible Injection|Polymer
  Addition|Surfactant Addition|Not Applicable|other];{timestamp}'
slot_uri: MIXS:0001009
multivalued: false
alias: add_recov_method
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
required: true

```
</details>