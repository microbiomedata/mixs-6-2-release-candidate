# Slot: study_tmnt


_A process in which the act is intended to modify or alter some other material entity.  From the study design, each treatment is comprised of one level of one or multiple factors. This field accepts terms listed under treatment (http://purl.obolibrary.org/obo/MCO_0000866). If the proper descriptor is not listed please use text to describe the study treatment. Multiple terms can be separated by one or more pipes_



URI: [MIXS:0001240](https://w3id.org/mixs/0001240)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Factor A|spike-in|levels high, medium, low |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | MCO:0000866 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: study_tmnt
annotations:
  Expected_value:
    tag: Expected_value
    value: MCO:0000866
description: A process in which the act is intended to modify or alter some other
  material entity.  From the study design, each treatment is comprised of one level
  of one or multiple factors. This field accepts terms listed under treatment (http://purl.obolibrary.org/obo/MCO_0000866).
  If the proper descriptor is not listed please use text to describe the study treatment.
  Multiple terms can be separated by one or more pipes
title: study treatment
notes:
- treatment
examples:
- value: Factor A|spike-in|levels high, medium, low
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001240
multivalued: true
alias: study_tmnt
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>