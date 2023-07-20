# Slot: food_product_qual


_Descriptors for describing food visually or via other senses, which is useful for tasks like food inspection where little prior knowledge of how the food came to be is available. Some terms like "food (frozen)" are both a quality descriptor and the output of a process. This field accepts terms listed under food product by quality (http://purl.obolibrary.org/obo/FOODON_00002454)_



URI: [MIXS:0001213](https://w3id.org/mixs/0001213)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| raw [FOODON:03311126] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_product_qual
description: Descriptors for describing food visually or via other senses, which is
  useful for tasks like food inspection where little prior knowledge of how the food
  came to be is available. Some terms like "food (frozen)" are both a quality descriptor
  and the output of a process. This field accepts terms listed under food product
  by quality (http://purl.obolibrary.org/obo/FOODON_00002454)
title: food product by quality
notes:
- food
- product
- quality
examples:
- value: raw [FOODON:03311126]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001213
multivalued: false
alias: food_product_qual
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>