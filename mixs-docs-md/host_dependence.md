# Slot: host_dependence


_Type of host dependence for the symbiotic host organism to its host_



URI: [MIXS:0001315](https://w3id.org/mixs/0001315)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [HOSTDEPENDENCEENUM](HOSTDEPENDENCEENUM.md)

* Required: True






## Examples

| Value |
| --- |
| obligate |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_dependence
description: Type of host dependence for the symbiotic host organism to its host
title: host dependence
notes:
- host
- host.
examples:
- value: obligate
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001315
multivalued: false
alias: host_dependence
domain_of:
- SymbiontAssociated
range: HOST_DEPENDENCE_ENUM
required: true

```
</details>