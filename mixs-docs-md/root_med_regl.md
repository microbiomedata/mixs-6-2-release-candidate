# Slot: root_med_regl


_Growth regulators in the culture rooting medium such as cytokinins, auxins, gybberellins, abscisic acid; e.g. 0.5mg/L NAA_



URI: [MIXS:0000581](https://w3id.org/mixs/0000581)



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
| abscisic acid;0.75 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | regulator name;measurement value || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: root_med_regl
annotations:
  Expected_value:
    tag: Expected_value
    value: regulator name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Growth regulators in the culture rooting medium such as cytokinins, auxins,
  gybberellins, abscisic acid; e.g. 0.5mg/L NAA
title: rooting medium regulators
examples:
- value: abscisic acid;0.75 milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000581
multivalued: false
alias: root_med_regl
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>