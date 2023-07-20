# Slot: bac_prod


_Bacterial production in the water column measured by isotope uptake_



URI: [MIXS:0000683](https://w3id.org/mixs/0000683)



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
| 5 milligram per cubic meter per day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram per cubic meter per day |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: bac_prod
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per cubic meter per day
description: Bacterial production in the water column measured by isotope uptake
title: bacterial production
notes:
- production
examples:
- value: 5 milligram per cubic meter per day
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000683
multivalued: false
alias: bac_prod
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>