# Slot: spikein_serovar


_Taxonomic information about the spike-in organism(s) at the serovar or serotype level. This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy. Multiple terms can be separated by pipes_



URI: [MIXS:0001168](https://w3id.org/mixs/0001168)



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
| Escherichia coli strain O157:H7 [NCIT:C86883]|83334 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C14250 or antigenic formula or serovar name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: spikein_serovar
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or antigenic formula or serovar name
description: Taxonomic information about the spike-in organism(s) at the serovar or
  serotype level. This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250).
  This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy.
  Multiple terms can be separated by pipes
title: spike-in bacterial serovar or serotype
notes:
- spike
examples:
- value: Escherichia coli strain O157:H7 [NCIT:C86883]|83334
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}]|{integer}'
slot_uri: MIXS:0001168
multivalued: true
alias: spikein_serovar
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>