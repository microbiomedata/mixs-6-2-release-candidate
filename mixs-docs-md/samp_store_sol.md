# Slot: samp_store_sol


_Solution within which sample was stored, if any_



URI: [MIXS:0001317](https://w3id.org/mixs/0001317)



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
| 5% ethanol |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | solution name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_store_sol
annotations:
  Expected_value:
    tag: Expected_value
    value: solution name
description: Solution within which sample was stored, if any
title: sample storage solution
notes:
- sample
- storage
examples:
- value: 5% ethanol
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001317
multivalued: false
alias: samp_store_sol
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>