# Slot: heat_cool_type


_Methods of conditioning or heating a room or building_



URI: [MIXS:0000766](https://w3id.org/mixs/0000766)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [HEATCOOLTYPEENUM](HEATCOOLTYPEENUM.md)

* Multivalued: True

* Required: True






## Examples

| Value |
| --- |
| heat pump |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: heat_cool_type
description: Methods of conditioning or heating a room or building
title: heating and cooling system type
notes:
- type
examples:
- value: heat pump
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000766
multivalued: true
alias: heat_cool_type
domain_of:
- BuiltEnvironment
range: HEAT_COOL_TYPE_ENUM
required: true

```
</details>