# Slot: host_body_mass_index


_Body mass index, calculated as weight/(height)squared_



URI: [MIXS:0000317](https://w3id.org/mixs/0000317)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |
[HumanGut](HumanGut.md) |  |  no  |
[HumanOral](HumanOral.md) |  |  no  |
[HumanSkin](HumanSkin.md) |  |  no  |
[HumanVaginal](HumanVaginal.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 22 kilogram per square meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | kilogram per square meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_body_mass_index
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: kilogram per square meter
description: Body mass index, calculated as weight/(height)squared
title: host body-mass index
notes:
- host
- host.
examples:
- value: 22 kilogram per square meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000317
multivalued: false
alias: host_body_mass_index
domain_of:
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>