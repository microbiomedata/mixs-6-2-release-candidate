# Slot: facility_type


_Establishment details about the type of facility where the sample was taken. This is independent of the specific product(s) within the facility_



URI: [MIXS:0001252](https://w3id.org/mixs/0001252)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [FACILITYTYPEENUM](FACILITYTYPEENUM.md)

* Multivalued: True






## Examples

| Value |
| --- |
| manufacturing-processing |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: facility_type
description: Establishment details about the type of facility where the sample was
  taken. This is independent of the specific product(s) within the facility
title: facility type
notes:
- facility
- type
examples:
- value: manufacturing-processing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001252
multivalued: true
alias: facility_type
domain_of:
- FoodFoodProductionFacility
range: FACILITY_TYPE_ENUM
required: false
recommended: false

```
</details>