# Slot: surf_moisture


_Water held on a surface_



URI: [MIXS:0000128](https://w3id.org/mixs/0000128)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 0.01 gram per square meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | parts per million, gram per cubic meter, gram per square meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: surf_moisture
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: parts per million, gram per cubic meter, gram per square meter
description: Water held on a surface
title: surface moisture
notes:
- moisture
- surface
examples:
- value: 0.01 gram per square meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000128
multivalued: false
alias: surf_moisture
domain_of:
- BuiltEnvironment
range: string
recommended: true
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>