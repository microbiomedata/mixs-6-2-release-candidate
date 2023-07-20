# Slot: primary_prod


_Measurement of primary production, generally measured as isotope uptake_



URI: [MIXS:0000728](https://w3id.org/mixs/0000728)



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
| 100 milligram per cubic meter per day |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram per cubic meter per day, gram per square meter per day |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: primary_prod
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per cubic meter per day, gram per square meter per day
description: Measurement of primary production, generally measured as isotope uptake
title: primary production
notes:
- primary
- production
examples:
- value: 100 milligram per cubic meter per day
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000728
multivalued: false
alias: primary_prod
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>