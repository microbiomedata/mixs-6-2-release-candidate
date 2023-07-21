# Slot: suspend_part_matter


_Concentration of suspended particulate matter_



URI: [MIXS:0000741](https://w3id.org/mixs/0000741)



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
| 0.5 milligram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: suspend_part_matter
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Concentration of suspended particulate matter
title: suspended particulate matter
notes:
- particle
- particulate
- suspended
examples:
- value: 0.5 milligram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000741
multivalued: false
alias: suspend_part_matter
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>