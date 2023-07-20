# Slot: farm_water_source


_Source of water used on the farm for irrigation of crops or watering of livestock_



URI: [MIXS:0001110](https://w3id.org/mixs/0001110)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [FARMWATERSOURCEENUM](FARMWATERSOURCEENUM.md)

* Recommended: True






## Examples

| Value |
| --- |
| well |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: farm_water_source
description: Source of water used on the farm for irrigation of crops or watering
  of livestock
title: farm watering water source
notes:
- farm
- source
- water
examples:
- value: well
  description: was water well (ENVO:01000002)
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001110
alias: farm_water_source
domain_of:
- Agriculture
- FoodFarmEnvironment
range: FARM_WATER_SOURCE_ENUM
recommended: true

```
</details>