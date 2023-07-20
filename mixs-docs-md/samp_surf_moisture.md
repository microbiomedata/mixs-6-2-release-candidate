# Slot: samp_surf_moisture


_Degree of water held on a sampled surface.  If present, user can state the degree of water held on surface (intermittent moisture, submerged). If no surface moisture is present indicate not present_



URI: [MIXS:0001256](https://w3id.org/mixs/0001256)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [SAMPSURFMOISTUREENUM](SAMPSURFMOISTUREENUM.md)

* Multivalued: True






## Examples

| Value |
| --- |
| submerged |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_surf_moisture
description: Degree of water held on a sampled surface.  If present, user can state
  the degree of water held on surface (intermittent moisture, submerged). If no surface
  moisture is present indicate not present
title: sample surface moisture
notes:
- moisture
- sample
- surface
examples:
- value: submerged
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001256
multivalued: true
alias: samp_surf_moisture
domain_of:
- FoodFoodProductionFacility
range: SAMP_SURF_MOISTURE_ENUM
required: false
recommended: false

```
</details>