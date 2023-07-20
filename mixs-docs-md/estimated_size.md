# Slot: estimated_size


_The estimated size of the genome prior to sequencing. Of particular importance in the sequencing of (eukaryotic) genome which could remain in draft form for a long or unspecified period_



URI: [MIXS:0000024](https://w3id.org/mixs/0000024)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsOrg](MigsOrg.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 300000 bp |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | number of base pairs |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: estimated_size
annotations:
  Expected_value:
    tag: Expected_value
    value: number of base pairs
description: The estimated size of the genome prior to sequencing. Of particular importance
  in the sequencing of (eukaryotic) genome which could remain in draft form for a
  long or unspecified period
title: estimated size
notes:
- size
examples:
- value: 300000 bp
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{integer} bp'
slot_uri: MIXS:0000024
multivalued: false
alias: estimated_size
domain_of:
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Miuvig
range: string

```
</details>