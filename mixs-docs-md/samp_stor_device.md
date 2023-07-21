# Slot: samp_stor_device


_The container used to store the  sample. This field accepts terms listed under container (http://purl.obolibrary.org/obo/NCIT_C43186). If the proper descriptor is not listed please use text to describe the storage device_



URI: [MIXS:0001228](https://w3id.org/mixs/0001228)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Whirl Pak sampling bag [GENEPIO:0002122] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C4318 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_stor_device
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C4318
description: The container used to store the  sample. This field accepts terms listed
  under container (http://purl.obolibrary.org/obo/NCIT_C43186). If the proper descriptor
  is not listed please use text to describe the storage device
title: sample storage device
notes:
- device
- sample
- storage
examples:
- value: Whirl Pak sampling bag [GENEPIO:0002122]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001228
multivalued: false
alias: samp_stor_device
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string

```
</details>