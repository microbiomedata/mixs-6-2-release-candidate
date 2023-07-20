# Slot: room_connected


_List of rooms connected to the sampling room by a doorway_



URI: [MIXS:0000826](https://w3id.org/mixs/0000826)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [ROOMCONNECTEDENUM](ROOMCONNECTEDENUM.md)






## Examples

| Value |
| --- |
| office |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: room_connected
description: List of rooms connected to the sampling room by a doorway
title: rooms connected by a doorway
notes:
- doorway
- room
examples:
- value: office
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000826
multivalued: false
alias: room_connected
domain_of:
- BuiltEnvironment
range: ROOM_CONNECTED_ENUM
required: false
recommended: false

```
</details>