# Slot: trna_ext_software


_Tools used for tRNA identification_



URI: [MIXS:0000068](https://w3id.org/mixs/0000068)



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
| infernal;v2;default parameters |

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
name: trna_ext_software
annotations:
  Expected_value:
    tag: Expected_value
    value: names and versions of software(s), parameters used
description: Tools used for tRNA identification
title: tRNA extraction software
notes:
- software
examples:
- value: infernal;v2;default parameters
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000068
multivalued: false
alias: trna_ext_software
domain_of:
- Mimag
- Misag
- Miuvig
range: string

```
</details>