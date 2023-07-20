# Slot: room_hallway


_List of room(s) (room number, room name) located in the same hallway as sampling room_



URI: [MIXS:0000238](https://w3id.org/mixs/0000238)



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
name: room_hallway
description: List of room(s) (room number, room name) located in the same hallway
  as sampling room
title: rooms that are on the same hallway
notes:
- hallway
- room
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000238
multivalued: false
alias: room_hallway
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