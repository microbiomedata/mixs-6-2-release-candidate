# Slot: sim_search_meth


_Tool used to compare ORFs with database, along with version and cutoffs used_



URI: [MIXS:0000063](https://w3id.org/mixs/0000063)



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
| HMMER3;3.1b2;hmmsearch, cutoff of 50 on score |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | names and versions of software(s), parameters used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: sim_search_meth
annotations:
  Expected_value:
    tag: Expected_value
    value: names and versions of software(s), parameters used
description: Tool used to compare ORFs with database, along with version and cutoffs
  used
title: similarity search method
notes:
- method
examples:
- value: HMMER3;3.1b2;hmmsearch, cutoff of 50 on score
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000063
multivalued: false
alias: sim_search_meth
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

```
</details>