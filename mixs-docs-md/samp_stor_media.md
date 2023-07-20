# Slot: samp_stor_media


_The liquid that is added to the sample collection device prior to sampling. If the sample is pre-hydrated, indicate the liquid media the sample is pre-hydrated with for storage purposes. This field accepts terms listed under microbiological culture medium (http://purl.obolibrary.org/obo/MICRO_0000067). If the proper descriptor is not listed please use text to describe the sample storage media_



URI: [MIXS:0001229](https://w3id.org/mixs/0001229)



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
| peptone water medium [MICRO:0000548] |

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
name: samp_stor_media
annotations:
  Expected_value:
    tag: Expected_value
    value: MICRO:0000067
description: The liquid that is added to the sample collection device prior to sampling.
  If the sample is pre-hydrated, indicate the liquid media the sample is pre-hydrated
  with for storage purposes. This field accepts terms listed under microbiological
  culture medium (http://purl.obolibrary.org/obo/MICRO_0000067). If the proper descriptor
  is not listed please use text to describe the sample storage media
title: sample storage media
notes:
- sample
- storage
examples:
- value: peptone water medium [MICRO:0000548]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001229
multivalued: false
alias: samp_stor_media
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string

```
</details>