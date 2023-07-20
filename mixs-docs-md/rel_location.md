# Slot: rel_location


_Location of sampled soil to other parts of the farm e.g. under crop plant, near irrigation ditch, from the dirt road_



URI: [MIXS:0001161](https://w3id.org/mixs/0001161)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| furrow |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: rel_location
description: Location of sampled soil to other parts of the farm e.g. under crop plant,
  near irrigation ditch, from the dirt road
title: relative location of sample
notes:
- location
- relative
- sample
examples:
- value: furrow
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001161
multivalued: false
alias: rel_location
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string

```
</details>