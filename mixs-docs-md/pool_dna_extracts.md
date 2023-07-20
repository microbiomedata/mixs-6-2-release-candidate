# Slot: pool_dna_extracts


_Indicate whether multiple DNA extractions were mixed. If the answer yes, the number of extracts that were pooled should be given_



URI: [MIXS:0000325](https://w3id.org/mixs/0000325)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram, milliliter, microliter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pool_dna_extracts
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram, milliliter, microliter
description: Indicate whether multiple DNA extractions were mixed. If the answer yes,
  the number of extracts that were pooled should be given
title: pooling of DNA extracts (if done)
notes:
- dna
- pooling
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000325
alias: pool_dna_extracts
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
- Soil
range: string

```
</details>