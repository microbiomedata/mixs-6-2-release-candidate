# Slot: coll_site_geo_feat


_Text or terms that describe the geographic feature where the food sample was obtained by the researcher. This field accepts selected terms listed under the following ontologies: anthropogenic geographic feature (http://purl.obolibrary.org/obo/ENVO_00000002), for example agricultural fairground [ENVO:01000986]; garden [ENVO:00000011} or any of its subclasses; market [ENVO:01000987]; water well [ENVO:01000002]; or human construction (http://purl.obolibrary.org/obo/ENVO_00000070)_



URI: [MIXS:0001183](https://w3id.org/mixs/0001183)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True






## Examples

| Value |
| --- |
| farm [ENVO:00000078] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | ENVO:00000002 or ENVO:00000070 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: coll_site_geo_feat
annotations:
  Expected_value:
    tag: Expected_value
    value: ENVO:00000002 or ENVO:00000070
description: 'Text or terms that describe the geographic feature where the food sample
  was obtained by the researcher. This field accepts selected terms listed under the
  following ontologies: anthropogenic geographic feature (http://purl.obolibrary.org/obo/ENVO_00000002),
  for example agricultural fairground [ENVO:01000986]; garden [ENVO:00000011} or any
  of its subclasses; market [ENVO:01000987]; water well [ENVO:01000002]; or human
  construction (http://purl.obolibrary.org/obo/ENVO_00000070)'
title: collection site geographic feature
notes:
- feature
- geographic
- site
examples:
- value: farm [ENVO:00000078]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001183
multivalued: false
alias: coll_site_geo_feat
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: true

```
</details>