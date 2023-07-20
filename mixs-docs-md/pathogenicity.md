# Slot: pathogenicity


_To what is the entity pathogenic_



URI: [MIXS:0000027](https://w3id.org/mixs/0000027)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| human, animal, plant, fungi, bacteria |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pathogenicity
description: To what is the entity pathogenic
title: known pathogenicity
examples:
- value: human, animal, plant, fungi, bacteria
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000027
multivalued: false
alias: pathogenicity
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MigsVi
- Miuvig
range: string

```
</details>