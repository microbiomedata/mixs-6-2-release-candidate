# Slot: air_flow_impede


_Presence of objects in the area that would influence or impede air flow through the air filter_



URI: [MIXS:0001146](https://w3id.org/mixs/0001146)



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
| obstructed;hay bales; 2 m |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration;obstruction type; distance from sampling device |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: air_flow_impede
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration;obstruction type; distance from sampling device
description: Presence of objects in the area that would influence or impede air flow
  through the air filter
title: local air flow impediments
notes:
- air
examples:
- value: obstructed;hay bales; 2 m
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[obstructed|unobstructed]; {text}; {measurement value}'
slot_uri: MIXS:0001146
multivalued: true
alias: air_flow_impede
domain_of:
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>