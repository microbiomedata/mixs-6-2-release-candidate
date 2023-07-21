# Slot: tidal_stage


_Stage of tide_



URI: [MIXS:0000750](https://w3id.org/mixs/0000750)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Sediment](Sediment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [TIDALSTAGEENUM](TIDALSTAGEENUM.md)






## Examples

| Value |
| --- |
| high tide |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: tidal_stage
description: Stage of tide
title: tidal stage
examples:
- value: high tide
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000750
multivalued: false
alias: tidal_stage
domain_of:
- Sediment
- Water
range: TIDAL_STAGE_ENUM
required: false
recommended: false

```
</details>