# Slot: host_of_host_env_loc


_For a symbiotic host organism the local anatomical environment within its host may have causal influences. Report the anatomical entity(s) which are in the direct environment of the symbiotic host organism being sampled and which you believe have significant causal influences on your sample or specimen. For example, if the symbiotic host organism being sampled is an intestinal worm, its local environmental context will be the term for intestine from UBERON (http://uberon.github.io/)_



URI: [MIXS:0001325](https://w3id.org/mixs/0001325)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| small intestine[uberon:0002108] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | UBERON term(s), multiple values can be separated by pipes |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_of_host_env_loc
annotations:
  Expected_value:
    tag: Expected_value
    value: UBERON term(s), multiple values can be separated by pipes
description: For a symbiotic host organism the local anatomical environment within
  its host may have causal influences. Report the anatomical entity(s) which are in
  the direct environment of the symbiotic host organism being sampled and which you
  believe have significant causal influences on your sample or specimen. For example,
  if the symbiotic host organism being sampled is an intestinal worm, its local environmental
  context will be the term for intestine from UBERON (http://uberon.github.io/)
title: host of the symbiotic host local environmental context
notes:
- context
- environmental
- host
- host.
- symbiosis
examples:
- value: small intestine[uberon:0002108]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: small intestine [UBERON:0002108]
slot_uri: MIXS:0001325
multivalued: true
alias: host_of_host_env_loc
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>