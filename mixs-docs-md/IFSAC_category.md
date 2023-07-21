# Slot: IFSAC_category


_The IFSAC food categorization scheme has five distinct levels to which foods can be assigned, depending upon the type of food. First, foods are assigned to one of four food groups (aquatic animals, land animals, plants, and other). Food groups include increasingly specific food categories; dairy, eggs, meat and poultry, and game are in the land animal food group, and the category meat and poultry is further subdivided into more specific categories of meat (beef, pork, other meat) and poultry (chicken, turkey, other poultry). Finally, foods are differentiated by differences in food processing (such as pasteurized fluid dairy products, unpasteurized fluid dairy products, pasteurized solid and semi-solid dairy products, and unpasteurized solid and semi-solid dairy products. An IFSAC food category chart is available from https://www.cdc.gov/foodsafety/ifsac/projects/food-categorization-scheme.html PMID: 28926300_



URI: [MIXS:0001179](https://w3id.org/mixs/0001179)



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

* Required: True






## Examples

| Value |
| --- |
| Plants:Produce:Vegetables:Herbs:Dried Herbs |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | IFSAC term |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: IFSAC_category
annotations:
  Expected_value:
    tag: Expected_value
    value: IFSAC term
description: 'The IFSAC food categorization scheme has five distinct levels to which
  foods can be assigned, depending upon the type of food. First, foods are assigned
  to one of four food groups (aquatic animals, land animals, plants, and other). Food
  groups include increasingly specific food categories; dairy, eggs, meat and poultry,
  and game are in the land animal food group, and the category meat and poultry is
  further subdivided into more specific categories of meat (beef, pork, other meat)
  and poultry (chicken, turkey, other poultry). Finally, foods are differentiated
  by differences in food processing (such as pasteurized fluid dairy products, unpasteurized
  fluid dairy products, pasteurized solid and semi-solid dairy products, and unpasteurized
  solid and semi-solid dairy products. An IFSAC food category chart is available from
  https://www.cdc.gov/foodsafety/ifsac/projects/food-categorization-scheme.html PMID:
  28926300'
title: Interagency Food Safety Analytics Collaboration (IFSAC) category
notes:
- food
examples:
- value: Plants:Produce:Vegetables:Herbs:Dried Herbs
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001179
multivalued: true
alias: IFSAC_category
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: true

```
</details>