# Slot: n_alkanes


_Concentration of n-alkanes; can include multiple n-alkanes_



URI: [MIXS:0000503](https://w3id.org/mixs/0000503)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Water](Water.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| n-hexadecane;100 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | n-alkane name;measurement value |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: n_alkanes
annotations:
  Expected_value:
    tag: Expected_value
    value: n-alkane name;measurement value
description: Concentration of n-alkanes; can include multiple n-alkanes
title: n-alkanes
examples:
- value: n-hexadecane;100 milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000503
multivalued: true
alias: n_alkanes
domain_of:
- MicrobialMatBiofilm
- Sediment
- Water
range: string
required: false
recommended: false

```
</details>