# Slot: env_broad_scale


_Report the major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the general environmental context of where the sampling was done (e.g. in the desert or a rainforest). We recommend using subclasses of EnvOs biome class:  http://purl.obolibrary.org/obo/ENVO_00000428. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS_



URI: [MIXS:0000012](https://w3id.org/mixs/0000012)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsBa](MigsBa.md) |  |  no  |
[MigsEu](MigsEu.md) |  |  no  |
[MigsOrg](MigsOrg.md) |  |  no  |
[MigsPl](MigsPl.md) |  |  no  |
[MigsVi](MigsVi.md) |  |  no  |
[Mimag](Mimag.md) |  |  no  |
[MimarksC](MimarksC.md) |  |  no  |
[MimarksS](MimarksS.md) |  |  no  |
[Mims](Mims.md) |  |  no  |
[Misag](Misag.md) |  |  no  |
[Miuvig](Miuvig.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| rangeland biome [ENVO:01000247] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: env_broad_scale
description: 'Report the major environmental system the sample or specimen came from.
  The system(s) identified should have a coarse spatial grain, to provide the general
  environmental context of where the sampling was done (e.g. in the desert or a rainforest).
  We recommend using subclasses of EnvOs biome class:  http://purl.obolibrary.org/obo/ENVO_00000428.
  EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS'
title: broad-scale environmental context
notes:
- context
- environmental
examples:
- value: rangeland biome [ENVO:01000247]
in_subset:
- environment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000012
multivalued: false
alias: env_broad_scale
domain_of:
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- MimarksC
- MimarksS
- Mims
- Misag
- Miuvig
range: string
required: true
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>