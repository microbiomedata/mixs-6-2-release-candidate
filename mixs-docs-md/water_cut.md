# Slot: water_cut


_Current amount of water (%) in a produced fluid stream; or the average of the combined streams_



URI: [MIXS:0000454](https://w3id.org/mixs/0000454)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `[0-9]*\.?[0-9]+ ?%`






## Examples

| Value |
| --- |
| 45% |

## Comments

* percent or float?

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | percent |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: water_cut
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percent
description: Current amount of water (%) in a produced fluid stream; or the average
  of the combined streams
title: water cut
notes:
- water
comments:
- percent or float?
examples:
- value: 45%
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000454
alias: water_cut
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
required: true
pattern: '[0-9]*\.?[0-9]+ ?%'

```
</details>