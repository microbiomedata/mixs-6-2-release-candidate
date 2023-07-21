# Slot: sr_dep_env


_Source rock depositional environment (https://en.wikipedia.org/wiki/Source_rock). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000996](https://w3id.org/mixs/0000996)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [SRDEPENVENUM](SRDEPENVENUM.md)






## Examples

| Value |
| --- |
| Marine |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sr_dep_env
description: Source rock depositional environment (https://en.wikipedia.org/wiki/Source_rock).
  If "other" is specified, please propose entry in "additional info" field
title: source rock depositional environment
notes:
- environment
- source
examples:
- value: Marine
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000996
multivalued: false
alias: sr_dep_env
domain_of:
- HydrocarbonResourcesCores
range: SR_DEP_ENV_ENUM
required: false
recommended: false

```
</details>