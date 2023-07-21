# Slot: door_direct


_The direction the door opens_



URI: [MIXS:0000789](https://w3id.org/mixs/0000789)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [DOORDIRECTENUM](DOORDIRECTENUM.md)






## Examples

| Value |
| --- |
| inward |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: door_direct
description: The direction the door opens
title: door direction of opening
notes:
- direction
- door
examples:
- value: inward
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000789
multivalued: false
alias: door_direct
domain_of:
- BuiltEnvironment
range: DOOR_DIRECT_ENUM
required: false
recommended: false

```
</details>