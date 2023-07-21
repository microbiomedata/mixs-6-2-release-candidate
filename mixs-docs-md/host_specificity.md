# Slot: host_specificity


_Level of specificity of symbiont-host interaction: e.g. generalist (symbiont able to establish associations with distantly related hosts) or species-specific_



URI: [MIXS:0001308](https://w3id.org/mixs/0001308)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [HOSTSPECIFICITYENUM](HOSTSPECIFICITYENUM.md)

* Recommended: True






## Examples

| Value |
| --- |
| species-specific |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_specificity
description: 'Level of specificity of symbiont-host interaction: e.g. generalist (symbiont
  able to establish associations with distantly related hosts) or species-specific'
title: host specificity
notes:
- host
- host.
examples:
- value: species-specific
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001308
multivalued: false
alias: host_specificity
domain_of:
- SymbiontAssociated
range: HOST_SPECIFICITY_ENUM
recommended: true

```
</details>