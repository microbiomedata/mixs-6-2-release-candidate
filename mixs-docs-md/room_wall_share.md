# Slot: room_wall_share


_List of room(s) (room number, room name) sharing a wall with the sampling room_



URI: [MIXS:0000243](https://w3id.org/mixs/0000243)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: room_wall_share
description: List of room(s) (room number, room name) sharing a wall with the sampling
  room
title: rooms that share a wall with sampling room
notes:
- room
- wall
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000243
multivalued: false
alias: room_wall_share
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
structured_pattern:
  syntax: '{room name};{room number}'
  interpolated: true
  partial_match: true

```
</details>