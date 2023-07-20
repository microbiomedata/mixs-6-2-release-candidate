# Slot: trnas


_The total number of tRNAs identified from the SAG or MAG_



URI: [MIXS:0000067](https://w3id.org/mixs/0000067)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 18 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | value from 0-21 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: trnas
annotations:
  Expected_value:
    tag: Expected_value
    value: value from 0-21
description: The total number of tRNAs identified from the SAG or MAG
title: number of standard tRNAs extracted
notes:
- number
examples:
- value: '18'
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{integer}'
slot_uri: MIXS:0000067
multivalued: false
alias: trnas
domain_of:
- Mimag
- Misag
- Miuvig
range: string

```
</details>