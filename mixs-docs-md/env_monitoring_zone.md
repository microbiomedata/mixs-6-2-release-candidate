# Slot: env_monitoring_zone


_An environmental monitoring zone is a formal designation as part of an environmental monitoring program, in which areas of a food production facility are categorized, commonly as zones 1-4, based on likelihood or risk of foodborne pathogen contamination. This field accepts terms listed under food production environmental monitoring zone (http://purl.obolibrary.org/obo/ENVO). Please add a term to indicate the environmental monitoring zone the sample was taken from_



URI: [MIXS:0001254](https://w3id.org/mixs/0001254)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Zone 1 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: env_monitoring_zone
description: An environmental monitoring zone is a formal designation as part of an
  environmental monitoring program, in which areas of a food production facility are
  categorized, commonly as zones 1-4, based on likelihood or risk of foodborne pathogen
  contamination. This field accepts terms listed under food production environmental
  monitoring zone (http://purl.obolibrary.org/obo/ENVO). Please add a term to indicate
  the environmental monitoring zone the sample was taken from
title: food production environmental monitoring zone
notes:
- environmental
- food
- production
examples:
- value: Zone 1
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001254
multivalued: false
alias: env_monitoring_zone
domain_of:
- FoodFoodProductionFacility
range: string
required: false
recommended: false

```
</details>