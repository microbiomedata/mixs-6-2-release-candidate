# Slot: pour_point


_Temperature at which a liquid becomes semi solid and loses its flow characteristics. In crude oil a highpour pointis generally associated with a high paraffin content, typically found in crude deriving from a larger proportion of plant material. (soure: https://en.wikipedia.org/wiki/pour_point)_



URI: [MIXS:0000127](https://w3id.org/mixs/0000127)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pour_point
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: 'Temperature at which a liquid becomes semi solid and loses its flow
  characteristics. In crude oil a highpour pointis generally associated with a high
  paraffin content, typically found in crude deriving from a larger proportion of
  plant material. (soure: https://en.wikipedia.org/wiki/pour_point)'
title: pour point
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000127
multivalued: false
alias: pour_point
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>