# Slot: spikein_count

URI: [MIXS:0001335](https://w3id.org/mixs/0001335)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| total prokaryotes;3.5e7 colony forming units per milliliter;qPCR |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | organism name;measurement value;enumeration || Preferred_unit | colony forming units per milliliter; colony forming units per gram of dry weight |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: spikein_count
annotations:
  Expected_value:
    tag: Expected_value
    value: organism name;measurement value;enumeration
  Preferred_unit:
    tag: Preferred_unit
    value: colony forming units per milliliter; colony forming units per gram of dry
      weight
title: spike-in organism count
notes:
- count
- organism
- spike
examples:
- value: total prokaryotes;3.5e7 colony forming units per milliliter;qPCR
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit};[ATP|MPN|qPCR|other]'
slot_uri: MIXS:0001335
multivalued: false
alias: spikein_count
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>