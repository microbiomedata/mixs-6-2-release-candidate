# Slot: gravidity


_Whether or not subject is gravid, and if yes date due or date post-conception, specifying which is used_



URI: [MIXS:0000875](https://w3id.org/mixs/0000875)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HostAssociated](HostAssociated.md) |  |  yes  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| yes;due date:2018-05-11 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: gravidity
description: Whether or not subject is gravid, and if yes date due or date post-conception,
  specifying which is used
title: gravidity
examples:
- value: yes;due date:2018-05-11
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{boolean};{timestamp}'
slot_uri: MIXS:0000875
multivalued: false
alias: gravidity
domain_of:
- HostAssociated
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>