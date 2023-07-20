# Slot: samp_collect_point


_Sampling point on the asset were sample was collected (e.g. Wellhead, storage tank, separator, etc). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0001015](https://w3id.org/mixs/0001015)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [SAMPCOLLECTPOINTENUM](SAMPCOLLECTPOINTENUM.md)

* Required: True






## Examples

| Value |
| --- |
| well |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_collect_point
description: Sampling point on the asset were sample was collected (e.g. Wellhead,
  storage tank, separator, etc). If "other" is specified, please propose entry in
  "additional info" field
title: sample collection point
notes:
- sample
examples:
- value: well
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001015
multivalued: false
alias: samp_collect_point
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: SAMP_COLLECT_POINT_ENUM
required: true

```
</details>