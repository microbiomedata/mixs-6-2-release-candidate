# Slot: heavy_metals


_Heavy metals present in the sequenced sample and their concentrations. For multiple heavy metals and concentrations, add multiple copies of this field_



URI: [MIXS:0000652](https://w3id.org/mixs/0000652)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Soil](Soil.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| mercury;0.09 micrograms per gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | heavy metal name;measurement value unit || Preferred_unit | microgram per gram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: heavy_metals
annotations:
  Expected_value:
    tag: Expected_value
    value: heavy metal name;measurement value unit
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per gram
description: Heavy metals present in the sequenced sample and their concentrations.
  For multiple heavy metals and concentrations, add multiple copies of this field
title: extreme_unusual_properties/heavy metals
notes:
- extreme
- properties
- unusual
examples:
- value: mercury;0.09 micrograms per gram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000652
multivalued: true
alias: heavy_metals
domain_of:
- Soil
range: string
required: false
recommended: false

```
</details>