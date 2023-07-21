# Slot: food_source_age


_The age of the food source host organim. Depending on the type of host organism, age may be more appropriate to report in days, weeks, or years_



URI: [MIXS:0001251](https://w3id.org/mixs/0001251)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 6 months |

## Comments

* ISO 8601 period or measurement value?

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | days |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: food_source_age
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: days
description: The age of the food source host organim. Depending on the type of host
  organism, age may be more appropriate to report in days, weeks, or years
title: food source age
notes:
- age
- food
- source
comments:
- ISO 8601 period or measurement value?
examples:
- value: 6 months
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001251
alias: food_source_age
domain_of:
- FoodAnimalAndAnimalFeed
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>