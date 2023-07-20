# Slot: down_par


_Visible waveband radiance and irradiance measurements in the water column_



URI: [MIXS:0000703](https://w3id.org/mixs/0000703)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 28.71 microEinstein per square meter per second |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | microEinstein per square meter per second, microEinstein per square centimeter per second |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: down_par
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: microEinstein per square meter per second, microEinstein per square centimeter
      per second
description: Visible waveband radiance and irradiance measurements in the water column
title: downward PAR
examples:
- value: 28.71 microEinstein per square meter per second
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000703
multivalued: false
alias: down_par
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>