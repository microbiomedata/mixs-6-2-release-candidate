# Slot: magnesium


_Concentration of magnesium in the sample_



URI: [MIXS:0000431](https://w3id.org/mixs/0000431)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 52.8 micromole per kilogram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | mole per liter, milligram per liter, parts per million, micromole per kilogram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: magnesium
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: mole per liter, milligram per liter, parts per million, micromole per kilogram
description: Concentration of magnesium in the sample
title: magnesium
examples:
- value: 52.8 micromole per kilogram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000431
multivalued: false
alias: magnesium
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
- MicrobialMatBiofilm
- Sediment
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>