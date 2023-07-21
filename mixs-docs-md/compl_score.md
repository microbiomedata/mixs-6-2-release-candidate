# Slot: compl_score


_Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. High Quality Draft: >90%, Medium Quality Draft: >50%, and Low Quality Draft: < 50% should have the indicated completeness scores_



URI: [MIXS:0000069](https://w3id.org/mixs/0000069)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsOrg](MigsOrg.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| med;60% |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | quality;percent completeness |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: compl_score
annotations:
  Expected_value:
    tag: Expected_value
    value: quality;percent completeness
description: 'Completeness score is typically based on either the fraction of markers
  found as compared to a database or the percent of a genome found as compared to
  a closely related reference genome. High Quality Draft: >90%, Medium Quality Draft:
  >50%, and Low Quality Draft: < 50% should have the indicated completeness scores'
title: completeness score
notes:
- score
examples:
- value: med;60%
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[high|med|low];{percentage}'
slot_uri: MIXS:0000069
multivalued: false
alias: compl_score
domain_of:
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- Misag
- Miuvig
range: string

```
</details>