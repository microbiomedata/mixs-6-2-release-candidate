# Slot: tax_ident


_The phylogenetic marker(s) used to assign an organism name to the SAG or MAG_



URI: [MIXS:0000053](https://w3id.org/mixs/0000053)



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

* Range: [TAXIDENTENUM](TAXIDENTENUM.md)






## Examples

| Value |
| --- |
| other |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: tax_ident
description: The phylogenetic marker(s) used to assign an organism name to the SAG
  or MAG
title: taxonomic identity marker
notes:
- identifier
- marker
- taxon
examples:
- value: other
  description: was other <colon> rpoB gene
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000053
alias: tax_ident
domain_of:
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- Misag
- Miuvig
range: TAX_IDENT_ENUM

```
</details>