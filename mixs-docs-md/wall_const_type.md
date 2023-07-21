# Slot: wall_const_type


_The building class of the wall defined by the composition of the building elements and fire-resistance rating_



URI: [MIXS:0000841](https://w3id.org/mixs/0000841)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [WALLCONSTTYPEENUM](WALLCONSTTYPEENUM.md)






## Examples

| Value |
| --- |
| fire resistive |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: wall_const_type
description: The building class of the wall defined by the composition of the building
  elements and fire-resistance rating
title: wall construction type
notes:
- type
- wall
examples:
- value: fire resistive
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000841
multivalued: false
alias: wall_const_type
domain_of:
- BuiltEnvironment
range: WALL_CONST_TYPE_ENUM
required: false
recommended: false

```
</details>