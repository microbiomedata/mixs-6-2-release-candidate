# Slot: room_air_exch_rate


_The rate at which outside air replaces indoor air in a given space_



URI: [MIXS:0000169](https://w3id.org/mixs/0000169)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | liter per hour |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: room_air_exch_rate
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: liter per hour
description: The rate at which outside air replaces indoor air in a given space
title: room air exchange rate
notes:
- air
- rate
- room
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000169
multivalued: false
alias: room_air_exch_rate
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>