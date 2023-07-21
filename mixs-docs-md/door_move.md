# Slot: door_move


_The type of movement of the door_



URI: [MIXS:0000792](https://w3id.org/mixs/0000792)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [DOORMOVEENUM](DOORMOVEENUM.md)






## Examples

| Value |
| --- |
| swinging |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: door_move
description: The type of movement of the door
title: door movement
notes:
- door
examples:
- value: swinging
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000792
multivalued: false
alias: door_move
domain_of:
- BuiltEnvironment
range: DOOR_MOVE_ENUM
required: false
recommended: false

```
</details>