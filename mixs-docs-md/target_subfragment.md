# Slot: target_subfragment


_Name of subfragment of a gene or locus. Important to e.g. identify special regions on marker genes like V6 on 16S rRNA_



URI: [MIXS:0000045](https://w3id.org/mixs/0000045)



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
| V6, V9, ITS |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: target_subfragment
description: Name of subfragment of a gene or locus. Important to e.g. identify special
  regions on marker genes like V6 on 16S rRNA
title: target subfragment
notes:
- target
examples:
- value: V6, V9, ITS
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000045
multivalued: false
alias: target_subfragment
domain_of:
- Agriculture
- MimarksC
- MimarksS
range: string

```
</details>