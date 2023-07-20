# Slot: food_treat_proc


_Used to specifically characterize a food product based on the treatment or processes applied to the product or any indexed ingredient. The processes include adding, substituting or removing components or modifying the food or component, e.g., through fermentation. Multiple values can be assigned. This fields accepts terms listed under food treatment process (http://purl.obolibrary.org/obo/FOODON_03460111)_



URI: [MIXS:0001140](https://w3id.org/mixs/0001140)



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
| gluten removal process [FOODON:03460750] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03460111 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_treat_proc
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03460111
description: Used to specifically characterize a food product based on the treatment
  or processes applied to the product or any indexed ingredient. The processes include
  adding, substituting or removing components or modifying the food or component,
  e.g., through fermentation. Multiple values can be assigned. This fields accepts
  terms listed under food treatment process (http://purl.obolibrary.org/obo/FOODON_03460111)
title: food treatment process
notes:
- food
- process
- treatment
examples:
- value: gluten removal process [FOODON:03460750]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001140
multivalued: true
alias: food_treat_proc
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