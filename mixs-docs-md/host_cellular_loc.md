# Slot: host_cellular_loc


_The localization of the symbiotic host organism within the host from which it was sampled: e.g. intracellular if the symbiotic host organism is localized within the cells or extracellular if the symbiotic host organism is localized outside of cells_



URI: [MIXS:0001313](https://w3id.org/mixs/0001313)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [HOSTCELLULARLOCENUM](HOSTCELLULARLOCENUM.md)

* Recommended: True






## Examples

| Value |
| --- |
| extracellular |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_cellular_loc
description: 'The localization of the symbiotic host organism within the host from
  which it was sampled: e.g. intracellular if the symbiotic host organism is localized
  within the cells or extracellular if the symbiotic host organism is localized outside
  of cells'
title: host cellular location
notes:
- host
- host.
- location
examples:
- value: extracellular
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001313
alias: host_cellular_loc
domain_of:
- SymbiontAssociated
range: HOST_CELLULAR_LOC_ENUM
recommended: true

```
</details>