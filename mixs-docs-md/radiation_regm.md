# Slot: radiation_regm


_Information about treatment involving exposure of plant or a plant part to a particular radiation regimen; should include the radiation type, amount or intensity administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple radiation regimens_



URI: [MIXS:0000575](https://w3id.org/mixs/0000575)



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
| gamma radiation;60 gray;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | radiation type name;radiation amount;treatment interval and duration || Preferred_unit | rad, gray |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: radiation_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: radiation type name;radiation amount;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: rad, gray
description: Information about treatment involving exposure of plant or a plant part
  to a particular radiation regimen; should include the radiation type, amount or
  intensity administered, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple radiation regimens
title: radiation regimen
notes:
- regimen
examples:
- value: gamma radiation;60 gray;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000575
multivalued: true
alias: radiation_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>