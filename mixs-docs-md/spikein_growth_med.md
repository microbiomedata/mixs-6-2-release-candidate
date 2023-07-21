# Slot: spikein_growth_med


_A liquid or gel containing nutrients, salts, and other factors formulated to support the growth of microorganisms, cells, or plants (National Cancer Institute Thesaurus).  A growth medium is a culture medium which has the disposition to encourage growth of particular bacteria to the exclusion of others in the same growth environment.  In this case, list the culture medium used to propagate the spike-in bacteria during preparation of spike-in inoculum. This field accepts terms listed under microbiological culture medium (http://purl.obolibrary.org/obo/MICRO_0000067). If the proper descriptor is not listed please use text to describe the spike in growth media_



URI: [MIXS:0001169](https://w3id.org/mixs/0001169)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| LB broth [MCO:0000036] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | MICRO:0000067 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: spikein_growth_med
annotations:
  Expected_value:
    tag: Expected_value
    value: MICRO:0000067
description: A liquid or gel containing nutrients, salts, and other factors formulated
  to support the growth of microorganisms, cells, or plants (National Cancer Institute
  Thesaurus).  A growth medium is a culture medium which has the disposition to encourage
  growth of particular bacteria to the exclusion of others in the same growth environment.  In
  this case, list the culture medium used to propagate the spike-in bacteria during
  preparation of spike-in inoculum. This field accepts terms listed under microbiological
  culture medium (http://purl.obolibrary.org/obo/MICRO_0000067). If the proper descriptor
  is not listed please use text to describe the spike in growth media
title: spike-in growth medium
notes:
- growth
- spike
examples:
- value: LB broth [MCO:0000036]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001169
multivalued: true
alias: spikein_growth_med
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>