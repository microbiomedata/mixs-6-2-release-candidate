# Slot: amount_light


_The unit of illuminance and luminous emittance, measuring luminous flux per unit area_



URI: [MIXS:0000140](https://w3id.org/mixs/0000140)



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
| Preferred_unit | lux, lumens per square meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: amount_light
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: lux, lumens per square meter
description: The unit of illuminance and luminous emittance, measuring luminous flux
  per unit area
title: amount of light
notes:
- light
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000140
multivalued: false
alias: amount_light
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>