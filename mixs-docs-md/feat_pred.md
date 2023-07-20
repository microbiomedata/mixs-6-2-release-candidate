# Slot: feat_pred


_Method used to predict UViGs features such as ORFs, integration site, etc_



URI: [MIXS:0000061](https://w3id.org/mixs/0000061)



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
| Prodigal;2.6.3;default parameters |

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
name: feat_pred
annotations:
  Expected_value:
    tag: Expected_value
    value: names and versions of software(s), parameters used
description: Method used to predict UViGs features such as ORFs, integration site,
  etc
title: feature prediction
notes:
- feature
- predict
examples:
- value: Prodigal;2.6.3;default parameters
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000061
multivalued: false
alias: feat_pred
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