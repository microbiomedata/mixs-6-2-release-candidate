# Slot: animal_housing


_Description of the housing system of the livestock. This field accepts terms listed under terrestrial management housing system (http://opendata.inra.fr/EOL/EOL_0001605)_



URI: [MIXS:0001180](https://w3id.org/mixs/0001180)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| pen rearing system [EOL:0001636] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: animal_housing
description: Description of the housing system of the livestock. This field accepts
  terms listed under terrestrial management housing system (http://opendata.inra.fr/EOL/EOL_0001605)
title: animal housing system
notes:
- animal
examples:
- value: pen rearing system [EOL:0001636]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001180
multivalued: true
alias: animal_housing
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
range: string
required: false
recommended: false
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>