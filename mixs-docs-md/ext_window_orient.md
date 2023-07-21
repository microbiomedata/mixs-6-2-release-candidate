# Slot: ext_window_orient


_The compass direction the exterior window of the room is facing_



URI: [MIXS:0000818](https://w3id.org/mixs/0000818)



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
| southwest |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: ext_window_orient
description: The compass direction the exterior window of the room is facing
title: orientations of exterior window
notes:
- exterior
- window
examples:
- value: southwest
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000818
multivalued: false
alias: ext_window_orient
domain_of:
- BuiltEnvironment
range: SHARED_ENUM_0
required: false
recommended: false

```
</details>