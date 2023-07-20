# Slot: indoor_space


_A distinguishable space within a structure, the purpose for which discrete areas of a building is used_



URI: [MIXS:0000763](https://w3id.org/mixs/0000763)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [INDOORSPACEENUM](INDOORSPACEENUM.md)

* Required: True






## Examples

| Value |
| --- |
| foyer |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: indoor_space
description: A distinguishable space within a structure, the purpose for which discrete
  areas of a building is used
title: indoor space
notes:
- indoor
examples:
- value: foyer
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000763
multivalued: false
alias: indoor_space
domain_of:
- BuiltEnvironment
range: INDOOR_SPACE_ENUM
required: true

```
</details>