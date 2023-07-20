# Slot: growth_hormone_regm


_Information about treatment involving use of growth hormones; should include the name of growth hormone, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple growth hormone regimens_



URI: [MIXS:0000560](https://w3id.org/mixs/0000560)



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
| abscisic acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | growth hormone name;growth hormone amount;treatment interval and duration || Preferred_unit | gram, mole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: growth_hormone_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: growth hormone name;growth hormone amount;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: gram, mole per liter, milligram per liter
description: Information about treatment involving use of growth hormones; should
  include the name of growth hormone, amount administered, treatment regimen including
  how many times the treatment was repeated, how long each treatment lasted, and the
  start and end time of the entire treatment; can include multiple growth hormone
  regimens
title: growth hormone regimen
notes:
- growth
- regimen
examples:
- value: abscisic acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000560
multivalued: true
alias: growth_hormone_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>