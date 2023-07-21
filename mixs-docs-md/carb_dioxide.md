# Slot: carb_dioxide


_Carbon dioxide (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000097](https://w3id.org/mixs/0000097)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  yes  |
[BuiltEnvironment](BuiltEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 410 parts per million |

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
name: carb_dioxide
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter, parts per million
description: Carbon dioxide (gas) amount or concentration at the time of sampling
title: carbon dioxide
notes:
- carbon
examples:
- value: 410 parts per million
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000097
multivalued: false
alias: carb_dioxide
domain_of:
- Air
- BuiltEnvironment
range: string
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>