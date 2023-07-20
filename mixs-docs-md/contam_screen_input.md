# Slot: contam_screen_input


_The type of sequence data used as input_



URI: [MIXS:0000005](https://w3id.org/mixs/0000005)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |







## Properties

* Range: [CONTAMSCREENINPUTENUM](CONTAMSCREENINPUTENUM.md)






## Examples

| Value |
| --- |
| contigs |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: contam_screen_input
description: The type of sequence data used as input
title: contamination screening input
examples:
- value: contigs
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000005
multivalued: false
alias: contam_screen_input
domain_of:
- Mimag
- Misag
range: CONTAM_SCREEN_INPUT_ENUM

```
</details>