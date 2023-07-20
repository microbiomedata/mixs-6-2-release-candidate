# Slot: cult_target


_The target microbial analyte in terms of investigation scope. This field accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy_



URI: [MIXS:0001119](https://w3id.org/mixs/0001119)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Listeria monocytogenes [NCIT:C86502] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C14250 or NCBI taxid or culture independent |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: cult_target
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or NCBI taxid or culture independent
description: The target microbial analyte in terms of investigation scope. This field
  accepts terms under organism (http://purl.obolibrary.org/obo/NCIT_C14250). This
  field also accepts identification numbers from NCBI under https://www.ncbi.nlm.nih.gov/taxonomy
title: culture target microbial analyte
notes:
- culture
- microbial
- target
examples:
- value: Listeria monocytogenes [NCIT:C86502]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001119
multivalued: true
alias: cult_target
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>