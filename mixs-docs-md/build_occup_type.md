# Slot: build_occup_type


_The primary function for which a building or discrete part of a building is intended to be used_



URI: [MIXS:0000761](https://w3id.org/mixs/0000761)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [BUILDOCCUPTYPEENUM](BUILDOCCUPTYPEENUM.md)

* Multivalued: True

* Required: True






## Examples

| Value |
| --- |
| market |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: build_occup_type
description: The primary function for which a building or discrete part of a building
  is intended to be used
title: building occupancy type
notes:
- type
examples:
- value: market
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000761
multivalued: true
alias: build_occup_type
domain_of:
- BuiltEnvironment
range: BUILD_OCCUP_TYPE_ENUM
required: true

```
</details>