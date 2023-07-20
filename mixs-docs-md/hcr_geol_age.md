# Slot: hcr_geol_age


_Geological age of hydrocarbon resource (Additional info: https://en.wikipedia.org/wiki/Period_(geology)). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000993](https://w3id.org/mixs/0000993)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [SHAREDENUM6](SHAREDENUM6.md)

* Recommended: True






## Examples

| Value |
| --- |
| Silurian |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: hcr_geol_age
description: 'Geological age of hydrocarbon resource (Additional info: https://en.wikipedia.org/wiki/Period_(geology)).
  If "other" is specified, please propose entry in "additional info" field'
title: hydrocarbon resource geological age
notes:
- age
- hydrocarbon
- resource
examples:
- value: Silurian
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000993
multivalued: false
alias: hcr_geol_age
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: SHARED_ENUM_6
recommended: true

```
</details>