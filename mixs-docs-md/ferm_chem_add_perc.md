# Slot: ferm_chem_add_perc


_The amount of chemical added to the fermentation process_



URI: [MIXS:0001186](https://w3id.org/mixs/0001186)



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
| 0.01 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | value || Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ferm_chem_add_perc
annotations:
  Expected_value:
    tag: Expected_value
    value: value
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: The amount of chemical added to the fermentation process
title: fermentation chemical additives percentage
notes:
- fermentation
- percent
examples:
- value: '0.01'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} percentage'
slot_uri: MIXS:0001186
multivalued: true
alias: ferm_chem_add_perc
domain_of:
- FoodHumanFoods
range: string
recommended: true

```
</details>