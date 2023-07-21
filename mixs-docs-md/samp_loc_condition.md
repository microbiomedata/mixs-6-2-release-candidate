# Slot: samp_loc_condition


_The condition of the sample location at the time of sampling_



URI: [MIXS:0001257](https://w3id.org/mixs/0001257)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [SAMPLOCCONDITIONENUM](SAMPLOCCONDITIONENUM.md)






## Examples

| Value |
| --- |
| new |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_loc_condition
description: The condition of the sample location at the time of sampling
title: sample location condition
notes:
- condition
- location
- sample
examples:
- value: new
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001257
multivalued: false
alias: samp_loc_condition
domain_of:
- FoodFoodProductionFacility
range: SAMP_LOC_CONDITION_ENUM
required: false
recommended: false

```
</details>