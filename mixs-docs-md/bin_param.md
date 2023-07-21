# Slot: bin_param


_The parameters that have been applied during the extraction of genomes from metagenomic datasets_



URI: [MIXS:0000077](https://w3id.org/mixs/0000077)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [BINPARAMENUM](BINPARAMENUM.md)






## Examples

| Value |
| --- |
| coverage |
| kmer |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: bin_param
description: The parameters that have been applied during the extraction of genomes
  from metagenomic datasets
title: binning parameters
notes:
- parameter
examples:
- value: coverage
  description: was 'coverage and kmer'
- value: kmer
  description: was coverage and kmer
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000077
alias: bin_param
domain_of:
- Mimag
- Miuvig
range: BIN_PARAM_ENUM

```
</details>