# Slot: seq_quality_check


_Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to SRA,ENA or DRA_



URI: [MIXS:0000051](https://w3id.org/mixs/0000051)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |







## Properties

* Range: [SEQQUALITYCHECKENUM](SEQQUALITYCHECKENUM.md)






## Examples

| Value |
| --- |
| none |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | none or manually edited |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: seq_quality_check
annotations:
  Expected_value:
    tag: Expected_value
    value: none or manually edited
description: Indicate if the sequence has been called by automatic systems (none)
  or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms).
  Applied only for sequences that are not submitted to SRA,ENA or DRA
title: sequence quality check
notes:
- quality
examples:
- value: none
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000051
multivalued: false
alias: seq_quality_check
domain_of:
- Agriculture
- MimarksC
- MimarksS
range: SEQ_QUALITY_CHECK_ENUM

```
</details>