# Slot: host_spec_range


_The range and diversity of host species that an organism is capable of infecting, defined by NCBI taxonomy identifier_



URI: [MIXS:0000030](https://w3id.org/mixs/0000030)



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

* Multivalued: True






## Examples

| Value |
| --- |
| 9606 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCBI taxid |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_spec_range
annotations:
  Expected_value:
    tag: Expected_value
    value: NCBI taxid
description: The range and diversity of host species that an organism is capable of
  infecting, defined by NCBI taxonomy identifier
title: host specificity or range
notes:
- host
- host.
- range
examples:
- value: '9606'
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{integer}'
slot_uri: MIXS:0000030
multivalued: true
alias: host_spec_range
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