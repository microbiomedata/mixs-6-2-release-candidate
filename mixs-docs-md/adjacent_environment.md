# Slot: adjacent_environment


_Description of the environmental system or features that are adjacent to the sampling site. This field accepts terms under ecosystem (http://purl.obolibrary.org/obo/ENVO_01001110) and human construction (http://purl.obolibrary.org/obo/ENVO_00000070). Multiple terms can be separated by pipes_



URI: [MIXS:0001121](https://w3id.org/mixs/0001121)



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
| estuarine biome [ENVO:01000020] |

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
name: adjacent_environment
annotations:
  Expected_value:
    tag: Expected_value
    value: ENVO_01001110 or ENVO_00000070
description: Description of the environmental system or features that are adjacent
  to the sampling site. This field accepts terms under ecosystem (http://purl.obolibrary.org/obo/ENVO_01001110)
  and human construction (http://purl.obolibrary.org/obo/ENVO_00000070). Multiple
  terms can be separated by pipes
title: environment adjacent to site
notes:
- adjacent
- environment
- site
examples:
- value: estuarine biome [ENVO:01000020]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel}{[termID]}'
slot_uri: MIXS:0001121
multivalued: true
alias: adjacent_environment
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>