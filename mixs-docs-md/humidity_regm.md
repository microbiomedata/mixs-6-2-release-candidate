# Slot: humidity_regm


_Information about treatment involving an exposure to varying degree of humidity; information about treatment involving use of growth hormones; should include amount of humidity administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000568](https://w3id.org/mixs/0000568)



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
| 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | humidity value;treatment interval and duration || Preferred_unit | gram per cubic meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: humidity_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: humidity value;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: gram per cubic meter
description: Information about treatment involving an exposure to varying degree of
  humidity; information about treatment involving use of growth hormones; should include
  amount of humidity administered, treatment regimen including how many times the
  treatment was repeated, how long each treatment lasted, and the start and end time
  of the entire treatment; can include multiple regimens
title: humidity regimen
notes:
- humidity
- regimen
examples:
- value: 25 gram per cubic meter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000568
multivalued: true
alias: humidity_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>