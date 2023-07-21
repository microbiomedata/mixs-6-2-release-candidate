# Slot: ster_meth_samp_room


_The method used to sterilize the sampling room. This field accepts terms listed under electromagnetic radiation (http://purl.obolibrary.org/obo/ENVO_01001026). If the proper descriptor is not listed, please use text to describe the sampling room sterilization method. Multiple terms can be separated by pipes_



URI: [MIXS:0001259](https://w3id.org/mixs/0001259)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| ultraviolet radiation [ENVO:21001216]|infrared radiation [ENVO:21001214] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | ENVO:01001026 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: ster_meth_samp_room
annotations:
  Expected_value:
    tag: Expected_value
    value: ENVO:01001026
description: The method used to sterilize the sampling room. This field accepts terms
  listed under electromagnetic radiation (http://purl.obolibrary.org/obo/ENVO_01001026).
  If the proper descriptor is not listed, please use text to describe the sampling
  room sterilization method. Multiple terms can be separated by pipes
title: sampling room sterilization method
notes:
- method
- room
examples:
- value: ultraviolet radiation [ENVO:21001216]|infrared radiation [ENVO:21001214]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001259
multivalued: true
alias: ster_meth_samp_room
domain_of:
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>