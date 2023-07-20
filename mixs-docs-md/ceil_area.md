# Slot: ceil_area


_The area of the ceiling space within the room_



URI: [MIXS:0000148](https://w3id.org/mixs/0000148)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 25 square meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | square meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ceil_area
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: square meter
description: The area of the ceiling space within the room
title: ceiling area
notes:
- area
- ceiling
examples:
- value: 25 square meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000148
multivalued: false
alias: ceil_area
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>