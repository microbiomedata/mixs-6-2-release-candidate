# Slot: floor_finish_mat


_The floor covering type; the finished surface that is walked on_



URI: [MIXS:0000804](https://w3id.org/mixs/0000804)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| carpet |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: floor_finish_mat
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: The floor covering type; the finished surface that is walked on
title: floor finish material
notes:
- floor
- material
examples:
- value: carpet
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[tile|wood strip or parquet|carpet|rug|laminate wood|lineoleum|vinyl
  composition tile|sheet vinyl|stone|bamboo|cork|terrazo|concrete|none;specify unfinished|sealed|clear
  finish|paint]'
slot_uri: MIXS:0000804
multivalued: false
alias: floor_finish_mat
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>