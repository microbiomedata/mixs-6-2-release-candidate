# Slot: rel_samp_loc


_The sampling location within the train car_



URI: [MIXS:0000821](https://w3id.org/mixs/0000821)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [RELSAMPLOCENUM](RELSAMPLOCENUM.md)






## Examples

| Value |
| --- |
| center of car |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: rel_samp_loc
description: The sampling location within the train car
title: relative sampling location
notes:
- location
- relative
examples:
- value: center of car
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000821
multivalued: false
alias: rel_samp_loc
domain_of:
- BuiltEnvironment
range: REL_SAMP_LOC_ENUM
required: false
recommended: false

```
</details>