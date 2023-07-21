# Slot: vir_ident_software


_Tool(s) used for the identification of UViG as a viral genome, software or protocol name including version number, parameters, and cutoffs used_



URI: [MIXS:0000081](https://w3id.org/mixs/0000081)



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
| VirSorter; 1.0.4; Virome database, category 2 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | software name, version and relevant parameters |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: vir_ident_software
annotations:
  Expected_value:
    tag: Expected_value
    value: software name, version and relevant parameters
description: Tool(s) used for the identification of UViG as a viral genome, software
  or protocol name including version number, parameters, and cutoffs used
title: viral identification software
notes:
- identifier
- software
examples:
- value: VirSorter; 1.0.4; Virome database, category 2
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{software};{version};{parameters}'
slot_uri: MIXS:0000081
multivalued: false
alias: vir_ident_software
domain_of:
- Miuvig
range: string

```
</details>