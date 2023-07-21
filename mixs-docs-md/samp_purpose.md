# Slot: samp_purpose


_The reason that the sample was collected_



URI: [MIXS:0001151](https://w3id.org/mixs/0001151)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| field trial |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration or {text} |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_purpose
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration or {text}
description: The reason that the sample was collected
title: purpose of sampling
notes:
- purpose
examples:
- value: field trial
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[active surveillance in response to an outbreak|active surveillance
  not initiated by an outbreak|clinical trial|cluster investigation|environmental
  assessment|farm sample|field trial|for cause|industry internal investigation|market
  sample|passive surveillance|population based studies|research|research and development]
  or {text}'
slot_uri: MIXS:0001151
multivalued: false
alias: samp_purpose
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string

```
</details>