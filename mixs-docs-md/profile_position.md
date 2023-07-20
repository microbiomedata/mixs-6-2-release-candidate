# Slot: profile_position


_Cross-sectional position in the hillslope where sample was collected.sample area position in relation to surrounding areas_



URI: [MIXS:0001084](https://w3id.org/mixs/0001084)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [PROFILEPOSITIONENUM](PROFILEPOSITIONENUM.md)






## Examples

| Value |
| --- |
| summit |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: profile_position
description: Cross-sectional position in the hillslope where sample was collected.sample
  area position in relation to surrounding areas
title: profile position
examples:
- value: summit
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001084
multivalued: false
alias: profile_position
domain_of:
- Agriculture
- Soil
range: PROFILE_POSITION_ENUM

```
</details>