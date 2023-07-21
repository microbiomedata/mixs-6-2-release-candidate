# Slot: lithology


_Hydrocarbon resource main lithology (Additional information: http://petrowiki.org/Lithology_and_rock_type_determination). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000990](https://w3id.org/mixs/0000990)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [LITHOLOGYENUM](LITHOLOGYENUM.md)

* Recommended: True






## Examples

| Value |
| --- |
| Volcanic |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: lithology
description: 'Hydrocarbon resource main lithology (Additional information: http://petrowiki.org/Lithology_and_rock_type_determination).
  If "other" is specified, please propose entry in "additional info" field'
title: lithology
notes:
- lithology
examples:
- value: Volcanic
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000990
multivalued: false
alias: lithology
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: LITHOLOGY_ENUM
recommended: true

```
</details>