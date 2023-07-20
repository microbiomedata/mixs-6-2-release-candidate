# Slot: water_source_shared


_Other users sharing access to the same water source. Multiple terms can be separated by one or more pipes_



URI: [MIXS:0001176](https://w3id.org/mixs/0001176)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| no sharing |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: water_source_shared
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: Other users sharing access to the same water source. Multiple terms can
  be separated by one or more pipes
title: water source shared
notes:
- source
- water
examples:
- value: no sharing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[multiple users, agricutural|multiple users, other|no sharing]'
slot_uri: MIXS:0001176
multivalued: true
alias: water_source_shared
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>