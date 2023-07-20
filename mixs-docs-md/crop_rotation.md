# Slot: crop_rotation


_Whether or not crop is rotated, and if yes, rotation schedule_



URI: [MIXS:0000318](https://w3id.org/mixs/0000318)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| yes;R2/2017-01-01/2018-12-31/P6M |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: crop_rotation
description: Whether or not crop is rotated, and if yes, rotation schedule
title: history/crop rotation
notes:
- history
examples:
- value: yes;R2/2017-01-01/2018-12-31/P6M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000318
multivalued: false
alias: crop_rotation
domain_of:
- Agriculture
- FoodFarmEnvironment
- Soil
range: string
structured_pattern:
  syntax: '{crop_rotation_status};{schedule}'
  interpolated: true
  partial_match: true

```
</details>