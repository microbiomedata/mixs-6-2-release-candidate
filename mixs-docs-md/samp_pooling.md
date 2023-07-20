# Slot: samp_pooling


_Physical combination of several instances of like material, e.g. RNA extracted from samples or dishes of cell cultures into one big aliquot of cells. Please provide a short description of the samples that were pooled_



URI: [MIXS:0001153](https://w3id.org/mixs/0001153)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 5uL of extracted genomic DNA from 5 leaves were pooled |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_pooling
description: Physical combination of several instances of like material, e.g. RNA
  extracted from samples or dishes of cell cultures into one big aliquot of cells.
  Please provide a short description of the samples that were pooled
title: sample pooling
notes:
- pooling
- sample
examples:
- value: 5uL of extracted genomic DNA from 5 leaves were pooled
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001153
multivalued: true
alias: samp_pooling
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string

```
</details>