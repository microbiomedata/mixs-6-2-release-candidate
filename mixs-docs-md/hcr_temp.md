# Slot: hcr_temp


_Original temperature of the hydrocarbon resource_



URI: [MIXS:0000393](https://w3id.org/mixs/0000393)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  yes  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 150-295 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: hcr_temp
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: Original temperature of the hydrocarbon resource
title: hydrocarbon resource original temperature
notes:
- hydrocarbon
- resource
- temperature
examples:
- value: 150-295 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000393
multivalued: false
alias: hcr_temp
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
structured_pattern:
  syntax: '{float} - {float} {unit}'
  interpolated: true
  partial_match: true

```
</details>