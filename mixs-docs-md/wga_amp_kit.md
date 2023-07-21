# Slot: wga_amp_kit


_Kit used to amplify genomic DNA in preparation for sequencing_



URI: [MIXS:0000006](https://w3id.org/mixs/0000006)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| qiagen repli-g |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | kit name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: wga_amp_kit
annotations:
  Expected_value:
    tag: Expected_value
    value: kit name
description: Kit used to amplify genomic DNA in preparation for sequencing
title: WGA amplification kit
notes:
- kit
examples:
- value: qiagen repli-g
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000006
multivalued: false
alias: wga_amp_kit
domain_of:
- Misag
- Miuvig
range: string

```
</details>