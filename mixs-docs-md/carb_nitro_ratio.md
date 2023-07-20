# Slot: carb_nitro_ratio


_Ratio of amount or concentrations of carbon to nitrogen_



URI: [MIXS:0000310](https://w3id.org/mixs/0000310)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Water](Water.md) |  |  yes  |







## Properties

* Range: [Float](Float.md)






## Examples

| Value |
| --- |
| 0.417361111 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: carb_nitro_ratio
description: Ratio of amount or concentrations of carbon to nitrogen
title: carbon/nitrogen ratio
notes:
- carbon
- nitrogen
- ratio
examples:
- value: '0.417361111'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000310
alias: carb_nitro_ratio
domain_of:
- MicrobialMatBiofilm
- Sediment
- Water
range: float
required: false
recommended: false

```
</details>