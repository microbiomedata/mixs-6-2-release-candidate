# Slot: host_number


_Number of symbiotic host individuals pooled at the time of collection_



URI: [MIXS:0001305](https://w3id.org/mixs/0001305)



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
| 3 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | count |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_number
annotations:
  Expected_value:
    tag: Expected_value
    value: count
description: Number of symbiotic host individuals pooled at the time of collection
title: host number individual
notes:
- host
- host.
- number
examples:
- value: '3'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} m'
slot_uri: MIXS:0001305
multivalued: false
alias: host_number
domain_of:
- SymbiontAssociated
range: string
required: false
recommended: false

```
</details>