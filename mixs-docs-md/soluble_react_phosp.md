# Slot: soluble_react_phosp


_Concentration of soluble reactive phosphorus_



URI: [MIXS:0000738](https://w3id.org/mixs/0000738)



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
| 0.1 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micromole per liter, milligram per liter, parts per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: soluble_react_phosp
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter, milligram per liter, parts per million
description: Concentration of soluble reactive phosphorus
title: soluble reactive phosphorus
notes:
- phosphorus
- soluble
examples:
- value: 0.1 milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000738
multivalued: false
alias: soluble_react_phosp
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>