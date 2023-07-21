# Slot: bacterial_density


_Number of bacteria in sample, as defined by bacteria density (http://purl.obolibrary.org/obo/GENEPIO_0000043)_



URI: [MIXS:0001194](https://w3id.org/mixs/0001194)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 10 colony forming units per gram dry weight |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | colony forming units per milliliter; colony forming units per gram of dry weight |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: bacterial_density
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: colony forming units per milliliter; colony forming units per gram of dry
      weight
description: Number of bacteria in sample, as defined by bacteria density (http://purl.obolibrary.org/obo/GENEPIO_0000043)
title: bacteria density
notes:
- density
examples:
- value: 10 colony forming units per gram dry weight
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001194
multivalued: false
alias: bacterial_density
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>