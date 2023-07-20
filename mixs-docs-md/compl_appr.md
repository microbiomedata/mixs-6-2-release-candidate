# Slot: compl_appr


_The approach used to determine the completeness of a given genomic assembly, which would typically make use of a set of conserved marker genes or a closely related reference genome. For UViG completeness, include reference genome or group used, and contig feature suggesting a complete genome_



URI: [MIXS:0000071](https://w3id.org/mixs/0000071)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [COMPLAPPRENUM](COMPLAPPRENUM.md)






## Examples

| Value |
| --- |
| other |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | text |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: compl_appr
annotations:
  Expected_value:
    tag: Expected_value
    value: text
description: The approach used to determine the completeness of a given genomic assembly,
  which would typically make use of a set of conserved marker genes or a closely related
  reference genome. For UViG completeness, include reference genome or group used,
  and contig feature suggesting a complete genome
title: completeness approach
examples:
- value: other
  description: was other <colon> UViG length compared to the average length of reference
    genomes from the P22virus genus (NCBI RefSeq v83)
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000071
alias: compl_appr
domain_of:
- Mimag
- Misag
- Miuvig
range: COMPL_APPR_ENUM

```
</details>