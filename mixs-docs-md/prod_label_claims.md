# Slot: prod_label_claims


_Labeling claims containing descriptors such as wild caught, free-range, organic, free-range, industrial, hormone-free, antibiotic free, cage free. Can include more than one term, separated by ";"_



URI: [mixs_6_2_proposal:prod_label_claims](https://turbomam.github.io/mixs-envo-struct-knowl-extraction/prod_label_claims)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| free range |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: prod_label_claims
description: Labeling claims containing descriptors such as wild caught, free-range,
  organic, free-range, industrial, hormone-free, antibiotic free, cage free. Can include
  more than one term, separated by ";"
title: production labeling claims
notes:
- production
examples:
- value: free range
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
multivalued: true
alias: prod_label_claims
domain_of:
- FoodFarmEnvironment
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>