# Slot: growth_facil


_Type of facility where the sampled plant was grown; controlled vocabulary: growth chamber, open top chamber, glasshouse, experimental garden, field. Alternatively use Crop Ontology (CO) terms, see http://www.cropontology.org/ontology/CO_715/Crop%20Research_



URI: [MIXS:0001043](https://w3id.org/mixs/0001043)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Growth chamber [CO_715:0000189] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | free text or CO |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: growth_facil
annotations:
  Expected_value:
    tag: Expected_value
    value: free text or CO
description: 'Type of facility where the sampled plant was grown; controlled vocabulary:
  growth chamber, open top chamber, glasshouse, experimental garden, field. Alternatively
  use Crop Ontology (CO) terms, see http://www.cropontology.org/ontology/CO_715/Crop%20Research'
title: growth facility
notes:
- facility
- growth
examples:
- value: Growth chamber [CO_715:0000189]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001043
multivalued: false
alias: growth_facil
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>