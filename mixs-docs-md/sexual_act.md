# Slot: sexual_act


_Current sexual partner and frequency of sex_



URI: [MIXS:0000285](https://w3id.org/mixs/0000285)



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
| Expected_value | partner sex;frequency |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: sexual_act
annotations:
  Expected_value:
    tag: Expected_value
    value: partner sex;frequency
description: Current sexual partner and frequency of sex
title: sexual activity
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000285
multivalued: false
alias: sexual_act
domain_of:
- HumanVaginal
range: string
required: false
recommended: false

```
</details>