# Slot: spikein_org


_Taxonomic information about the spike-in organism(s). This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy. Multiple terms can be separated by pipes_



URI: [MIXS:0001167](https://w3id.org/mixs/0001167)



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
| Listeria monocytogenes [NCIT:C86502]|28901 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C14250 or NCBI taxid |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: spikein_org
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or NCBI taxid
description: Taxonomic information about the spike-in organism(s). This field accepts
  terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also
  accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy.
  Multiple terms can be separated by pipes
title: spike in organism
notes:
- organism
- spike
examples:
- value: Listeria monocytogenes [NCIT:C86502]|28901
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{termLabel} [{termID}]|{integer}'
slot_uri: MIXS:0001167
multivalued: true
alias: spikein_org
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>