# Slot: x16s_recover


_Can a 16S gene be recovered from the submitted SAG or MAG?_



URI: [MIXS:0000065](https://w3id.org/mixs/0000065)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mimag](Mimag.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |







## Properties

* Range: [Boolean](Boolean.md)






## Examples

| Value |
| --- |
| yes |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: x16s_recover
description: Can a 16S gene be recovered from the submitted SAG or MAG?
title: 16S recovered
notes:
- recover
examples:
- value: 'yes'
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000065
multivalued: false
alias: x16s_recover
domain_of:
- Mimag
- Misag
range: boolean

```
</details>