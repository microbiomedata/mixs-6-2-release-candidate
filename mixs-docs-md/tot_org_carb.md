# Slot: tot_org_carb


_Definition for soil: total organic carbon content of the soil, definition otherwise: total organic carbon content_



URI: [MIXS:0000533](https://w3id.org/mixs/0000533)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 0.02 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram Carbon per kilogram sample material |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: tot_org_carb
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram Carbon per kilogram sample material
description: 'Definition for soil: total organic carbon content of the soil, definition
  otherwise: total organic carbon content'
title: total organic carbon
notes:
- carbon
- organic
- total
examples:
- value: '0.02'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000533
multivalued: false
alias: tot_org_carb
domain_of:
- Agriculture
- FoodFarmEnvironment
- MicrobialMatBiofilm
- Sediment
- Soil
range: string

```
</details>