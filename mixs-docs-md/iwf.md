# Slot: iwf


_Proportion of the produced fluids derived from injected water at the time of sampling. (e.g. 87%)_



URI: [MIXS:0000455](https://w3id.org/mixs/0000455)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [Float](Float.md)

* Required: True






## Examples

| Value |
| --- |
| 0.79 |

## Comments

* pattern was "[0-9]*\\.?[0-9]+ ?%"
* percent or float?

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | percent |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: iwf
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percent
description: Proportion of the produced fluids derived from injected water at the
  time of sampling. (e.g. 87%)
title: injection water fraction
notes:
- fraction
- water
comments:
- pattern was "[0-9]*\\.?[0-9]+ ?%"
- percent or float?
examples:
- value: '0.79'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000455
alias: iwf
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: float
required: true

```
</details>