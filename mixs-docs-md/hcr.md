# Slot: hcr


_Main Hydrocarbon Resource type. The term "Hydrocarbon Resource" HCR defined as a natural environmental feature containing large amounts of hydrocarbons at high concentrations potentially suitable for commercial exploitation. This term should not be confused with the Hydrocarbon Occurrence term which also includes hydrocarbon-rich environments with currently limited commercial interest such as seeps, outcrops, gas hydrates etc. If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000988](https://w3id.org/mixs/0000988)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [HCRENUM](HCRENUM.md)

* Required: True






## Examples

| Value |
| --- |
| Oil Sand |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: hcr
description: Main Hydrocarbon Resource type. The term "Hydrocarbon Resource" HCR defined
  as a natural environmental feature containing large amounts of hydrocarbons at high
  concentrations potentially suitable for commercial exploitation. This term should
  not be confused with the Hydrocarbon Occurrence term which also includes hydrocarbon-rich
  environments with currently limited commercial interest such as seeps, outcrops,
  gas hydrates etc. If "other" is specified, please propose entry in "additional info"
  field
title: hydrocarbon resource type
notes:
- hydrocarbon
- resource
- type
examples:
- value: Oil Sand
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000988
multivalued: false
alias: hcr
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: HCR_ENUM
required: true

```
</details>