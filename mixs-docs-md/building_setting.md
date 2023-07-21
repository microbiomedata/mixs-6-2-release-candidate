# Slot: building_setting


_A location (geography) where a building is set_



URI: [MIXS:0000768](https://w3id.org/mixs/0000768)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [BUILDINGSETTINGENUM](BUILDINGSETTINGENUM.md)

* Required: True






## Examples

| Value |
| --- |
| rural |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: building_setting
description: A location (geography) where a building is set
title: building setting
examples:
- value: rural
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000768
multivalued: false
alias: building_setting
domain_of:
- BuiltEnvironment
range: BUILDING_SETTING_ENUM
required: true

```
</details>