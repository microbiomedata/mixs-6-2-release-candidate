# Slot: detec_type


_Type of UViG detection_



URI: [MIXS:0000084](https://w3id.org/mixs/0000084)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| independent sequence (UViG) |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: detec_type
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: Type of UViG detection
title: detection type
notes:
- type
examples:
- value: independent sequence (UViG)
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[independent sequence (UViG)|provirus (UpViG)]'
slot_uri: MIXS:0000084
multivalued: false
alias: detec_type
domain_of:
- Miuvig
range: string

```
</details>