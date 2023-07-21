# Slot: diss_inorg_phosp


_Concentration of dissolved inorganic phosphorus in the sample_



URI: [MIXS:0000106](https://w3id.org/mixs/0000106)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  yes  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  yes  |
[Water](Water.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 56.5 micromole per liter |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: diss_inorg_phosp
description: Concentration of dissolved inorganic phosphorus in the sample
title: dissolved inorganic phosphorus
notes:
- dissolved
- inorganic
- phosphorus
examples:
- value: 56.5 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000106
multivalued: false
alias: diss_inorg_phosp
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
- Water
range: string
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>