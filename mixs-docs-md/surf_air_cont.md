# Slot: surf_air_cont


_Contaminant identified on surface_



URI: [MIXS:0000759](https://w3id.org/mixs/0000759)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [SURFAIRCONTENUM](SURFAIRCONTENUM.md)

* Multivalued: True

* Recommended: True






## Examples

| Value |
| --- |
| radon |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: surf_air_cont
description: Contaminant identified on surface
title: surface-air contaminant
examples:
- value: radon
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000759
multivalued: true
alias: surf_air_cont
domain_of:
- BuiltEnvironment
range: SURF_AIR_CONT_ENUM
recommended: true

```
</details>