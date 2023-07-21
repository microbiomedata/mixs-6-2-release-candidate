# Slot: sr_geol_age


_Geological age of source rock (Additional info: https://en.wikipedia.org/wiki/Period_(geology)). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000997](https://w3id.org/mixs/0000997)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [SHAREDENUM6](SHAREDENUM6.md)






## Examples

| Value |
| --- |
| Silurian |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sr_geol_age
description: 'Geological age of source rock (Additional info: https://en.wikipedia.org/wiki/Period_(geology)).
  If "other" is specified, please propose entry in "additional info" field'
title: source rock geological age
notes:
- age
- source
examples:
- value: Silurian
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000997
multivalued: false
alias: sr_geol_age
domain_of:
- HydrocarbonResourcesCores
range: SHARED_ENUM_6
required: false
recommended: false

```
</details>