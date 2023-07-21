# Slot: pet_farm_animal


_Specification of presence of pets or farm animals in the environment of subject, if yes the animals should be specified; can include multiple animals present_



URI: [MIXS:0000267](https://w3id.org/mixs/0000267)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| yes; 5 cats |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | presence status;type of animal or pet |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: pet_farm_animal
annotations:
  Expected_value:
    tag: Expected_value
    value: presence status;type of animal or pet
description: Specification of presence of pets or farm animals in the environment
  of subject, if yes the animals should be specified; can include multiple animals
  present
title: presence of pets or farm animals
notes:
- animal
- farm
- presence
examples:
- value: yes; 5 cats
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{boolean};{text}'
slot_uri: MIXS:0000267
multivalued: true
alias: pet_farm_animal
domain_of:
- HumanAssociated
range: string
required: false
recommended: false

```
</details>