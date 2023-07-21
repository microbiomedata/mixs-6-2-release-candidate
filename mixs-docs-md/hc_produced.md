# Slot: hc_produced


_Main hydrocarbon type produced from resource (i.e. Oil, gas, condensate, etc). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000989](https://w3id.org/mixs/0000989)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [HCPRODUCEDENUM](HCPRODUCEDENUM.md)

* Required: True






## Examples

| Value |
| --- |
| Gas |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: hc_produced
description: Main hydrocarbon type produced from resource (i.e. Oil, gas, condensate,
  etc). If "other" is specified, please propose entry in "additional info" field
title: hydrocarbon type produced
notes:
- hydrocarbon
- type
examples:
- value: Gas
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000989
multivalued: false
alias: hc_produced
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: HC_PRODUCED_ENUM
required: true

```
</details>