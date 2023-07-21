# Slot: mid


_Molecular barcodes, called Multiplex Identifiers (MIDs), that are used to specifically tag unique samples in a sequencing run. Sequence should be reported in uppercase letters_



URI: [MIXS:0000047](https://w3id.org/mixs/0000047)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Mimag](Mimag.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[ACGTRKSYMWBHDVN]+$`






## Examples

| Value |
| --- |
| GTGAATAT |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: mid
description: Molecular barcodes, called Multiplex Identifiers (MIDs), that are used
  to specifically tag unique samples in a sequencing run. Sequence should be reported
  in uppercase letters
title: multiplex identifiers
notes:
- identifier
examples:
- value: GTGAATAT
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000047
multivalued: false
alias: mid
domain_of:
- Agriculture
- Mimag
- MimarksS
- Mims
- Misag
- Miuvig
range: string
pattern: ^[ACGTRKSYMWBHDVN]+$

```
</details>