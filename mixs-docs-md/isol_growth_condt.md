# Slot: isol_growth_condt


_Publication reference in the form of pubmed ID (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material_



URI: [MIXS:0000003](https://w3id.org/mixs/0000003)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsOrg](MigsOrg.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| doi: 10.1016/j.syapm.2018.01.009 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: isol_growth_condt
description: Publication reference in the form of pubmed ID (pmid), digital object
  identifier (doi) or url for isolation and growth condition specifications of the
  organism/material
title: isolation and growth condition
notes:
- condition
- growth
- isolation
examples:
- value: 'doi: 10.1016/j.syapm.2018.01.009'
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000003
multivalued: false
alias: isol_growth_condt
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- MimarksC
range: string
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}'
  interpolated: true
  partial_match: true

```
</details>