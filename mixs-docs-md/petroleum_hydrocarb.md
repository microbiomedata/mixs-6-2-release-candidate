# Slot: petroleum_hydrocarb


_Concentration of petroleum hydrocarbon_



URI: [MIXS:0000516](https://w3id.org/mixs/0000516)



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
| 0.05 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micromole per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: petroleum_hydrocarb
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter
description: Concentration of petroleum hydrocarbon
title: petroleum hydrocarbon
notes:
- hydrocarbon
- petroleum
examples:
- value: 0.05 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000516
multivalued: false
alias: petroleum_hydrocarb
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