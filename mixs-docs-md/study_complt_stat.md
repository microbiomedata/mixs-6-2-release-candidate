# Slot: study_complt_stat


_Specification of study completion status, if no the reason should be specified_



URI: [MIXS:0000898](https://w3id.org/mixs/0000898)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| no;non-compliance |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | YES or NO due to (1)adverse event (2) non-compliance (3) lost to follow up (4)other-specify |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: study_complt_stat
annotations:
  Expected_value:
    tag: Expected_value
    value: YES or NO due to (1)adverse event (2) non-compliance (3) lost to follow
      up (4)other-specify
description: Specification of study completion status, if no the reason should be
  specified
title: study completion status
notes:
- status
examples:
- value: no;non-compliance
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{boolean};[adverse event|non-compliance|lost to follow up|other-specify]'
slot_uri: MIXS:0000898
multivalued: false
alias: study_complt_stat
domain_of:
- HumanAssociated
range: string
required: false
recommended: false

```
</details>