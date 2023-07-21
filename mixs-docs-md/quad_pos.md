# Slot: quad_pos


_The quadrant position of the sampling room within the building_



URI: [MIXS:0000820](https://w3id.org/mixs/0000820)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [QUADPOSENUM](QUADPOSENUM.md)






## Examples

| Value |
| --- |
| West side |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: quad_pos
description: The quadrant position of the sampling room within the building
title: quadrant position
examples:
- value: West side
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000820
multivalued: false
alias: quad_pos
domain_of:
- BuiltEnvironment
range: QUAD_POS_ENUM
required: false
recommended: false

```
</details>