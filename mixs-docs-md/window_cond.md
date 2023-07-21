# Slot: window_cond


_The physical condition of the window at the time of sampling_



URI: [MIXS:0000849](https://w3id.org/mixs/0000849)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [SHAREDENUM3](SHAREDENUM3.md)






## Examples

| Value |
| --- |
| rupture |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: window_cond
description: The physical condition of the window at the time of sampling
title: window condition
notes:
- condition
- window
examples:
- value: rupture
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000849
multivalued: false
alias: window_cond
domain_of:
- BuiltEnvironment
range: SHARED_ENUM_3
required: false
recommended: false

```
</details>