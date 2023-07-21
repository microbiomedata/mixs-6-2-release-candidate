# Slot: birth_control


_Specification of birth control medication used_



URI: [MIXS:0000286](https://w3id.org/mixs/0000286)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanVaginal](HumanVaginal.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | medication name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: birth_control
annotations:
  Expected_value:
    tag: Expected_value
    value: medication name
description: Specification of birth control medication used
title: birth control
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000286
multivalued: false
alias: birth_control
domain_of:
- HumanVaginal
range: string
required: false
recommended: false

```
</details>