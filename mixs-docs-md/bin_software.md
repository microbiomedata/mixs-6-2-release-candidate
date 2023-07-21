# Slot: bin_software


_Tool(s) used for the extraction of genomes from metagenomic datasets, where possible include a product ID (PID) of the tool(s) used_



URI: [MIXS:0000078](https://w3id.org/mixs/0000078)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| MetaCluster-TA (RRID:SCR_004599), MaxBin (biotools:maxbin) |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | names and versions of software(s) used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: bin_software
annotations:
  Expected_value:
    tag: Expected_value
    value: names and versions of software(s) used
description: Tool(s) used for the extraction of genomes from metagenomic datasets,
  where possible include a product ID (PID) of the tool(s) used
title: binning software
notes:
- software
examples:
- value: MetaCluster-TA (RRID:SCR_004599), MaxBin (biotools:maxbin)
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{software};{version}{PID}'
slot_uri: MIXS:0000078
multivalued: false
alias: bin_software
domain_of:
- Mimag
- Miuvig
range: string

```
</details>