# Slot: light_intensity


_Measurement of light intensity_



URI: [MIXS:0000706](https://w3id.org/mixs/0000706)



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
| 0.3 lux |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | lux |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: light_intensity
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: lux
description: Measurement of light intensity
title: light intensity
notes:
- intensity
- light
examples:
- value: 0.3 lux
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000706
multivalued: false
alias: light_intensity
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>