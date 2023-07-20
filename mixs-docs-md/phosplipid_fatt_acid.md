# Slot: phosplipid_fatt_acid


_Concentration of phospholipid fatty acids; can include multiple values_



URI: [MIXS:0000181](https://w3id.org/mixs/0000181)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Water](Water.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 2.98 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | phospholipid fatty acid name;measurement value |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: phosplipid_fatt_acid
annotations:
  Expected_value:
    tag: Expected_value
    value: phospholipid fatty acid name;measurement value
description: Concentration of phospholipid fatty acids; can include multiple values
title: phospholipid fatty acid
examples:
- value: 2.98 milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000181
multivalued: true
alias: phosplipid_fatt_acid
domain_of:
- MicrobialMatBiofilm
- MiscellaneousNaturalOrArtificialEnvironment
- Sediment
- Water
range: string
required: false
recommended: false

```
</details>