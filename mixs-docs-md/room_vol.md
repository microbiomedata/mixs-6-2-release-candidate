# Slot: room_vol


_Volume of sampling room_



URI: [MIXS:0000195](https://w3id.org/mixs/0000195)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[1-9][0-9]* \S.*\S+$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | cubic feet, cubic meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: room_vol
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: cubic feet, cubic meter
description: Volume of sampling room
title: room volume
notes:
- room
- volume
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000195
multivalued: false
alias: room_vol
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[1-9][0-9]* \S.*\S+$

```
</details>