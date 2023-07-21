# Slot: room_door_dist


_Distance between doors (meters) in the hallway between the sampling room and adjacent rooms_



URI: [MIXS:0000193](https://w3id.org/mixs/0000193)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[1-9][0-9]* \S.*\S+$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: room_door_dist
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: meter
description: Distance between doors (meters) in the hallway between the sampling room
  and adjacent rooms
title: room door distance
notes:
- distance
- door
- room
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000193
multivalued: false
alias: room_door_dist
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[1-9][0-9]* \S.*\S+$

```
</details>