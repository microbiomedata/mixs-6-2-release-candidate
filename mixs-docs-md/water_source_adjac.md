# Slot: water_source_adjac


_Description of the environmental features that are adjacent to the farm water source. This field accepts terms under ecosystem (http://purl.obolibrary.org/obo/ENVO_01001110) and human construction (http://purl.obolibrary.org/obo/ENVO_00000070). Multiple terms can be separated by pipes_



URI: [MIXS:0001122](https://w3id.org/mixs/0001122)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| feedlot [ENVO:01000627] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | ENVO_01001110 or ENVO_00000070 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: water_source_adjac
annotations:
  Expected_value:
    tag: Expected_value
    value: ENVO_01001110 or ENVO_00000070
description: Description of the environmental features that are adjacent to the farm
  water source. This field accepts terms under ecosystem (http://purl.obolibrary.org/obo/ENVO_01001110)
  and human construction (http://purl.obolibrary.org/obo/ENVO_00000070). Multiple
  terms can be separated by pipes
title: environmental feature adjacent water source
notes:
- adjacent
- environmental
- feature
- source
- water
examples:
- value: feedlot [ENVO:01000627]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001122
multivalued: true
alias: water_source_adjac
domain_of:
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>