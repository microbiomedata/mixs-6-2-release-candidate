# Slot: food_origin


_A reference to a place on the Earth, by its name or by its geographical location that describes the origin of the food commodity, either in terms of its cultivation or production. This field accepts terms listed under geographic location (http://purl.obolibrary.org/obo/GAZ_00000448)_



URI: [MIXS:0001207](https://w3id.org/mixs/0001207)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_origin
description: A reference to a place on the Earth, by its name or by its geographical
  location that describes the origin of the food commodity, either in terms of its
  cultivation or production. This field accepts terms listed under geographic location
  (http://purl.obolibrary.org/obo/GAZ_00000448)
title: food product origin geographic location
notes:
- food
- geographic
- location
- product
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001207
multivalued: false
alias: food_origin
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
structured_pattern:
  syntax: '{country}: {region}, {specific location}'
  interpolated: true
  partial_match: true

```
</details>