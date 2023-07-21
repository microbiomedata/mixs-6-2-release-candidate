# Slot: microb_start_inoc


_The amount of starter culture used to inoculate a new batch_



URI: [MIXS:0001219](https://w3id.org/mixs/0001219)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 100 milligrams |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram or gram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: microb_start_inoc
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram or gram
description: The amount of starter culture used to inoculate a new batch
title: microbial starter inoculation
notes:
- microbial
examples:
- value: 100 milligrams
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001219
multivalued: false
alias: microb_start_inoc
domain_of:
- FoodHumanFoods
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>