# Slot: sulfide


_Concentration of sulfide in the sample_



URI: [MIXS:0000424](https://w3id.org/mixs/0000424)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  yes  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  yes  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Water](Water.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 2 micromole per liter |

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
name: sulfide
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter, milligram per liter, parts per million
description: Concentration of sulfide in the sample
title: sulfide
notes:
- sulfide
examples:
- value: 2 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000424
multivalued: false
alias: sulfide
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
- MicrobialMatBiofilm
- MiscellaneousNaturalOrArtificialEnvironment
- Sediment
- Water
range: string
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>