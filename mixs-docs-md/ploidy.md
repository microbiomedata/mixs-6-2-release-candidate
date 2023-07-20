# Slot: ploidy


_The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). It has implications for the downstream study of duplicated gene and regions of the genomes (and perhaps for difficulties in assembly). For terms, please select terms listed under class ploidy (PATO:001374) of Phenotypic Quality Ontology (PATO), and for a browser of PATO (v 2018-03-27) please refer to http://purl.bioontology.org/ontology/PATO_



URI: [MIXS:0000021](https://w3id.org/mixs/0000021)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsEu](MigsEu.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| allopolyploidy [PATO:0001379] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ploidy
description: The ploidy level of the genome (e.g. allopolyploid, haploid, diploid,
  triploid, tetraploid). It has implications for the downstream study of duplicated
  gene and regions of the genomes (and perhaps for difficulties in assembly). For
  terms, please select terms listed under class ploidy (PATO:001374) of Phenotypic
  Quality Ontology (PATO), and for a browser of PATO (v 2018-03-27) please refer to
  http://purl.bioontology.org/ontology/PATO
title: ploidy
examples:
- value: allopolyploidy [PATO:0001379]
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000021
multivalued: false
alias: ploidy
domain_of:
- MigsEu
range: string
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>