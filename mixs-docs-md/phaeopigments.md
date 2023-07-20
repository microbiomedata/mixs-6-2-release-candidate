# Slot: phaeopigments


_Concentration of phaeopigments; can include multiple phaeopigments_



URI: [MIXS:0000180](https://w3id.org/mixs/0000180)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 2.5 milligram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | phaeopigment name;measurement value || Preferred_unit | milligram per cubic meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: phaeopigments
annotations:
  Expected_value:
    tag: Expected_value
    value: phaeopigment name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per cubic meter
description: Concentration of phaeopigments; can include multiple phaeopigments
title: phaeopigments
examples:
- value: 2.5 milligram per cubic meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000180
multivalued: true
alias: phaeopigments
domain_of:
- MicrobialMatBiofilm
- Sediment
- Water
range: string
required: false
recommended: false

```
</details>