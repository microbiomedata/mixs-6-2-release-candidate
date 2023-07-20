# Slot: propagation


_The type of reproduction from the parent stock. Values for this field is specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual_



URI: [MIXS:0000033](https://w3id.org/mixs/0000033)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| lytic |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | for virus: lytic, lysogenic, temperate, obligately lytic; for plasmid: incompatibility group; for eukaryote: asexual, sexual; other more specific values (e.g., incompatibility group) are allowed |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: propagation
annotations:
  Expected_value:
    tag: Expected_value
    value: 'for virus: lytic, lysogenic, temperate, obligately lytic; for plasmid:
      incompatibility group; for eukaryote: asexual, sexual; other more specific values
      (e.g., incompatibility group) are allowed'
description: 'The type of reproduction from the parent stock. Values for this field
  is specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately
  lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual'
title: propagation
examples:
- value: lytic
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000033
multivalued: false
alias: propagation
domain_of:
- MigsEu
- MigsPl
- MigsVi
range: string

```
</details>