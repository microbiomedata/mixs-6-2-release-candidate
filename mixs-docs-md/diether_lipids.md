# Slot: diether_lipids


_Concentration of diether lipids; can include multiple types of diether lipids_



URI: [MIXS:0000178](https://w3id.org/mixs/0000178)



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
| 0.2 nanogram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | diether lipid name;measurement value || Preferred_unit | nanogram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: diether_lipids
annotations:
  Expected_value:
    tag: Expected_value
    value: diether lipid name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: nanogram per liter
description: Concentration of diether lipids; can include multiple types of diether
  lipids
title: diether lipids
examples:
- value: 0.2 nanogram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000178
multivalued: true
alias: diether_lipids
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