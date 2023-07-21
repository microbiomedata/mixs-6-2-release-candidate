# Slot: assembly_software


_Tool(s) used for assembly, including version number and parameters_



URI: [MIXS:0000058](https://w3id.org/mixs/0000058)



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

* Range: [String](String.md)






## Examples

| Value |
| --- |
| metaSPAdes;3.11.0;kmer set 21,33,55,77,99,121, default parameters otherwise |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | name and version of software, parameters used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: assembly_software
annotations:
  Expected_value:
    tag: Expected_value
    value: name and version of software, parameters used
description: Tool(s) used for assembly, including version number and parameters
title: assembly software
notes:
- software
examples:
- value: metaSPAdes;3.11.0;kmer set 21,33,55,77,99,121, default parameters otherwise
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000058
multivalued: false
alias: assembly_software
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
range: string

```
</details>