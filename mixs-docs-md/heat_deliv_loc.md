# Slot: heat_deliv_loc


_The location of heat delivery within the room_



URI: [MIXS:0000810](https://w3id.org/mixs/0000810)



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


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: heat_deliv_loc
description: The location of heat delivery within the room
title: heating delivery locations
notes:
- delivery
- location
- locations
examples:
- value: north
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000810
multivalued: false
alias: heat_deliv_loc
domain_of:
- BuiltEnvironment
range: SHARED_ENUM_0
required: false
recommended: false

```
</details>