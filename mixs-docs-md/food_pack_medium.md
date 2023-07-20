# Slot: food_pack_medium


_The medium in which the food is packed for preservation and handling or the medium surrounding homemade foods, e.g., peaches cooked in sugar syrup. The packing medium may provide a controlled environment for the food. It may also serve to improve palatability and consumer appeal.  This includes edible packing media (e.g. fruit juice), gas other than air (e.g. carbon dioxide), vacuum packed, or packed with aerosol propellant. This field accepts terms under food packing medium (http://purl.obolibrary.org/obo/FOODON_03480020). Multiple terms may apply and can be separated by pipes_



URI: [MIXS:0001134](https://w3id.org/mixs/0001134)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03480020 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_pack_medium
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03480020
description: The medium in which the food is packed for preservation and handling
  or the medium surrounding homemade foods, e.g., peaches cooked in sugar syrup. The
  packing medium may provide a controlled environment for the food. It may also serve
  to improve palatability and consumer appeal.  This includes edible packing media
  (e.g. fruit juice), gas other than air (e.g. carbon dioxide), vacuum packed, or
  packed with aerosol propellant. This field accepts terms under food packing medium
  (http://purl.obolibrary.org/obo/FOODON_03480020). Multiple terms may apply and can
  be separated by pipes
title: food packing medium
notes:
- food
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001134
multivalued: true
alias: food_pack_medium
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>