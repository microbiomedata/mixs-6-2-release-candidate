# Slot: plant_part_maturity


_A description of the stage of development of a plant or plant part based on maturity or ripeness. This field accepts terms listed under degree of plant maturity (http://purl.obolibrary.org/obo/FOODON_03530050)_



URI: [MIXS:0001120](https://w3id.org/mixs/0001120)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| ripe or mature [FOODON:03530052] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03530050 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: plant_part_maturity
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03530050
description: A description of the stage of development of a plant or plant part based
  on maturity or ripeness. This field accepts terms listed under degree of plant maturity
  (http://purl.obolibrary.org/obo/FOODON_03530050)
title: degree of plant part maturity
notes:
- degree
- plant
examples:
- value: ripe or mature [FOODON:03530052]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{term label}{term ID}'
slot_uri: MIXS:0001120
multivalued: false
alias: plant_part_maturity
domain_of:
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>