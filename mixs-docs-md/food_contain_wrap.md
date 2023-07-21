# Slot: food_contain_wrap


_Type of container or wrapping defined by the main container material, the container form, and the material of the liner lids or ends. Also type of container or wrapping by form; prefer description by material first, then by form. This field accepts terms listed under food container or wrapping (http://purl.obolibrary.org/obo/FOODON_03490100)_



URI: [MIXS:0001132](https://w3id.org/mixs/0001132)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Plastic shrink-pack [FOODON:03490137] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03490100 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_contain_wrap
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03490100
description: Type of container or wrapping defined by the main container material,
  the container form, and the material of the liner lids or ends. Also type of container
  or wrapping by form; prefer description by material first, then by form. This field
  accepts terms listed under food container or wrapping (http://purl.obolibrary.org/obo/FOODON_03490100)
title: food container or wrapping
notes:
- food
examples:
- value: Plastic shrink-pack [FOODON:03490137]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001132
multivalued: false
alias: food_contain_wrap
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