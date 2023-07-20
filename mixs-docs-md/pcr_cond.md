# Slot: pcr_cond


_Description of reaction conditions and components of PCR in the form of 'initial denaturation:94degC_1.5min; annealing=...'_



URI: [MIXS:0000049](https://w3id.org/mixs/0000049)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| initial denaturation:94_3;annealing:50_1;elongation:72_1.5;final elongation:72_10;35 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pcr_cond
description: Description of reaction conditions and components of PCR in the form
  of 'initial denaturation:94degC_1.5min; annealing=...'
title: pcr conditions
notes:
- condition
- pcr
examples:
- value: initial denaturation:94_3;annealing:50_1;elongation:72_1.5;final elongation:72_10;35
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000049
multivalued: false
alias: pcr_cond
domain_of:
- Agriculture
- MimarksC
- MimarksS
range: string

```
</details>