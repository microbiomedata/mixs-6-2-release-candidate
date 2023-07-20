# Slot: serovar_or_serotype


_A characterization of a cell or microorganism based on the antigenic properties of the molecules on its surface. Indicate the name of a serovar or serotype of interest. This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy_



URI: [MIXS:0001157](https://w3id.org/mixs/0001157)



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
| Escherichia coli strain O157:H7 [NCIT:C86883] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C14250 or NCBI taxid |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: serovar_or_serotype
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or NCBI taxid
description: A characterization of a cell or microorganism based on the antigenic
  properties of the molecules on its surface. Indicate the name of a serovar or serotype
  of interest. This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250).
  This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy
title: serovar or serotype
examples:
- value: Escherichia coli strain O157:H7 [NCIT:C86883]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}]|{integer}'
slot_uri: MIXS:0001157
multivalued: true
alias: serovar_or_serotype
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>