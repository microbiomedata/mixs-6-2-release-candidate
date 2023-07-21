# Slot: animal_intrusion


_Identification of animals intruding on the sample or sample site including invertebrates (such as pests or pollinators) and vertebrates (such as wildlife or domesticated animals). This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy. Multiple terms can be separated by pipes_



URI: [MIXS:0001114](https://w3id.org/mixs/0001114)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Thripidae [NCBITaxon:45053] |

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
name: animal_intrusion
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or NCBI taxid
description: Identification of animals intruding on the sample or sample site including
  invertebrates (such as pests or pollinators) and vertebrates (such as wildlife or
  domesticated animals). This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250).
  This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy.
  Multiple terms can be separated by pipes
title: animal intrusion near sample source
notes:
- animal
- sample
- source
examples:
- value: Thripidae [NCBITaxon:45053]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{termLabel} [{termID}]|{integer}'
slot_uri: MIXS:0001114
multivalued: true
alias: animal_intrusion
domain_of:
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>