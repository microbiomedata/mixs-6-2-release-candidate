# Slot: room_condt


_The condition of the room at the time of sampling_



URI: [MIXS:0000822](https://w3id.org/mixs/0000822)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [ROOMCONDTENUM](ROOMCONDTENUM.md)






## Examples

| Value |
| --- |
| new |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: room_condt
description: The condition of the room at the time of sampling
title: room condition
notes:
- condition
- room
examples:
- value: new
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000822
multivalued: false
alias: room_condt
domain_of:
- BuiltEnvironment
range: ROOM_CONDT_ENUM
required: false
recommended: false

```
</details>