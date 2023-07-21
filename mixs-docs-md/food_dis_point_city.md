# Slot: food_dis_point_city


_A reference to a place on the Earth, by its name or by its geographical location that refers to a distribution point along the food chain. This field accepts terms listed under geographic location (http://purl.obolibrary.org/obo/GAZ_00000448). Reference: Adam Diamond, James Barham. Moving Food Along the Value Chain: Innovations in Regional Food Distribution. U.S. Dept. of Agriculture, Agricultural Marketing Service. Washington, DC. March 2012. http://dx.doi.org/10.9752/MS045.03-2012_



URI: [MIXS:0001204](https://w3id.org/mixs/0001204)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Atlanta[GAZ:00004445] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | GAZ:00000448 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_dis_point_city
annotations:
  Expected_value:
    tag: Expected_value
    value: GAZ:00000448
description: 'A reference to a place on the Earth, by its name or by its geographical
  location that refers to a distribution point along the food chain. This field accepts
  terms listed under geographic location (http://purl.obolibrary.org/obo/GAZ_00000448).
  Reference: Adam Diamond, James Barham. Moving Food Along the Value Chain: Innovations
  in Regional Food Distribution. U.S. Dept. of Agriculture, Agricultural Marketing
  Service. Washington, DC. March 2012. http://dx.doi.org/10.9752/MS045.03-2012'
title: food distribution point geographic location (city)
notes:
- food
- geographic
- location
examples:
- value: Atlanta[GAZ:00004445]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001204
multivalued: true
alias: food_dis_point_city
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>