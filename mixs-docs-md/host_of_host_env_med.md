# Slot: host_of_host_env_med


_Report the environmental material(s) immediately surrounding the symbiotic host organism at the time of sampling. This usually will be a tissue or substance type from the host, but may be another material if the symbiont is external to the host. We recommend using classes from the UBERON ontology, but subclasses of 'environmental material' (http://purl.obolibrary.org/obo/ENVO_00010483) may also be used. EnvO documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. intestines, heart).MIxS . Terms from other OBO ontologies are permissible as long as they reference mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. intestines, heart)_



URI: [MIXS:0001326](https://w3id.org/mixs/0001326)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| feces[uberon:0001988] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | An ontology term for a material such as a tissue type or excreted substance |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_of_host_env_med
annotations:
  Expected_value:
    tag: Expected_value
    value: An ontology term for a material such as a tissue type or excreted substance
description: 'Report the environmental material(s) immediately surrounding the symbiotic
  host organism at the time of sampling. This usually will be a tissue or substance
  type from the host, but may be another material if the symbiont is external to the
  host. We recommend using classes from the UBERON ontology, but subclasses of ''environmental
  material'' (http://purl.obolibrary.org/obo/ENVO_00010483) may also be used. EnvO
  documentation about how to use the field: https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS
  . Terms from other OBO ontologies are permissible as long as they reference mass/volume
  nouns (e.g. air, water, blood) and not discrete, countable entities (e.g. intestines,
  heart).MIxS . Terms from other OBO ontologies are permissible as long as they reference
  mass/volume nouns (e.g. air, water, blood) and not discrete, countable entities
  (e.g. intestines, heart)'
title: host of the symbiotic host environemental medium
notes:
- environmental
- host
- host.
- symbiosis
examples:
- value: feces[uberon:0001988]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}]'
slot_uri: MIXS:0001326
alias: host_of_host_env_med
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>