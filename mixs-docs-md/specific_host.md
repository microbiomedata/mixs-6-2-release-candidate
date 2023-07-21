# Slot: specific_host


_Report the host's taxonomic name and/or NCBI taxonomy ID_



URI: [MIXS:0000029](https://w3id.org/mixs/0000029)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Homo sapiens and/or 9606 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | host scientific name, taxonomy ID |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: specific_host
annotations:
  Expected_value:
    tag: Expected_value
    value: host scientific name, taxonomy ID
description: Report the host's taxonomic name and/or NCBI taxonomy ID
title: host scientific name
notes:
- host
- host.
examples:
- value: Homo sapiens and/or 9606
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{NCBI taxid}'
slot_uri: MIXS:0000029
multivalued: false
alias: specific_host
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MigsPl
- MigsVi
- Miuvig
range: string

```
</details>