# Slot: host_of_host_fam_rel


_Familial relationship of the host of the symbiotic host organisms to other hosts of symbiotic host organism in the same study; can include multiple relationships_



URI: [MIXS:0001328](https://w3id.org/mixs/0001328)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | relationship type;arbitrary identifier |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_of_host_fam_rel
annotations:
  Expected_value:
    tag: Expected_value
    value: relationship type;arbitrary identifier
description: Familial relationship of the host of the symbiotic host organisms to
  other hosts of symbiotic host organism in the same study; can include multiple relationships
title: host of the symbiotic host family relationship
notes:
- family
- host
- host.
- relationship
- symbiosis
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{text}'
slot_uri: MIXS:0001328
multivalued: true
alias: host_of_host_fam_rel
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>