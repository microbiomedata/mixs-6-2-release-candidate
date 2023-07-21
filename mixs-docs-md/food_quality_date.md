# Slot: food_quality_date


_The date recommended for the use of the product while at peak quality, this date is not a reflection of safety unless used on infant formula this date is not a reflection of safety and is typically labeled on a food product as "best if used by," best by," "use by," or "freeze by."_



URI: [MIXS:0001178](https://w3id.org/mixs/0001178)



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
| best by 2020-05-24 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration, date |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_quality_date
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration, date
description: The date recommended for the use of the product while at peak quality,
  this date is not a reflection of safety unless used on infant formula this date
  is not a reflection of safety and is typically labeled on a food product as "best
  if used by," best by," "use by," or "freeze by."
title: food quality date
notes:
- date
- food
- quality
examples:
- value: best by 2020-05-24
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[best by|best if used by|freeze by|use by]; date'
slot_uri: MIXS:0001178
multivalued: false
alias: food_quality_date
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