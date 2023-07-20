# Slot: microb_cult_med


_A culture medium used to select for, grow, and maintain prokaryotic microorganisms. Can be in either liquid (broth) or solidified (e.g. with agar) forms. This field accepts terms listed under microbiological culture medium (http://purl.obolibrary.org/obo/MICRO_0000067). If the proper descriptor is not listed please use text to describe the culture medium_



URI: [MIXS:0001216](https://w3id.org/mixs/0001216)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| brain heart infusion agar [MICRO:0000566] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | MICRO:0000067 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: microb_cult_med
annotations:
  Expected_value:
    tag: Expected_value
    value: MICRO:0000067
description: A culture medium used to select for, grow, and maintain prokaryotic microorganisms.
  Can be in either liquid (broth) or solidified (e.g. with agar) forms. This field
  accepts terms listed under microbiological culture medium (http://purl.obolibrary.org/obo/MICRO_0000067).
  If the proper descriptor is not listed please use text to describe the culture medium
title: microbiological culture medium
notes:
- culture
- microbiological
examples:
- value: brain heart infusion agar [MICRO:0000566]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001216
multivalued: false
alias: microb_cult_med
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>