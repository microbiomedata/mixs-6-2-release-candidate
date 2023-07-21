# Slot: ph_regm


_Information about treatment involving exposure of plants to varying levels of ph of the growth media, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimen_



URI: [MIXS:0001056](https://w3id.org/mixs/0001056)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 7.6;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: ph_regm
description: Information about treatment involving exposure of plants to varying levels
  of ph of the growth media, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple regimen
title: pH regimen
notes:
- ph
- regimen
examples:
- value: 7.6;R2/2018-05-11:T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001056
multivalued: true
alias: ph_regm
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>