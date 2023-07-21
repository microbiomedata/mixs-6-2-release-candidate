# Slot: host_of_host_taxid


_NCBI taxon id of the host of the symbiotic host organism_



URI: [MIXS:0001306](https://w3id.org/mixs/0001306)



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
| 145637 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCBI taxon identifier of the host of the symbiotic taxon organism |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_of_host_taxid
annotations:
  Expected_value:
    tag: Expected_value
    value: NCBI taxon identifier of the host of the symbiotic taxon organism
description: NCBI taxon id of the host of the symbiotic host organism
title: host of the symbiotic host taxon id
notes:
- host
- host.
- identifier
- symbiosis
- taxon
examples:
- value: '145637'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{integer}'
slot_uri: MIXS:0001306
multivalued: false
alias: host_of_host_taxid
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>