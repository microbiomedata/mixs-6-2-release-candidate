# Slot: reassembly_bin


_Has an assembly been performed on a genome bin extracted from a metagenomic assembly?_



URI: [MIXS:0000079](https://w3id.org/mixs/0000079)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [Boolean](Boolean.md)






## Examples

| Value |
| --- |
| no |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: reassembly_bin
description: Has an assembly been performed on a genome bin extracted from a metagenomic
  assembly?
title: reassembly post binning
notes:
- post
examples:
- value: 'no'
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000079
multivalued: false
alias: reassembly_bin
domain_of:
- Mimag
- Miuvig
range: boolean

```
</details>