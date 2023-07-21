# Slot: room_type


_The main purpose or activity of the sampling room. A room is any distinguishable space within a structure_



URI: [MIXS:0000825](https://w3id.org/mixs/0000825)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| bathroom |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: room_type
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: The main purpose or activity of the sampling room. A room is any distinguishable
  space within a structure
title: room type
notes:
- room
- type
examples:
- value: bathroom
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[attic|bathroom|closet|conference room|elevator|examining room|hallway|kitchen|mail
  room|private office|open office|stairwell|,restroom|lobby|vestibule|mechanical or
  electrical room|data center|laboratory_wet|laboratory_dry|gymnasium|natatorium|auditorium|lockers|cafe|warehouse]'
slot_uri: MIXS:0000825
multivalued: false
alias: room_type
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>