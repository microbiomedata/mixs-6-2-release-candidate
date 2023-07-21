# Slot: special_diet


_Specification of special diet; can include multiple special diets_



URI: [MIXS:0000905](https://w3id.org/mixs/0000905)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanGut](HumanGut.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| other:vegan |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: special_diet
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: Specification of special diet; can include multiple special diets
title: special diet
notes:
- diet
examples:
- value: other:vegan
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[low carb|reduced calorie|vegetarian|other(to be specified)]'
slot_uri: MIXS:0000905
multivalued: true
alias: special_diet
domain_of:
- HumanGut
range: string
required: false
recommended: false

```
</details>