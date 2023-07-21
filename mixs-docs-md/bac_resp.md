# Slot: bac_resp


_Measurement of bacterial respiration in the water column_



URI: [MIXS:0000684](https://w3id.org/mixs/0000684)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 300 micromole oxygen per liter per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram per cubic meter per day, micromole oxygen per liter per hour |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: bac_resp
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per cubic meter per day, micromole oxygen per liter per hour
description: Measurement of bacterial respiration in the water column
title: bacterial respiration
examples:
- value: 300 micromole oxygen per liter per hour
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000684
multivalued: false
alias: bac_resp
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>