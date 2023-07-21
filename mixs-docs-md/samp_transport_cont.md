# Slot: samp_transport_cont


_Conatiner in which the sample was stored during transport. Indicate the location name_



URI: [MIXS:0001230](https://w3id.org/mixs/0001230)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [SAMPTRANSPORTCONTENUM](SAMPTRANSPORTCONTENUM.md)






## Examples

| Value |
| --- |
| cooler |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_transport_cont
description: Conatiner in which the sample was stored during transport. Indicate the
  location name
title: sample transport  container
notes:
- sample
- transport
examples:
- value: cooler
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001230
multivalued: false
alias: samp_transport_cont
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: SAMP_TRANSPORT_CONT_ENUM
required: false
recommended: false

```
</details>