# Slot: compl_software


_Tools used for completion estimate, i.e. checkm, anvi'o, busco_



URI: [MIXS:0000070](https://w3id.org/mixs/0000070)



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
| checkm |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | names and versions of software(s) used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: compl_software
annotations:
  Expected_value:
    tag: Expected_value
    value: names and versions of software(s) used
description: Tools used for completion estimate, i.e. checkm, anvi'o, busco
title: completeness software
notes:
- software
examples:
- value: checkm
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{software};{version}'
slot_uri: MIXS:0000070
multivalued: false
alias: compl_software
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