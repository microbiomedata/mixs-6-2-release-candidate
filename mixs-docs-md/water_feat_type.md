# Slot: water_feat_type


_The type of water feature present within the building being sampled_



URI: [MIXS:0000847](https://w3id.org/mixs/0000847)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [WATERFEATTYPEENUM](WATERFEATTYPEENUM.md)






## Examples

| Value |
| --- |
| stream |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: water_feat_type
description: The type of water feature present within the building being sampled
title: water feature type
notes:
- feature
- type
- water
examples:
- value: stream
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000847
multivalued: false
alias: water_feat_type
domain_of:
- BuiltEnvironment
range: WATER_FEAT_TYPE_ENUM
required: false
recommended: false

```
</details>