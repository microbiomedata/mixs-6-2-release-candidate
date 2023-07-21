# Slot: org_nitro


_Concentration of organic nitrogen_



URI: [MIXS:0000205](https://w3id.org/mixs/0000205)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[Water](Water.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 4 micromole per liter |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: org_nitro
description: Concentration of organic nitrogen
title: organic nitrogen
notes:
- nitrogen
- organic
examples:
- value: 4 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000205
multivalued: false
alias: org_nitro
domain_of:
- MicrobialMatBiofilm
- MiscellaneousNaturalOrArtificialEnvironment
- Sediment
- Soil
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>