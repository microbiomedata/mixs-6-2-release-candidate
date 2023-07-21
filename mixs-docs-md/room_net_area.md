# Slot: room_net_area


_The net floor area of sampling room. Net area excludes wall thicknesses_



URI: [MIXS:0000194](https://w3id.org/mixs/0000194)



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
| Preferred_unit | square feet, square meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: room_net_area
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: square feet, square meter
description: The net floor area of sampling room. Net area excludes wall thicknesses
title: room net area
notes:
- area
- room
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000194
multivalued: false
alias: room_net_area
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[1-9][0-9]* \S.*\S+$

```
</details>