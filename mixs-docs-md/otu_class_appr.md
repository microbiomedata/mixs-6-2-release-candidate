# Slot: otu_class_appr


_Cutoffs and approach used when clustering species-level OTUs. Note that results from standard 95% ANI / 85% AF clustering should be provided alongside OTUS defined from another set of thresholds, even if the latter are the ones primarily used during the analysis_



URI: [MIXS:0000085](https://w3id.org/mixs/0000085)



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
| 95% ANI;85% AF; greedy incremental clustering |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | cutoffs and method used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: otu_class_appr
annotations:
  Expected_value:
    tag: Expected_value
    value: cutoffs and method used
description: Cutoffs and approach used when clustering species-level OTUs. Note that
  results from standard 95% ANI / 85% AF clustering should be provided alongside OTUS
  defined from another set of thresholds, even if the latter are the ones primarily
  used during the analysis
title: OTU classification approach
notes:
- classification
- otu
examples:
- value: 95% ANI;85% AF; greedy incremental clustering
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{ANI cutoff};{AF cutoff};{clustering method}'
slot_uri: MIXS:0000085
multivalued: false
alias: otu_class_appr
domain_of:
- Miuvig
range: string

```
</details>