# Slot: antibiotic_regm


_Information about treatment involving antibiotic administration; should include the name of antibiotic, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple antibiotic regimens_



URI: [MIXS:0000553](https://w3id.org/mixs/0000553)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| penicillin;5 milligram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | antibiotic name;antibiotic amount;treatment interval and duration || Preferred_unit | milligram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: antibiotic_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: antibiotic name;antibiotic amount;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: milligram
description: Information about treatment involving antibiotic administration; should
  include the name of antibiotic, amount administered, treatment regimen including
  how many times the treatment was repeated, how long each treatment lasted, and the
  start and end time of the entire treatment; can include multiple antibiotic regimens
title: antibiotic regimen
notes:
- regimen
examples:
- value: penicillin;5 milligram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000553
multivalued: true
alias: antibiotic_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>