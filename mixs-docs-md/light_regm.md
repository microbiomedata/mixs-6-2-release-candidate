# Slot: light_regm


_Information about treatment(s) involving exposure to light, including both light intensity and quality_



URI: [MIXS:0000569](https://w3id.org/mixs/0000569)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| incandescant light;10 lux;450 nanometer |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | exposure type;light intensity;light quality || Preferred_unit | lux; micrometer, nanometer, angstrom |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: light_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: exposure type;light intensity;light quality
  Preferred_unit:
    tag: Preferred_unit
    value: lux; micrometer, nanometer, angstrom
description: Information about treatment(s) involving exposure to light, including
  both light intensity and quality
title: light regimen
notes:
- light
- regimen
examples:
- value: incandescant light;10 lux;450 nanometer
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit};{float} {unit}'
slot_uri: MIXS:0000569
multivalued: false
alias: light_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>