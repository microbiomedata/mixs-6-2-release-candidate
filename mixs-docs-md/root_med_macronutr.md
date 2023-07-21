# Slot: root_med_macronutr

URI: [MIXS:0000578](https://w3id.org/mixs/0000578)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| KH2PO4;170milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | macronutrient name;measurement value || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: root_med_macronutr
annotations:
  Expected_value:
    tag: Expected_value
    value: macronutrient name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
title: rooting medium macronutrients
notes:
- macronutrients
examples:
- value: KH2PO4;170milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000578
multivalued: false
alias: root_med_macronutr
domain_of:
- Agriculture
- FoodFarmEnvironment
- PlantAssociated
range: string
required: false
recommended: false

```
</details>