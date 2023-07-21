# Slot: root_med_carbon


_Source of organic carbon in the culture rooting medium; e.g. sucrose_



URI: [MIXS:0000577](https://w3id.org/mixs/0000577)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| sucrose |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | carbon source name;measurement value || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: root_med_carbon
annotations:
  Expected_value:
    tag: Expected_value
    value: carbon source name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Source of organic carbon in the culture rooting medium; e.g. sucrose
title: rooting medium carbon
notes:
- carbon
examples:
- value: sucrose
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000577
multivalued: false
alias: root_med_carbon
domain_of:
- Agriculture
- FoodFarmEnvironment
- PlantAssociated
range: string
required: false
recommended: false

```
</details>