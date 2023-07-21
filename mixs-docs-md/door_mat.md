# Slot: door_mat


_The material the door is composed of_



URI: [MIXS:0000791](https://w3id.org/mixs/0000791)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [DOORMATENUM](DOORMATENUM.md)






## Examples

| Value |
| --- |
| wood |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: door_mat
description: The material the door is composed of
title: door material
notes:
- door
- material
examples:
- value: wood
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000791
multivalued: false
alias: door_mat
domain_of:
- BuiltEnvironment
range: DOOR_MAT_ENUM
required: false
recommended: false

```
</details>