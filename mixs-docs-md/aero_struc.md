# Slot: aero_struc


_Aerospace structures typically consist of thin plates with stiffeners for the external surfaces, bulkheads and frames to support the shape and fasteners such as welds, rivets, screws and bolts to hold the components together_



URI: [MIXS:0000773](https://w3id.org/mixs/0000773)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [AEROSTRUCENUM](AEROSTRUCENUM.md)






## Examples

| Value |
| --- |
| plane |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: aero_struc
description: Aerospace structures typically consist of thin plates with stiffeners
  for the external surfaces, bulkheads and frames to support the shape and fasteners
  such as welds, rivets, screws and bolts to hold the components together
title: aerospace structure
examples:
- value: plane
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000773
multivalued: false
alias: aero_struc
domain_of:
- BuiltEnvironment
range: AERO_STRUC_ENUM
required: false
recommended: false

```
</details>