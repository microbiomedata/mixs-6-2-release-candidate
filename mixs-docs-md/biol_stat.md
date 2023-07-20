# Slot: biol_stat


_The level of genome modification_



URI: [MIXS:0000858](https://w3id.org/mixs/0000858)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HostAssociated](HostAssociated.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| natural |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: biol_stat
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: The level of genome modification
title: biological status
notes:
- status
examples:
- value: natural
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[wild|natural|semi-natural|inbred line|breeder''s line|hybrid|clonal
  selection|mutant]'
slot_uri: MIXS:0000858
multivalued: false
alias: biol_stat
domain_of:
- HostAssociated
- PlantAssociated
range: string
required: false
recommended: false

```
</details>