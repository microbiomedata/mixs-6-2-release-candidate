# Slot: biocide_used


_Substance intended for preventing, neutralizing, destroying, repelling, or mitigating the effects of any pest or microorganism; that inhibits the growth, reproduction, and activity of organisms, including fungal cells; decreases the number of fungi or pests present; deters microbial growth and degradation of other ingredients in the formulation. Indicate the biocide used on the location where the sample was taken. Multiple terms can be separated by pipes_



URI: [MIXS:0001258](https://w3id.org/mixs/0001258)



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
| Quaternary ammonium compound|SterBac |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | commercial name of biocide, active ingredient in biocide or class of biocide |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: biocide_used
annotations:
  Expected_value:
    tag: Expected_value
    value: commercial name of biocide, active ingredient in biocide or class of biocide
description: Substance intended for preventing, neutralizing, destroying, repelling,
  or mitigating the effects of any pest or microorganism; that inhibits the growth,
  reproduction, and activity of organisms, including fungal cells; decreases the number
  of fungi or pests present; deters microbial growth and degradation of other ingredients
  in the formulation. Indicate the biocide used on the location where the sample was
  taken. Multiple terms can be separated by pipes
title: biocide
examples:
- value: Quaternary ammonium compound|SterBac
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001258
multivalued: true
alias: biocide_used
domain_of:
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>