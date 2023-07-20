# Slot: ferm_time


_The time duration of the fermented food fermentation process_



URI: [MIXS:0001192](https://w3id.org/mixs/0001192)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$`






## Examples

| Value |
| --- |
| P10D |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | days |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ferm_time
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: days
description: The time duration of the fermented food fermentation process
title: fermentation time
notes:
- fermentation
- time
examples:
- value: P10D
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001192
multivalued: false
alias: ferm_time
domain_of:
- FoodHumanFoods
range: string
recommended: true
pattern: ^P(?!$)(\d+Y)?(\d+M)?(\d+W)?(\d+D)?(T(?=\d+[HMS])(\d+H)?(\d+M)?(\d+S)?)?$

```
</details>