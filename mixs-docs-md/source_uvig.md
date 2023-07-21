# Slot: source_uvig


_Type of dataset from which the UViG was obtained_



URI: [MIXS:0000035](https://w3id.org/mixs/0000035)



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
| viral fraction metagenome (virome) |

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
name: source_uvig
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: Type of dataset from which the UViG was obtained
title: source of UViGs
notes:
- source
examples:
- value: viral fraction metagenome (virome)
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[metagenome (not viral targeted)|viral fraction metagenome
  (virome)|sequence-targeted metagenome|metatranscriptome (not viral targeted)|viral
  fraction RNA metagenome (RNA virome)|sequence-targeted RNA metagenome|microbial
  single amplified genome (SAG)|viral single amplified genome (vSAG)|isolate microbial
  genome|other]'
slot_uri: MIXS:0000035
multivalued: false
alias: source_uvig
domain_of:
- Miuvig
range: string

```
</details>