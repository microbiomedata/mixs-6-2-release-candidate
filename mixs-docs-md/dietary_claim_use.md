# Slot: dietary_claim_use


_These descriptors are used either for foods intended for special dietary use as defined in 21 CFR 105 or for foods that have special characteristics indicated in the name or labeling. This field accepts terms listed under dietary claim or use (http://purl.obolibrary.org/obo/FOODON_03510023). Multiple terms can be separated by one or more pipes, but please consider limiting this list to the most prominent dietary claim or use_



URI: [MIXS:0001199](https://w3id.org/mixs/0001199)



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
| No preservatives [FOODON:03510113] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03510023 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: dietary_claim_use
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03510023
description: These descriptors are used either for foods intended for special dietary
  use as defined in 21 CFR 105 or for foods that have special characteristics indicated
  in the name or labeling. This field accepts terms listed under dietary claim or
  use (http://purl.obolibrary.org/obo/FOODON_03510023). Multiple terms can be separated
  by one or more pipes, but please consider limiting this list to the most prominent
  dietary claim or use
title: dietary claim or use
notes:
- diet
- use
examples:
- value: No preservatives [FOODON:03510113]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}|{termLabel} [{termID}]'
slot_uri: MIXS:0001199
multivalued: true
alias: dietary_claim_use
domain_of:
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>