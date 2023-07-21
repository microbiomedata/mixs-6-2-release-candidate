# Slot: sym_life_cycle_type


_Type of life cycle of the symbiotic host species (the thing being sampled). Simple life cycles occur within a single host, complex ones within multiple different hosts over the course of their normal life cycle_



URI: [MIXS:0001300](https://w3id.org/mixs/0001300)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |







## Properties

* Range: [SYMLIFECYCLETYPEENUM](SYMLIFECYCLETYPEENUM.md)

* Required: True






## Examples

| Value |
| --- |
| complex life cycle |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | type of life cycle of the symbiotic organism (host of the samples) |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sym_life_cycle_type
annotations:
  Expected_value:
    tag: Expected_value
    value: type of life cycle of the symbiotic organism (host of the samples)
description: Type of life cycle of the symbiotic host species (the thing being sampled).
  Simple life cycles occur within a single host, complex ones within multiple different
  hosts over the course of their normal life cycle
title: symbiotic host organism life cycle type
notes:
- host
- host.
- life
- organism
- symbiosis
- type
examples:
- value: complex life cycle
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001300
multivalued: false
alias: sym_life_cycle_type
domain_of:
- SymbiontAssociated
range: SYM_LIFE_CYCLE_TYPE_ENUM
required: true

```
</details>