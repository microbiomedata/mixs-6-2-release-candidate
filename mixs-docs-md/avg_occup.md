# Slot: avg_occup


_Daily average occupancy of room. Indicate the number of person(s) daily occupying the sampling room_



URI: [MIXS:0000775](https://w3id.org/mixs/0000775)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: avg_occup
description: Daily average occupancy of room. Indicate the number of person(s) daily
  occupying the sampling room
title: average daily occupancy
notes:
- average
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000775
multivalued: false
alias: avg_occup
domain_of:
- BuiltEnvironment
- FoodFoodProductionFacility
range: float
required: false
recommended: false

```
</details>