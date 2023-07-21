# Slot: redox_potential


_Redox potential, measured relative to a hydrogen cell, indicating oxidation or reduction potential_



URI: [MIXS:0000182](https://w3id.org/mixs/0000182)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 300 millivolt |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | millivolt |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: redox_potential
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: millivolt
description: Redox potential, measured relative to a hydrogen cell, indicating oxidation
  or reduction potential
title: redox potential
examples:
- value: 300 millivolt
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000182
multivalued: false
alias: redox_potential
domain_of:
- MicrobialMatBiofilm
- Sediment
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>