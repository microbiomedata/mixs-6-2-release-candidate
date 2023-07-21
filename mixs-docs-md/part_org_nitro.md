# Slot: part_org_nitro


_Concentration of particulate organic nitrogen_



URI: [MIXS:0000719](https://w3id.org/mixs/0000719)



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
| 0.3 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | microgram per liter, micromole per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: part_org_nitro
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per liter, micromole per liter
description: Concentration of particulate organic nitrogen
title: particulate organic nitrogen
notes:
- nitrogen
- organic
- particle
- particulate
examples:
- value: 0.3 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000719
multivalued: false
alias: part_org_nitro
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>