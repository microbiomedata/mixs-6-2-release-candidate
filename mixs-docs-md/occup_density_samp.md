# Slot: occup_density_samp


_Average number of occupants at time of sampling per square footage_



URI: [MIXS:0000217](https://w3id.org/mixs/0000217)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [Float](Float.md)

* Required: True






## Examples

| Value |
| --- |
| 0.1 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: occup_density_samp
description: Average number of occupants at time of sampling per square footage
title: occupant density at sampling
notes:
- density
examples:
- value: '0.1'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000217
multivalued: false
alias: occup_density_samp
domain_of:
- BuiltEnvironment
range: float
required: true

```
</details>