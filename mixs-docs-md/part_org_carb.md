# Slot: part_org_carb


_Concentration of particulate organic carbon_



URI: [MIXS:0000515](https://w3id.org/mixs/0000515)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Water](Water.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 1.92 micromole per liter |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: part_org_carb
description: Concentration of particulate organic carbon
title: particulate organic carbon
notes:
- carbon
- organic
- particle
- particulate
examples:
- value: 1.92 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000515
multivalued: false
alias: part_org_carb
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