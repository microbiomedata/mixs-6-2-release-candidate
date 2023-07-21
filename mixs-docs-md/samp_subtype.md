# Slot: samp_subtype


_Name of sample sub-type. For example if "sample type" is "Produced Water" then subtype could be "Oil Phase" or "Water Phase". If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000999](https://w3id.org/mixs/0000999)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [SAMPSUBTYPEENUM](SAMPSUBTYPEENUM.md)

* Recommended: True






## Examples

| Value |
| --- |
| biofilm |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_subtype
description: Name of sample sub-type. For example if "sample type" is "Produced Water"
  then subtype could be "Oil Phase" or "Water Phase". If "other" is specified, please
  propose entry in "additional info" field
title: sample subtype
notes:
- sample
examples:
- value: biofilm
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000999
multivalued: false
alias: samp_subtype
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: SAMP_SUBTYPE_ENUM
recommended: true

```
</details>