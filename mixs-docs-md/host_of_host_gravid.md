# Slot: host_of_host_gravid


_Whether or not the host of the symbiotic host organism is gravid, and if yes date due or date post-conception, specifying which is used_



URI: [MIXS:0001333](https://w3id.org/mixs/0001333)



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
| Expected_value | gravidity status;timestamp |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_of_host_gravid
annotations:
  Expected_value:
    tag: Expected_value
    value: gravidity status;timestamp
description: Whether or not the host of the symbiotic host organism is gravid, and
  if yes date due or date post-conception, specifying which is used
title: host of the symbiotic host gravidity
notes:
- host
- host.
- symbiosis
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{boolean};{timestamp}'
slot_uri: MIXS:0001333
multivalued: false
alias: host_of_host_gravid
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>