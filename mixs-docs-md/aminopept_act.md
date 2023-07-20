# Slot: aminopept_act


_Measurement of aminopeptidase activity_



URI: [MIXS:0000172](https://w3id.org/mixs/0000172)



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
| 0.269 mole per liter per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | mole per liter per hour |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: aminopept_act
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: mole per liter per hour
description: Measurement of aminopeptidase activity
title: aminopeptidase activity
examples:
- value: 0.269 mole per liter per hour
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000172
multivalued: false
alias: aminopept_act
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