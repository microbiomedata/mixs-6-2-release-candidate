# Slot: door_type_wood


_The type of wood door_



URI: [MIXS:0000797](https://w3id.org/mixs/0000797)



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
| battened |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: door_type_wood
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: The type of wood door
title: door type, wood
notes:
- door
- type
examples:
- value: battened
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[bettened and ledged|battened|ledged and braced|battened|ledged
  and framed|battened|ledged, braced and frame|framed and paneled|glashed or sash|flush|louvered|wire
  gauged]'
slot_uri: MIXS:0000797
multivalued: false
alias: door_type_wood
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>