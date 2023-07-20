# Slot: ferm_headspace_oxy


_The amount of headspace oxygen in a fermentation vessel_



URI: [MIXS:0001187](https://w3id.org/mixs/0001187)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True






## Examples

| Value |
| --- |
| 0.05 |

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
name: ferm_headspace_oxy
annotations:
  Expected_value:
    tag: Expected_value
    value: value
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: The amount of headspace oxygen in a fermentation vessel
title: fermentation headspace oxygen
notes:
- fermentation
- oxygen
examples:
- value: '0.05'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} percentage'
slot_uri: MIXS:0001187
multivalued: false
alias: ferm_headspace_oxy
domain_of:
- FoodHumanFoods
range: string
recommended: true

```
</details>