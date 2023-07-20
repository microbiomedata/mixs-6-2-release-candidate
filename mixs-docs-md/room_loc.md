# Slot: room_loc


_The position of the room within the building_



URI: [MIXS:0000823](https://w3id.org/mixs/0000823)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [ROOMLOCENUM](ROOMLOCENUM.md)






## Examples

| Value |
| --- |
| interior room |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: room_loc
description: The position of the room within the building
title: room location in building
notes:
- location
- room
examples:
- value: interior room
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000823
multivalued: false
alias: room_loc
domain_of:
- BuiltEnvironment
range: ROOM_LOC_ENUM
required: false
recommended: false

```
</details>