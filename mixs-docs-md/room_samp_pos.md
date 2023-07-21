# Slot: room_samp_pos


_The horizontal sampling position in the room relative to architectural elements_



URI: [MIXS:0000824](https://w3id.org/mixs/0000824)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [ROOMSAMPPOSENUM](ROOMSAMPPOSENUM.md)






## Examples

| Value |
| --- |
| south corner |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: room_samp_pos
description: The horizontal sampling position in the room relative to architectural
  elements
title: room sampling position
notes:
- room
examples:
- value: south corner
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000824
multivalued: false
alias: room_samp_pos
domain_of:
- BuiltEnvironment
range: ROOM_SAMP_POS_ENUM
required: false
recommended: false

```
</details>