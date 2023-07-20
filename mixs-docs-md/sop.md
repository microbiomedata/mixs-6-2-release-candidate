# Slot: sop


_Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences_



URI: [MIXS:0000090](https://w3id.org/mixs/0000090)



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
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/its/ |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | reference to SOP |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: sop
annotations:
  Expected_value:
    tag: Expected_value
    value: reference to SOP
description: Standard operating procedures used in assembly and/or annotation of genomes,
  metagenomes or environmental sequences
title: relevant standard operating procedures
notes:
- procedures
examples:
- value: http://press.igsb.anl.gov/earthmicrobiome/protocols-and-standards/its/
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000090
multivalued: true
alias: sop
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- MimarksC
- MimarksS
- Mims
- Misag
- Miuvig
range: string

```
</details>