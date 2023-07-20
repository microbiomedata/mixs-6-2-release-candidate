# Slot: photosynt_activ


_Measurement of photosythetic activity (i.e. leaf gas exchange / chlorophyll fluorescence emissions / reflectance / transpiration) Please also include the term method term detailing the method of activity measurement_



URI: [MIXS:0001296](https://w3id.org/mixs/0001296)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 0.1 mol CO2 m-2 s-1 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | mol m-2 s-1 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: photosynt_activ
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: mol m-2 s-1
description: Measurement of photosythetic activity (i.e. leaf gas exchange / chlorophyll
  fluorescence emissions / reflectance / transpiration) Please also include the term
  method term detailing the method of activity measurement
title: photosynthetic activity
examples:
- value: 0.1 mol CO2 m-2 s-1
  description: added a magnitude to the example from the XLSX file, " mol CO2 m-2
    s-1"
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001296
alias: photosynt_activ
domain_of:
- Agriculture
range: string
recommended: true
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>