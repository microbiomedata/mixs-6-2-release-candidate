# Slot: host_of_host_coinf


_The taxonomic name of any coinfecting organism observed in a symbiotic relationship with the host of the sampled host organism. e.g. where a sample collected from a host trematode species (A) which was collected from a host_of_host fish (B) that was also infected with a nematode (C), the value here would be (C) the nematode {species name} or {common name}. Multiple co-infecting species may be added in a comma-separated list. For listing symbiotic organisms associated with the host (A) use the term Observed host symbiont_



URI: [MIXS:0001310](https://w3id.org/mixs/0001310)



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
| Maritrema novaezealandense |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | species name of coinfecting organism(s) |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_of_host_coinf
annotations:
  Expected_value:
    tag: Expected_value
    value: species name of coinfecting organism(s)
description: The taxonomic name of any coinfecting organism observed in a symbiotic
  relationship with the host of the sampled host organism. e.g. where a sample collected
  from a host trematode species (A) which was collected from a host_of_host fish (B)
  that was also infected with a nematode (C), the value here would be (C) the nematode
  {species name} or {common name}. Multiple co-infecting species may be added in a
  comma-separated list. For listing symbiotic organisms associated with the host (A)
  use the term Observed host symbiont
title: observed coinfecting organisms in host of host
notes:
- host
- host.
- observed
- organism
examples:
- value: Maritrema novaezealandense
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001310
multivalued: false
alias: host_of_host_coinf
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>