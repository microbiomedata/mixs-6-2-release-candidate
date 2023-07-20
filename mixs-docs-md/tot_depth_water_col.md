# Slot: tot_depth_water_col


_Measurement of total depth of water column_



URI: [MIXS:0000634](https://w3id.org/mixs/0000634)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Sediment](Sediment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 500 meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: tot_depth_water_col
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: meter
description: Measurement of total depth of water column
title: total depth of water column
notes:
- depth
- total
- water
examples:
- value: 500 meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000634
multivalued: false
alias: tot_depth_water_col
domain_of:
- Sediment
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>