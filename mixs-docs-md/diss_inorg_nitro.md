# Slot: diss_inorg_nitro


_Concentration of dissolved inorganic nitrogen_



URI: [MIXS:0000698](https://w3id.org/mixs/0000698)



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
| 761 micromole per liter |

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
name: diss_inorg_nitro
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per liter, micromole per liter
description: Concentration of dissolved inorganic nitrogen
title: dissolved inorganic nitrogen
notes:
- dissolved
- inorganic
- nitrogen
examples:
- value: 761 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000698
multivalued: false
alias: diss_inorg_nitro
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>