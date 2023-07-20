# Slot: standing_water_regm


_Treatment involving an exposure to standing water during a plant's life span, types can be flood water or standing water, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens_



URI: [MIXS:0001069](https://w3id.org/mixs/0001069)



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
| standing water;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: standing_water_regm
description: Treatment involving an exposure to standing water during a plant's life
  span, types can be flood water or standing water, treatment regimen including how
  many times the treatment was repeated, how long each treatment lasted, and the start
  and end time of the entire treatment; can include multiple regimens
title: standing water regimen
notes:
- regimen
- water
examples:
- value: standing water;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001069
multivalued: true
alias: standing_water_regm
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>