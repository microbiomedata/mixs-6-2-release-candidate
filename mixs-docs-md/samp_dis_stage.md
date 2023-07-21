# Slot: samp_dis_stage


_Stage of the disease at the time of sample collection, e.g. inoculation, penetration, infection, growth and reproduction, dissemination of pathogen_



URI: [MIXS:0000249](https://w3id.org/mixs/0000249)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HostAssociated](HostAssociated.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [SAMPDISSTAGEENUM](SAMPDISSTAGEENUM.md)






## Examples

| Value |
| --- |
| infection |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_dis_stage
description: Stage of the disease at the time of sample collection, e.g. inoculation,
  penetration, infection, growth and reproduction, dissemination of pathogen
title: sample disease stage
notes:
- disease
- sample
examples:
- value: infection
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000249
multivalued: false
alias: samp_dis_stage
domain_of:
- HostAssociated
- PlantAssociated
range: SAMP_DIS_STAGE_ENUM
required: false
recommended: false

```
</details>