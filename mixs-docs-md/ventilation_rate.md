# Slot: ventilation_rate


_Ventilation rate of the system in the sampled premises_



URI: [MIXS:0000114](https://w3id.org/mixs/0000114)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 750 cubic meter per minute |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | cubic meter per minute, liters per second |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ventilation_rate
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: cubic meter per minute, liters per second
description: Ventilation rate of the system in the sampled premises
title: ventilation rate
notes:
- rate
examples:
- value: 750 cubic meter per minute
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000114
multivalued: false
alias: ventilation_rate
domain_of:
- Air
- FoodFarmEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>