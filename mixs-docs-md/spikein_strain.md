# Slot: spikein_strain


_Taxonomic information about the spike-in organism(s) at the strain level. This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy. Multiple terms can be separated by pipes_



URI: [MIXS:0001170](https://w3id.org/mixs/0001170)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 169963 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C14250 or NCBI taxid or text |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: spikein_strain
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or NCBI taxid or text
description: Taxonomic information about the spike-in organism(s) at the strain level.
  This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250).
  This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy.
  Multiple terms can be separated by pipes
title: spike-in microbial strain
notes:
- microbial
- spike
examples:
- value: '169963'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{termLabel} [{termID}]|{integer}'
slot_uri: MIXS:0001170
multivalued: true
alias: spikein_strain
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>