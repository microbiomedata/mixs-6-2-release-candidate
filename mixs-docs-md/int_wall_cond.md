# Slot: int_wall_cond


_The physical condition of the wall at the time of sampling; photos or video preferred; use drawings to indicate location of damaged areas_



URI: [MIXS:0000813](https://w3id.org/mixs/0000813)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [SHAREDENUM2](SHAREDENUM2.md)






## Examples

| Value |
| --- |
| damaged |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: int_wall_cond
description: The physical condition of the wall at the time of sampling; photos or
  video preferred; use drawings to indicate location of damaged areas
title: interior wall condition
notes:
- condition
- interior
- wall
examples:
- value: damaged
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000813
multivalued: false
alias: int_wall_cond
domain_of:
- BuiltEnvironment
range: SHARED_ENUM_2
required: false
recommended: false

```
</details>