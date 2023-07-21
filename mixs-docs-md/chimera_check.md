# Slot: chimera_check


_Tool(s) used for chimera checking, including version number and parameters, to discover and remove chimeric sequences. A chimeric sequence is comprised of two or more phylogenetically distinct parent sequences_



URI: [MIXS:0000052](https://w3id.org/mixs/0000052)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| uchime;v4.1;default parameters |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | name and version of software, parameters used |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: chimera_check
annotations:
  Expected_value:
    tag: Expected_value
    value: name and version of software, parameters used
description: Tool(s) used for chimera checking, including version number and parameters,
  to discover and remove chimeric sequences. A chimeric sequence is comprised of two
  or more phylogenetically distinct parent sequences
title: chimera check software
notes:
- software
examples:
- value: uchime;v4.1;default parameters
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000052
multivalued: false
alias: chimera_check
domain_of:
- Agriculture
- MimarksC
- MimarksS
range: string

```
</details>