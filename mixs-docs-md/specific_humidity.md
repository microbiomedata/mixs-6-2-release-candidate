# Slot: specific_humidity


_The mass of water vapour in a unit mass of moist air, usually expressed as grams of vapour per kilogram of air, or, in air conditioning, as grains per pound_



URI: [MIXS:0000214](https://w3id.org/mixs/0000214)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 15 per kilogram of air |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram of air, kilogram of air |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: specific_humidity
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram of air, kilogram of air
description: The mass of water vapour in a unit mass of moist air, usually expressed
  as grams of vapour per kilogram of air, or, in air conditioning, as grains per pound
title: specific humidity
notes:
- humidity
examples:
- value: 15 per kilogram of air
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000214
multivalued: false
alias: specific_humidity
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>