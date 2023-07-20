# Slot: target_gene


_Targeted gene or locus name for marker gene studies_



URI: [MIXS:0000044](https://w3id.org/mixs/0000044)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 16S rRNA, 18S rRNA, nif, amoA, rpo |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: target_gene
description: Targeted gene or locus name for marker gene studies
title: target gene
notes:
- target
examples:
- value: 16S rRNA, 18S rRNA, nif, amoA, rpo
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000044
multivalued: false
alias: target_gene
domain_of:
- Agriculture
- MimarksC
- MimarksS
range: string

```
</details>