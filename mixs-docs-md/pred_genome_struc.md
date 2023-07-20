# Slot: pred_genome_struc


_Expected structure of the viral genome_



URI: [MIXS:0000083](https://w3id.org/mixs/0000083)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [PREDGENOMESTRUCENUM](PREDGENOMESTRUCENUM.md)






## Examples

| Value |
| --- |
| non-segmented |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pred_genome_struc
description: Expected structure of the viral genome
title: predicted genome structure
notes:
- predict
examples:
- value: non-segmented
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000083
multivalued: false
alias: pred_genome_struc
domain_of:
- Miuvig
range: PRED_GENOME_STRUC_ENUM

```
</details>