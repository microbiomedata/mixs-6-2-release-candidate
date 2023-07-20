# Slot: env_medium


_Report the environmental material(s) immediately surrounding the sample or specimen at the time of sampling. We recommend using subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree, a leaf, a table top)_



URI: [MIXS:0000014](https://w3id.org/mixs/0000014)



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
| bluegrass field soil [ENVO:00005789] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: env_medium
description: 'Report the environmental material(s) immediately surrounding the sample
  or specimen at the time of sampling. We recommend using subclasses of ''environmental
  material'' (http://purl.obolibrary.org/obo/ENVO_00010483). EnvO documentation about
  how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
  . Terms from other OBO ontologies are permissible as long as they reference mass/volume
  nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. a tree,
  a leaf, a table top)'
title: environmental medium
notes:
- environmental
examples:
- value: bluegrass field soil [ENVO:00005789]
in_subset:
- environment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000014
multivalued: false
alias: env_medium
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