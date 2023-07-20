# Slot: lib_layout


_Specify whether to expect single, paired, or other configuration of reads_



URI: [MIXS:0000041](https://w3id.org/mixs/0000041)



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
[Mimag](Mimag.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [LIBLAYOUTENUM](LIBLAYOUTENUM.md)






## Examples

| Value |
| --- |
| paired |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: lib_layout
description: Specify whether to expect single, paired, or other configuration of reads
title: library layout
notes:
- library
examples:
- value: paired
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000041
multivalued: false
alias: lib_layout
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- MimarksS
- Mims
- Misag
- Miuvig
range: LIB_LAYOUT_ENUM

```
</details>