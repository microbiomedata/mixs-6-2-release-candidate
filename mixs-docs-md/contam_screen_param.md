# Slot: contam_screen_param


_Specific parameters used in the decontamination sofware, such as reference database, coverage, and kmers. Combinations of these parameters may also be used, i.e. kmer and coverage, or reference database and kmer_



URI: [MIXS:0000073](https://w3id.org/mixs/0000073)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| kmer |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration;value or name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: contam_screen_param
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration;value or name
description: Specific parameters used in the decontamination sofware, such as reference
  database, coverage, and kmers. Combinations of these parameters may also be used,
  i.e. kmer and coverage, or reference database and kmer
title: contamination screening parameters
notes:
- parameter
examples:
- value: kmer
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[ref db|kmer|coverage|combination];{text|integer}'
slot_uri: MIXS:0000073
multivalued: false
alias: contam_screen_param
domain_of:
- Mimag
- Misag
range: string

```
</details>