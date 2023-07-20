# Slot: plant_struc


_Name of plant structure the sample was obtained from; for Plant Ontology (PO) (v releases/2017-12-14) terms, see http://purl.bioontology.org/ontology/PO, e.g. petiole epidermis (PO_0000051). If an individual flower is sampled, the sex of it can be recorded here_



URI: [MIXS:0001060](https://w3id.org/mixs/0001060)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| epidermis [PO:0005679] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: plant_struc
description: Name of plant structure the sample was obtained from; for Plant Ontology
  (PO) (v releases/2017-12-14) terms, see http://purl.bioontology.org/ontology/PO,
  e.g. petiole epidermis (PO_0000051). If an individual flower is sampled, the sex
  of it can be recorded here
title: plant structure
notes:
- plant
examples:
- value: epidermis [PO:0005679]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001060
multivalued: false
alias: plant_struc
domain_of:
- Agriculture
- PlantAssociated
range: string
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>