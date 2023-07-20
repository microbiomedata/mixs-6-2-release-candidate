# Slot: biomass


_Amount of biomass; should include the name for the part of biomass measured, e.g. Microbial, total. Can include multiple measurements_



URI: [MIXS:0000174](https://w3id.org/mixs/0000174)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  no  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| total;20 gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | biomass type;measurement value || Preferred_unit | ton, kilogram, gram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: biomass
annotations:
  Expected_value:
    tag: Expected_value
    value: biomass type;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: ton, kilogram, gram
description: Amount of biomass; should include the name for the part of biomass measured,
  e.g. Microbial, total. Can include multiple measurements
title: biomass
notes:
- biomass
examples:
- value: total;20 gram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000174
multivalued: true
alias: biomass
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