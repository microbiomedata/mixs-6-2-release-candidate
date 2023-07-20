# Slot: adj_room


_List of rooms (room number, room name) immediately adjacent to the sampling room_



URI: [MIXS:0000219](https://w3id.org/mixs/0000219)



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
name: adj_room
description: List of rooms (room number, room name) immediately adjacent to the sampling
  room
title: adjacent rooms
notes:
- adjacent
- room
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000219
multivalued: false
alias: adj_room
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