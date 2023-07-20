# Slot: ref_biomaterial


_Primary publication if isolated before genome publication; otherwise, primary genome report_



URI: [MIXS:0000025](https://w3id.org/mixs/0000025)



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
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| doi:10.1016/j.syapm.2018.01.009 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ref_biomaterial
description: Primary publication if isolated before genome publication; otherwise,
  primary genome report
title: reference for biomaterial
examples:
- value: doi:10.1016/j.syapm.2018.01.009
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000025
multivalued: false
alias: ref_biomaterial
domain_of:
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- Mims
- Misag
- Miuvig
range: string
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}'
  interpolated: true
  partial_match: true

```
</details>