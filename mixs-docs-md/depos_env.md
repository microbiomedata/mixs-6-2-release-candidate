# Slot: depos_env


_Main depositional environment (https://en.wikipedia.org/wiki/Depositional_environment). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000992](https://w3id.org/mixs/0000992)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  yes  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  yes  |







## Properties

* Range: [DEPOSENVENUM](DEPOSENVENUM.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: depos_env
description: Main depositional environment (https://en.wikipedia.org/wiki/Depositional_environment).
  If "other" is specified, please propose entry in "additional info" field
title: depositional environment
notes:
- environment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000992
multivalued: false
alias: depos_env
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: DEPOS_ENV_ENUM
recommended: true

```
</details>