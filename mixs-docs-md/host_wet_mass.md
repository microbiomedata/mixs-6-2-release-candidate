# Slot: host_wet_mass


_Measurement of wet mass_



URI: [MIXS:0000567](https://w3id.org/mixs/0000567)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 1500 gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | kilogram, gram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_wet_mass
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: kilogram, gram
description: Measurement of wet mass
title: host wet mass
notes:
- host
- host.
- mass
- wet
examples:
- value: 1500 gram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000567
multivalued: false
alias: host_wet_mass
domain_of:
- PlantAssociated
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>