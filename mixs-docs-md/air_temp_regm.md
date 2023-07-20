# Slot: air_temp_regm


_Information about treatment involving an exposure to varying temperatures; should include the temperature, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include different temperature regimens_



URI: [MIXS:0000551](https://w3id.org/mixs/0000551)



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
| 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | temperature value;treatment interval and duration || Preferred_unit | meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: air_temp_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: temperature value;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: meter
description: Information about treatment involving an exposure to varying temperatures;
  should include the temperature, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include different temperature regimens
title: air temperature regimen
notes:
- air
- regimen
- temperature
examples:
- value: 25 degree Celsius;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000551
multivalued: true
alias: air_temp_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>