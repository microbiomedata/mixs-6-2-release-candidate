# Slot: x16s_recover_software


_Tools used for 16S rRNA gene extraction_



URI: [MIXS:0000066](https://w3id.org/mixs/0000066)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| rambl;v2;default parameters |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | names and versions of software(s), parameters used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: x16s_recover_software
annotations:
  Expected_value:
    tag: Expected_value
    value: names and versions of software(s), parameters used
description: Tools used for 16S rRNA gene extraction
title: 16S recovery software
notes:
- recover
- software
examples:
- value: rambl;v2;default parameters
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000066
multivalued: false
alias: x16s_recover_software
domain_of:
- Mimag
- Misag
range: string

```
</details>