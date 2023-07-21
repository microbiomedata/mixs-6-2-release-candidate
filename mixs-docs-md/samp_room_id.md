# Slot: samp_room_id


_Sampling room number. This ID should be consistent with the designations on the building floor plans_



URI: [MIXS:0000244](https://w3id.org/mixs/0000244)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_room_id
description: Sampling room number. This ID should be consistent with the designations
  on the building floor plans
title: sampling room ID or name
notes:
- identifier
- room
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000244
multivalued: false
alias: samp_room_id
domain_of:
- BuiltEnvironment
- FoodFoodProductionFacility
range: integer
required: false
recommended: false

```
</details>