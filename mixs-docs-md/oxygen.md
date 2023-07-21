# Slot: oxygen


_Oxygen (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000104](https://w3id.org/mixs/0000104)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 600 parts per million |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram per liter, parts per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: oxygen
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter, parts per million
description: Oxygen (gas) amount or concentration at the time of sampling
title: oxygen
notes:
- oxygen
examples:
- value: 600 parts per million
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000104
multivalued: false
alias: oxygen
domain_of:
- Air
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>