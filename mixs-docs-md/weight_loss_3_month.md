# Slot: weight_loss_3_month


_Specification of weight loss in the last three months, if yes should be further specified to include amount of weight loss_



URI: [MIXS:0000295](https://w3id.org/mixs/0000295)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| yes;5 kilogram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | weight loss specification;measurement value || Preferred_unit | kilogram, gram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: weight_loss_3_month
annotations:
  Expected_value:
    tag: Expected_value
    value: weight loss specification;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: kilogram, gram
description: Specification of weight loss in the last three months, if yes should
  be further specified to include amount of weight loss
title: weight loss in last three months
notes:
- months
- weight
examples:
- value: yes;5 kilogram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{boolean};{float} {unit}'
slot_uri: MIXS:0000295
multivalued: false
alias: weight_loss_3_month
domain_of:
- HumanAssociated
range: string
required: false
recommended: false

```
</details>