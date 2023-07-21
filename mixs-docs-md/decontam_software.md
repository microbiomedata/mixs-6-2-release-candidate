# Slot: decontam_software


_Tool(s) used in contamination screening_



URI: [MIXS:0000074](https://w3id.org/mixs/0000074)



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
| anvi'o |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: decontam_software
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: Tool(s) used in contamination screening
title: decontamination software
notes:
- software
examples:
- value: anvi'o
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[checkm/refinem|anvi''o|prodege|bbtools:decontaminate.sh|acdc|combination]'
slot_uri: MIXS:0000074
multivalued: false
alias: decontam_software
domain_of:
- Mimag
- Misag
range: string

```
</details>