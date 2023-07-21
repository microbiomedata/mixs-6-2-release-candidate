# Slot: gravity


_Information about treatment involving use of gravity factor to study various types of responses in presence, absence or modified levels of gravity; treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple treatments_



URI: [MIXS:0000559](https://w3id.org/mixs/0000559)



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
| 12 g;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | gravity factor value;treatment interval and duration || Preferred_unit | meter per square second, g |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: gravity
annotations:
  Expected_value:
    tag: Expected_value
    value: gravity factor value;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: meter per square second, g
description: Information about treatment involving use of gravity factor to study
  various types of responses in presence, absence or modified levels of gravity; treatment
  regimen including how many times the treatment was repeated, how long each treatment
  lasted, and the start and end time of the entire treatment; can include multiple
  treatments
title: gravity
examples:
- value: 12 g;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000559
multivalued: true
alias: gravity
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>