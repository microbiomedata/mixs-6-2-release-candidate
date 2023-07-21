# Slot: address


_The street name and building number where the sampling occurred_



URI: [MIXS:0000218](https://w3id.org/mixs/0000218)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | value |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: address
annotations:
  Expected_value:
    tag: Expected_value
    value: value
description: The street name and building number where the sampling occurred
title: address
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{integer}{text}'
slot_uri: MIXS:0000218
multivalued: false
alias: address
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>