# Slot: mean_peak_frict_vel


_Measurement of mean peak friction velocity_



URI: [MIXS:0000502](https://w3id.org/mixs/0000502)



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
| 1 meter per second |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | meter per second |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: mean_peak_frict_vel
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: meter per second
description: Measurement of mean peak friction velocity
title: mean peak friction velocity
notes:
- mean
- peak
- velocity
examples:
- value: 1 meter per second
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000502
multivalued: false
alias: mean_peak_frict_vel
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