# Slot: spikein_metal


_Heavy metals used in research study to assess effects of exposure on microbiome of a specific site.  Please list heavy metals and concentration used for spike-in_



URI: [MIXS:0001172](https://w3id.org/mixs/0001172)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Cd at 20 ppm |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | heavy metal name or chemical symbol; concentration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: spikein_metal
annotations:
  Expected_value:
    tag: Expected_value
    value: heavy metal name or chemical symbol; concentration
description: Heavy metals used in research study to assess effects of exposure on
  microbiome of a specific site.  Please list heavy metals and concentration used
  for spike-in
title: spike-in with heavy metals
notes:
- heavy
- spike
examples:
- value: Cd at 20 ppm
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text} {integer}'
slot_uri: MIXS:0001172
multivalued: true
alias: spikein_metal
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>