# Slot: trophic_level


_Trophic levels are the feeding position in a food chain. Microbes can be a range of producers (e.g. chemolithotroph)_



URI: [MIXS:0000032](https://w3id.org/mixs/0000032)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |







## Properties

* Range: [TROPHICLEVELENUM](TROPHICLEVELENUM.md)






## Examples

| Value |
| --- |
| heterotroph |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: trophic_level
description: Trophic levels are the feeding position in a food chain. Microbes can
  be a range of producers (e.g. chemolithotroph)
title: trophic level
notes:
- level
examples:
- value: heterotroph
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000032
multivalued: false
alias: trophic_level
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MimarksC
range: TROPHIC_LEVEL_ENUM

```
</details>