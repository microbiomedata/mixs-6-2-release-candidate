# Slot: otu_db


_Reference database (i.e. sequences not generated as part of the current study) used to cluster new genomes in "species-level" OTUs, if any_



URI: [MIXS:0000087](https://w3id.org/mixs/0000087)



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
| NCBI Viral RefSeq;83 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | database and version |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: otu_db
annotations:
  Expected_value:
    tag: Expected_value
    value: database and version
description: Reference database (i.e. sequences not generated as part of the current
  study) used to cluster new genomes in "species-level" OTUs, if any
title: OTU database
notes:
- database
- otu
examples:
- value: NCBI Viral RefSeq;83
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{database};{version}'
slot_uri: MIXS:0000087
multivalued: false
alias: otu_db
domain_of:
- Miuvig
range: string

```
</details>