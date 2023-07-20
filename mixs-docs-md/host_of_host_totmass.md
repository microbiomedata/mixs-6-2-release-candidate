# Slot: host_of_host_totmass


_Total mass of the host of the symbiotic host organism at collection, the unit depends on the host_



URI: [MIXS:0001334](https://w3id.org/mixs/0001334)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_of_host_totmass
description: Total mass of the host of the symbiotic host organism at collection,
  the unit depends on the host
title: host of the symbiotic host total mass
notes:
- host
- host.
- mass
- symbiosis
- total
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001334
multivalued: false
alias: host_of_host_totmass
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>