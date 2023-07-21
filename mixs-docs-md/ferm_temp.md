# Slot: ferm_temp


_The temperature of the fermented food fermentation process_



URI: [MIXS:0001191](https://w3id.org/mixs/0001191)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 22 degrees Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: ferm_temp
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: The temperature of the fermented food fermentation process
title: fermentation temperature
notes:
- fermentation
- temperature
examples:
- value: 22 degrees Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001191
multivalued: false
alias: ferm_temp
domain_of:
- FoodHumanFoods
range: string
recommended: true
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>