# Slot: diet_last_six_month


_Specification of major diet changes in the last six months, if yes the change should be specified_



URI: [MIXS:0000266](https://w3id.org/mixs/0000266)



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
| yes;vegetarian diet |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | diet change;current diet |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: diet_last_six_month
annotations:
  Expected_value:
    tag: Expected_value
    value: diet change;current diet
description: Specification of major diet changes in the last six months, if yes the
  change should be specified
title: major diet change in last six months
notes:
- diet
- months
examples:
- value: yes;vegetarian diet
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{boolean};{text}'
slot_uri: MIXS:0000266
multivalued: false
alias: diet_last_six_month
domain_of:
- HumanAssociated
range: string
required: false
recommended: false

```
</details>