# Slot: food_product_type


_A food product type is a class of food products that is differentiated by its food composition (e.g., single- or multi-ingredient), processing and/or consumption characteristics. This does not include brand name products but it may include generic food dish categories. This field accepts terms under food product type (http://purl.obolibrary.org/obo/FOODON:03400361). For terms related to food product for an animal, consult food product for animal (http://purl.obolibrary.org/obo/FOODON_03309997). If the proper descriptor is not listed please use text to describe the food type. Multiple terms can be separated by one or more pipes_



URI: [MIXS:0001184](https://w3id.org/mixs/0001184)



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





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:00001002 or FOODON:03309997 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_product_type
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:00001002 or FOODON:03309997
description: A food product type is a class of food products that is differentiated
  by its food composition (e.g., single- or multi-ingredient), processing and/or consumption
  characteristics. This does not include brand name products but it may include generic
  food dish categories. This field accepts terms under food product type (http://purl.obolibrary.org/obo/FOODON:03400361).
  For terms related to food product for an animal, consult food product for animal
  (http://purl.obolibrary.org/obo/FOODON_03309997). If the proper descriptor is not
  listed please use text to describe the food type. Multiple terms can be separated
  by one or more pipes
title: food product type
notes:
- food
- product
- type
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001184
multivalued: false
alias: food_product_type
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string

```
</details>