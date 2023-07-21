# Slot: mag_cov_software


_Tool(s) used to determine the genome coverage if coverage is used as a binning parameter in the extraction of genomes from metagenomic datasets_



URI: [MIXS:0000080](https://w3id.org/mixs/0000080)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [MAGCOVSOFTWAREENUM](MAGCOVSOFTWAREENUM.md)






## Examples

| Value |
| --- |
| bbmap |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: mag_cov_software
description: Tool(s) used to determine the genome coverage if coverage is used as
  a binning parameter in the extraction of genomes from metagenomic datasets
title: MAG coverage software
notes:
- software
examples:
- value: bbmap
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000080
multivalued: false
alias: mag_cov_software
domain_of:
- Mimag
- Miuvig
range: MAG_COV_SOFTWARE_ENUM

```
</details>