# Slot: climate_environment


_Treatment involving an exposure to a particular climate; treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple climates_



URI: [MIXS:0001040](https://w3id.org/mixs/0001040)



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
| tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: climate_environment
description: Treatment involving an exposure to a particular climate; treatment regimen
  including how many times the treatment was repeated, how long each treatment lasted,
  and the start and end time of the entire treatment; can include multiple climates
title: climate environment
notes:
- environment
examples:
- value: tropical climate;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001040
multivalued: true
alias: climate_environment
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>