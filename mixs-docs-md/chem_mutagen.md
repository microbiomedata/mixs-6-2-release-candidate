# Slot: chem_mutagen


_Treatment involving use of mutagens; should include the name of mutagen, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple mutagen regimens_



URI: [MIXS:0000555](https://w3id.org/mixs/0000555)



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
| nitrous acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | mutagen name;mutagen amount;treatment interval and duration || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: chem_mutagen
annotations:
  Expected_value:
    tag: Expected_value
    value: mutagen name;mutagen amount;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Treatment involving use of mutagens; should include the name of mutagen,
  amount administered, treatment regimen including how many times the treatment was
  repeated, how long each treatment lasted, and the start and end time of the entire
  treatment; can include multiple mutagen regimens
title: chemical mutagen
examples:
- value: nitrous acid;0.5 milligram per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000555
multivalued: true
alias: chem_mutagen
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>