# Slot: watering_regm


_Information about treatment involving an exposure to watering frequencies, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0000591](https://w3id.org/mixs/0000591)



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
| 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milliliter, liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: watering_regm
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milliliter, liter
description: Information about treatment involving an exposure to watering frequencies,
  treatment regimen including how many times the treatment was repeated, how long
  each treatment lasted, and the start and end time of the entire treatment; can include
  multiple regimens
title: watering regimen
notes:
- regimen
- water
examples:
- value: 1 liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000591
multivalued: true
alias: watering_regm
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>