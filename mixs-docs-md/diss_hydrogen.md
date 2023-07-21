# Slot: diss_hydrogen


_Concentration of dissolved hydrogen_



URI: [MIXS:0000179](https://w3id.org/mixs/0000179)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  no  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
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
| Preferred_unit | micromole per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: diss_hydrogen
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter
description: Concentration of dissolved hydrogen
title: dissolved hydrogen
notes:
- dissolved
examples:
- value: 0.3 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000179
multivalued: false
alias: diss_hydrogen
domain_of:
- MicrobialMatBiofilm
- MiscellaneousNaturalOrArtificialEnvironment
- Sediment
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>