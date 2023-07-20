# Slot: encoded_traits


_Should include key traits like antibiotic resistance or xenobiotic degradation phenotypes for plasmids, converting genes for phage_



URI: [MIXS:0000034](https://w3id.org/mixs/0000034)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| beta-lactamase class A |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | for plasmid: antibiotic resistance; for phage: converting genes |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: encoded_traits
annotations:
  Expected_value:
    tag: Expected_value
    value: 'for plasmid: antibiotic resistance; for phage: converting genes'
description: Should include key traits like antibiotic resistance or xenobiotic degradation
  phenotypes for plasmids, converting genes for phage
title: encoded traits
examples:
- value: beta-lactamase class A
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000034
multivalued: false
alias: encoded_traits
domain_of:
- MigsBa
- MigsPl
- MigsVi
range: string

```
</details>