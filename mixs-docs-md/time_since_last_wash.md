# Slot: time_since_last_wash


_Specification of the time since last wash_



URI: [MIXS:0000943](https://w3id.org/mixs/0000943)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanSkin](HumanSkin.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$`






## Examples

| Value |
| --- |
| P1D |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: time_since_last_wash
description: Specification of the time since last wash
title: time since last wash
notes:
- time
examples:
- value: P1D
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000943
multivalued: false
alias: time_since_last_wash
domain_of:
- HumanSkin
range: string
required: false
recommended: false
pattern: ^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$

```
</details>