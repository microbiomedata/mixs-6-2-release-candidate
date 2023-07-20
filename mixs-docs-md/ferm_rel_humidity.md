# Slot: ferm_rel_humidity


_The relative humidity of the fermented food fermentation process_



URI: [MIXS:0001190](https://w3id.org/mixs/0001190)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `[0-9]*\.?[0-9]+ ?%`






## Examples

| Value |
| --- |
| 95% |

## Comments

* percent or float?

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ferm_rel_humidity
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: The relative humidity of the fermented food fermentation process
title: fermentation relative humidity
notes:
- fermentation
- humidity
- relative
comments:
- percent or float?
examples:
- value: 95%
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001190
alias: ferm_rel_humidity
domain_of:
- FoodHumanFoods
range: string
recommended: true
pattern: '[0-9]*\.?[0-9]+ ?%'

```
</details>