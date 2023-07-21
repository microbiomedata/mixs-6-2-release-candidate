# Slot: num_replicons


_Reports the number of replicons in a nuclear genome of eukaryotes, in the genome of a bacterium or archaea or the number of segments in a segmented virus. Always applied to the haploid chromosome count of a eukaryote_



URI: [MIXS:0000022](https://w3id.org/mixs/0000022)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |







## Properties

* Range: [Integer](Integer.md)






## Examples

| Value |
| --- |
| 2 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | for eukaryotes and bacteria: chromosomes (haploid count); for viruses: segments |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: num_replicons
annotations:
  Expected_value:
    tag: Expected_value
    value: 'for eukaryotes and bacteria: chromosomes (haploid count); for viruses:
      segments'
description: Reports the number of replicons in a nuclear genome of eukaryotes, in
  the genome of a bacterium or archaea or the number of segments in a segmented virus.
  Always applied to the haploid chromosome count of a eukaryote
title: number of replicons
notes:
- number
examples:
- value: '2'
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{integer}'
slot_uri: MIXS:0000022
alias: num_replicons
domain_of:
- MigsBa
- MigsEu
- MigsVi
range: integer

```
</details>