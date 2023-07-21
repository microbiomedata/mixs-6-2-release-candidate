# Slot: water_current


_Measurement of magnitude and direction of flow within a fluid_



URI: [MIXS:0000203](https://w3id.org/mixs/0000203)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 10 cubic meter per second |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | cubic meter per second, knots |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: water_current
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: cubic meter per second, knots
description: Measurement of magnitude and direction of flow within a fluid
title: water current
notes:
- water
examples:
- value: 10 cubic meter per second
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000203
multivalued: false
alias: water_current
domain_of:
- MiscellaneousNaturalOrArtificialEnvironment
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>