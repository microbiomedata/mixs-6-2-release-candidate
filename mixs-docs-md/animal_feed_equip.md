# Slot: animal_feed_equip


_Description of the feeding equipment used for livestock. This field accepts terms listed under feed delivery (http://opendata.inra.fr/EOL/EOL_0001757). Multiple terms can be separated by pipes_



URI: [MIXS:0001113](https://w3id.org/mixs/0001113)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| self feeding [EOL:0001645]| straight feed trough [EOL:0001661] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: animal_feed_equip
description: Description of the feeding equipment used for livestock. This field accepts
  terms listed under feed delivery (http://opendata.inra.fr/EOL/EOL_0001757). Multiple
  terms can be separated by pipes
title: animal feeding equipment
notes:
- animal
- equipment
examples:
- value: self feeding [EOL:0001645]| straight feed trough [EOL:0001661]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001113
multivalued: true
alias: animal_feed_equip
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>