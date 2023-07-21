# Slot: root_med_micronutr

URI: [MIXS:0000579](https://w3id.org/mixs/0000579)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| H3BO3;6.2milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | micronutrient name;measurement value || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: root_med_micronutr
annotations:
  Expected_value:
    tag: Expected_value
    value: micronutrient name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
title: rooting medium micronutrients
notes:
- micronutrients
examples:
- value: H3BO3;6.2milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000579
multivalued: false
alias: root_med_micronutr
domain_of:
- FoodFarmEnvironment
- PlantAssociated
range: string
required: false
recommended: false

```
</details>