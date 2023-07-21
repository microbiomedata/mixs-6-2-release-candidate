# Slot: rel_to_oxygen


_Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments_



URI: [MIXS:0000015](https://w3id.org/mixs/0000015)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  yes  |
[Mimag](Mimag.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [RELTOOXYGENENUM](RELTOOXYGENENUM.md)






## Examples

| Value |
| --- |
| aerobe |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: rel_to_oxygen
description: Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic
  are valid descriptors for microbial environments
title: relationship to oxygen
notes:
- oxygen
- relationship
examples:
- value: aerobe
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000015
multivalued: false
alias: rel_to_oxygen
domain_of:
- MigsBa
- Mimag
- MimarksC
- MimarksS
- Mims
- Misag
range: REL_TO_OXYGEN_ENUM

```
</details>