# Slot: study_design


_A plan specification comprised of protocols (which may specify how and what kinds of data will be gathered) that are executed as part of an investigation and is realized during a study design execution. This field accepts terms under study design (http://purl.obolibrary.org/obo/OBI_0500000). If the proper descriptor is not listed please use text to describe the study design. Multiple terms can be separated by pipes_



URI: [MIXS:0001236](https://w3id.org/mixs/0001236)



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
| in vitro design [OBI:0001285] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | OBI:0500000 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: study_design
annotations:
  Expected_value:
    tag: Expected_value
    value: OBI:0500000
description: A plan specification comprised of protocols (which may specify how and
  what kinds of data will be gathered) that are executed as part of an investigation
  and is realized during a study design execution. This field accepts terms under
  study design (http://purl.obolibrary.org/obo/OBI_0500000). If the proper descriptor
  is not listed please use text to describe the study design. Multiple terms can be
  separated by pipes
title: study design
examples:
- value: in vitro design [OBI:0001285]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001236
multivalued: true
alias: study_design
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>