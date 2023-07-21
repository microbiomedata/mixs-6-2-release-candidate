# Slot: anim_water_method


_Description of the equipment or method used to distribute water to livestock. This field accepts termed listed under water delivery equipment (http://opendata.inra.fr/EOL/EOL_0001653). Multiple terms can be separated by pipes_



URI: [MIXS:0001115](https://w3id.org/mixs/0001115)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| water trough [EOL:0001618] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: anim_water_method
description: Description of the equipment or method used to distribute water to livestock.
  This field accepts termed listed under water delivery equipment (http://opendata.inra.fr/EOL/EOL_0001653).
  Multiple terms can be separated by pipes
title: animal water delivery method
notes:
- animal
- delivery
- method
- water
examples:
- value: water trough [EOL:0001618]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001115
multivalued: true
alias: anim_water_method
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
required: false
recommended: false
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>