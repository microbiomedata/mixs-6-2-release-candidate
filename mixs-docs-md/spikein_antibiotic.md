# Slot: spikein_antibiotic


_Antimicrobials used in research study to assess effects of exposure on microbiome of a specific site.  Please list antimicrobial, common name and/or class and concentration used for spike-in_



URI: [MIXS:0001171](https://w3id.org/mixs/0001171)



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
| Tetracycline at 5 mg/ml |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | drug name; concentration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: spikein_antibiotic
annotations:
  Expected_value:
    tag: Expected_value
    value: drug name; concentration
description: Antimicrobials used in research study to assess effects of exposure on
  microbiome of a specific site.  Please list antimicrobial, common name and/or class
  and concentration used for spike-in
title: spike-in with antibiotics
notes:
- spike
examples:
- value: Tetracycline at 5 mg/ml
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text} {integer}'
slot_uri: MIXS:0001171
multivalued: true
alias: spikein_antibiotic
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>