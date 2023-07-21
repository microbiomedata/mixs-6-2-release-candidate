# Slot: door_loc


_The relative location of the door in the room_



URI: [MIXS:0000790](https://w3id.org/mixs/0000790)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [SHAREDENUM0](SHAREDENUM0.md)






## Examples

| Value |
| --- |
| north |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: door_loc
description: The relative location of the door in the room
title: door location
notes:
- door
- location
examples:
- value: north
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000790
multivalued: false
alias: door_loc
domain_of:
- BuiltEnvironment
range: SHARED_ENUM_0
required: false
recommended: false

```
</details>