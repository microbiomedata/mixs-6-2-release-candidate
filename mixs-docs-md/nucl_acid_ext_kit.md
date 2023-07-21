# Slot: nucl_acid_ext_kit


_The name of the extraction kit used to recover the nucleic acid fraction of an input material is performed_



URI: [MIXS:0001223](https://w3id.org/mixs/0001223)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Qiagen PowerSoil Kit |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | The name of an extraction kit |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: nucl_acid_ext_kit
annotations:
  Expected_value:
    tag: Expected_value
    value: The name of an extraction kit
description: The name of the extraction kit used to recover the nucleic acid fraction
  of an input material is performed
title: nucleic acid extraction kit
notes:
- kit
examples:
- value: Qiagen PowerSoil Kit
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001223
multivalued: true
alias: nucl_acid_ext_kit
domain_of:
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>