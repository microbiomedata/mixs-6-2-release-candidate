# Slot: root_med_suppl


_Organic supplements of the culture rooting medium, such as vitamins, amino acids, organic acids, antibiotics activated charcoal; e.g. nicotinic acid (0.5mg/L)_



URI: [MIXS:0000580](https://w3id.org/mixs/0000580)



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
| nicotinic acid;0.5 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | supplement name;measurement value || Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: root_med_suppl
annotations:
  Expected_value:
    tag: Expected_value
    value: supplement name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Organic supplements of the culture rooting medium, such as vitamins,
  amino acids, organic acids, antibiotics activated charcoal; e.g. nicotinic acid
  (0.5mg/L)
title: rooting medium organic supplements
notes:
- organic
examples:
- value: nicotinic acid;0.5 milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000580
multivalued: false
alias: root_med_suppl
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>