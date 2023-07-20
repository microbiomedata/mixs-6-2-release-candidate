# Slot: ferm_chem_add


_Any chemicals that are added to the fermentation process to achieve the desired final product_



URI: [MIXS:0001185](https://w3id.org/mixs/0001185)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Recommended: True






## Examples

| Value |
| --- |
| salt |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | chemical ingredient |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ferm_chem_add
annotations:
  Expected_value:
    tag: Expected_value
    value: chemical ingredient
description: Any chemicals that are added to the fermentation process to achieve the
  desired final product
title: fermentation chemical additives
notes:
- fermentation
examples:
- value: salt
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {unit}'
slot_uri: MIXS:0001185
multivalued: true
alias: ferm_chem_add
domain_of:
- FoodHumanFoods
range: string
recommended: true

```
</details>