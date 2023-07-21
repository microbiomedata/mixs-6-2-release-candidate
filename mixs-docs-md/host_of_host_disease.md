# Slot: host_of_host_disease


_List of diseases with which the host of the symbiotic host organism has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from the DO (Human Disease Ontology) at https://www.disease-ontology.org, non-human host diseases are free text_



URI: [MIXS:0001319](https://w3id.org/mixs/0001319)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| rabies [DOID:11260] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | disease name or Disease Ontology term |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_of_host_disease
annotations:
  Expected_value:
    tag: Expected_value
    value: disease name or Disease Ontology term
description: List of diseases with which the host of the symbiotic host organism has
  been diagnosed; can include multiple diagnoses. The value of the field depends on
  host; for humans the terms should be chosen from the DO (Human Disease Ontology)
  at https://www.disease-ontology.org, non-human host diseases are free text
title: host of the symbiotic host disease status
notes:
- disease
- host
- host.
- status
- symbiosis
examples:
- value: rabies [DOID:11260]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{termLabel} [{termID}]|{text}'
slot_uri: MIXS:0001319
multivalued: true
alias: host_of_host_disease
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>