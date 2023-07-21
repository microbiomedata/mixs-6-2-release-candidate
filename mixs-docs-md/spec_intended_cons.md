# Slot: spec_intended_cons


_Food consumer type, human or animal, for which the food product is produced and marketed. This field accepts terms listed under food consumer group (http://purl.obolibrary.org/obo/FOODON_03510136)_



URI: [MIXS:0001234](https://w3id.org/mixs/0001234)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| senior as food consumer [FOODON:03510254] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: spec_intended_cons
description: Food consumer type, human or animal, for which the food product is produced
  and marketed. This field accepts terms listed under food consumer group (http://purl.obolibrary.org/obo/FOODON_03510136)
title: specific intended consumer
notes:
- consumer
examples:
- value: senior as food consumer [FOODON:03510254]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001234
multivalued: true
alias: spec_intended_cons
domain_of:
- FoodFoodProductionFacility
range: string
required: false
recommended: false
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>