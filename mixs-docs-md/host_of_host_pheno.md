# Slot: host_of_host_pheno


_Phenotype of the host of the symbiotic host organism. For phenotypic quality ontology (PATO) terms, see http://purl.bioontology.org/ontology/pato_



URI: [MIXS:0001332](https://w3id.org/mixs/0001332)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | phenotype of the host of the symbiotic organism; PATO |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_of_host_pheno
annotations:
  Expected_value:
    tag: Expected_value
    value: phenotype of the host of the symbiotic organism; PATO
description: Phenotype of the host of the symbiotic host organism. For phenotypic
  quality ontology (PATO) terms, see http://purl.bioontology.org/ontology/pato
title: host of the symbiotic host phenotype
notes:
- host
- host.
- symbiosis
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{term}'
slot_uri: MIXS:0001332
multivalued: false
alias: host_of_host_pheno
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>