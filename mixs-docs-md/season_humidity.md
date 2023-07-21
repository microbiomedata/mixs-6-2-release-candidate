# Slot: season_humidity


_Average humidity of the region throughout the growing season_



URI: [MIXS:0001148](https://w3id.org/mixs/0001148)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [Float](Float.md)






## Examples

| Value |
| --- |
| 0.25 |

## Comments

* percent or float?

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: season_humidity
description: Average humidity of the region throughout the growing season
title: mean seasonal humidity
notes:
- humidity
- mean
- season
comments:
- percent or float?
examples:
- value: '0.25'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001148
alias: season_humidity
domain_of:
- Agriculture
- FoodFarmEnvironment
range: float
required: false
recommended: false

```
</details>