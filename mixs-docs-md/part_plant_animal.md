# Slot: part_plant_animal


_The anatomical part of the organism being involved in food production or consumption; e.g., a carrot is the root of the plant (root vegetable). This field accepts terms listed under part of plant or animal (http://purl.obolibrary.org/obo/FOODON_03420116)_



URI: [MIXS:0001149](https://w3id.org/mixs/0001149)



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

* Multivalued: True






## Examples

| Value |
| --- |
| chuck [FOODON:03530021] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03420116 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: part_plant_animal
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03420116
description: The anatomical part of the organism being involved in food production
  or consumption; e.g., a carrot is the root of the plant (root vegetable). This field
  accepts terms listed under part of plant or animal (http://purl.obolibrary.org/obo/FOODON_03420116)
title: part of plant or animal
notes:
- animal
- plant
examples:
- value: chuck [FOODON:03530021]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001149
multivalued: true
alias: part_plant_animal
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