# Slot: spikein_AMR


_Qualitative description of a microbial response to antimicrobial agents. Bacteria may be susceptible or resistant to a broad range of antibiotic drugs or drug classes, with several intermediate states or phases. This field accepts terms under antimicrobial phenotype (http://purl.obolibrary.org/obo/ARO_3004299)_



URI: [MIXS:0001235](https://w3id.org/mixs/0001235)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| wild type [ARO:3004432] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value ARO:3004299 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: spikein_AMR
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value ARO:3004299
description: Qualitative description of a microbial response to antimicrobial agents.
  Bacteria may be susceptible or resistant to a broad range of antibiotic drugs or
  drug classes, with several intermediate states or phases. This field accepts terms
  under antimicrobial phenotype (http://purl.obolibrary.org/obo/ARO_3004299)
title: antimicrobial phenotype of spike-in bacteria
notes:
- antimicrobial
- spike
examples:
- value: wild type [ARO:3004432]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} {unit};{termLabel} [{termID}]'
slot_uri: MIXS:0001235
multivalued: true
alias: spikein_AMR
domain_of:
- FoodAnimalAndAnimalFeed
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>