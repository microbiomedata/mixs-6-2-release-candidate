# Slot: carb_monoxide


_Carbon monoxide (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000098](https://w3id.org/mixs/0000098)



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
| 0.1 parts per million |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micromole per liter, parts per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: carb_monoxide
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter, parts per million
description: Carbon monoxide (gas) amount or concentration at the time of sampling
title: carbon monoxide
notes:
- carbon
examples:
- value: 0.1 parts per million
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000098
multivalued: false
alias: carb_monoxide
domain_of:
- Air
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>