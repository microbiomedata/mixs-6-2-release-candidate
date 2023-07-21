# Slot: farm_equip_san

URI: [MIXS:0001124](https://w3id.org/mixs/0001124)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| hot water pressure wash, hypochlorite solution, 50 parts per million |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | text or commercial name of sanitizer or class of sanitizer or active ingredient in sanitizer || Preferred_unit | parts per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: farm_equip_san
annotations:
  Expected_value:
    tag: Expected_value
    value: text or commercial name of sanitizer or class of sanitizer or active ingredient
      in sanitizer
  Preferred_unit:
    tag: Preferred_unit
    value: parts per million
title: farm equipment sanitization
notes:
- equipment
- farm
examples:
- value: hot water pressure wash, hypochlorite solution, 50 parts per million
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text} {float} {unit}'
slot_uri: MIXS:0001124
multivalued: true
alias: farm_equip_san
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>