# Slot: rainfall_regm


_Information about treatment involving an exposure to a given amount of rainfall, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000576](https://w3id.org/mixs/0000576)



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
| 15 millimeter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value;treatment interval and duration || Preferred_unit | millimeter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: rainfall_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: millimeter
description: Information about treatment involving an exposure to a given amount of
  rainfall, treatment regimen including how many times the treatment was repeated,
  how long each treatment lasted, and the start and end time of the entire treatment;
  can include multiple regimens
title: rainfall regimen
notes:
- rain
- regimen
examples:
- value: 15 millimeter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000576
multivalued: true
alias: rainfall_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>