# Slot: travel_out_six_month


_Specification of the countries travelled in the last six months; can include multiple travels_



URI: [MIXS:0000268](https://w3id.org/mixs/0000268)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanAssociated](HumanAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | country name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: travel_out_six_month
annotations:
  Expected_value:
    tag: Expected_value
    value: country name
description: Specification of the countries travelled in the last six months; can
  include multiple travels
title: travel outside the country in last six months
notes:
- months
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000268
multivalued: true
alias: travel_out_six_month
domain_of:
- HumanAssociated
range: string
required: false
recommended: false

```
</details>