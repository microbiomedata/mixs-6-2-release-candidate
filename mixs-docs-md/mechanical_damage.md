# Slot: mechanical_damage


_Information about any mechanical damage exerted on the plant; can include multiple damages and sites_



URI: [MIXS:0001052](https://w3id.org/mixs/0001052)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| pruning;bark |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | damage type;body site |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: mechanical_damage
annotations:
  Expected_value:
    tag: Expected_value
    value: damage type;body site
description: Information about any mechanical damage exerted on the plant; can include
  multiple damages and sites
title: mechanical damage
examples:
- value: pruning;bark
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{text}'
slot_uri: MIXS:0001052
multivalued: true
alias: mechanical_damage
domain_of:
- FoodFarmEnvironment
- PlantAssociated
range: string
required: false
recommended: false

```
</details>