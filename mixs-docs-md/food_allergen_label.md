# Slot: food_allergen_label


_A label indication that the product contains a recognized allergen. This field accepts terms listed under dietary claim or use (http://purl.obolibrary.org/obo/FOODON_03510213)_



URI: [MIXS:0001201](https://w3id.org/mixs/0001201)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| food allergen labelling about crustaceans and products thereof [FOODON:03510215] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03510213 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: food_allergen_label
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03510213
description: A label indication that the product contains a recognized allergen. This
  field accepts terms listed under dietary claim or use (http://purl.obolibrary.org/obo/FOODON_03510213)
title: food allergen labeling
notes:
- food
examples:
- value: food allergen labelling about crustaceans and products thereof [FOODON:03510215]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001201
multivalued: true
alias: food_allergen_label
domain_of:
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>