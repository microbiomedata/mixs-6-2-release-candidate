# Slot: otu_seq_comp_appr


_Tool and thresholds used to compare sequences when computing "species-level" OTUs_



URI: [MIXS:0000086](https://w3id.org/mixs/0000086)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| blastn;2.6.0+;e-value cutoff: 0.001 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | software name, version and relevant parameters |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: otu_seq_comp_appr
annotations:
  Expected_value:
    tag: Expected_value
    value: software name, version and relevant parameters
description: Tool and thresholds used to compare sequences when computing "species-level"
  OTUs
title: OTU sequence comparison approach
notes:
- otu
examples:
- value: 'blastn;2.6.0+;e-value cutoff: 0.001'
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000086
multivalued: false
alias: otu_seq_comp_appr
domain_of:
- Miuvig
range: string

```
</details>