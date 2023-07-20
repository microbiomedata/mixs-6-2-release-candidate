# Slot: env_local_scale


_Report the entity or entities which are in the sample or specimens local vicinity and which you believe have significant causal influences on your sample or specimen. We recommend using EnvO terms which are of smaller spatial grain than your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS_



URI: [MIXS:0000013](https://w3id.org/mixs/0000013)



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






## Examples

| Value |
| --- |
| hillside [ENVO:01000333] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | Environmental entities having causal influences upon the entity at time of sampling |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: env_local_scale
annotations:
  Expected_value:
    tag: Expected_value
    value: Environmental entities having causal influences upon the entity at time
      of sampling
description: 'Report the entity or entities which are in the sample or specimens local
  vicinity and which you believe have significant causal influences on your sample
  or specimen. We recommend using EnvO terms which are of smaller spatial grain than
  your entry for env_broad_scale. Terms, such as anatomical sites, from other OBO
  Library ontologies which interoperate with EnvO (e.g. UBERON) are accepted in this
  field. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS'
title: local environmental context
notes:
- context
- environmental
examples:
- value: hillside [ENVO:01000333]
in_subset:
- environment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}]'
slot_uri: MIXS:0000013
multivalued: false
alias: env_local_scale
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

```
</details>