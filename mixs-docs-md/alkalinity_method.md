# Slot: alkalinity_method


_Method used for alkalinity measurement_



URI: [MIXS:0000298](https://w3id.org/mixs/0000298)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| titration |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: alkalinity_method
description: Method used for alkalinity measurement
title: alkalinity method
notes:
- alkalinity
- method
examples:
- value: titration
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000298
multivalued: false
alias: alkalinity_method
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
- Water
range: string
required: false
recommended: false

```
</details>