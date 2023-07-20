# Slot: host_pulse


_Resting pulse, measured as beats per minute_



URI: [MIXS:0000333](https://w3id.org/mixs/0000333)



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
| 65 beats per minute |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | beats per minute |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_pulse
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: beats per minute
description: Resting pulse, measured as beats per minute
title: host pulse
notes:
- host
- host.
examples:
- value: 65 beats per minute
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000333
multivalued: false
alias: host_pulse
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