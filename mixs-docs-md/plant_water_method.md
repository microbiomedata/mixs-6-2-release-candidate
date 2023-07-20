# Slot: plant_water_method


_Description of the equipment or method used to distribute water to crops. This field accepts termed listed under irrigation process (http://purl.obolibrary.org/obo/AGRO_00000006). Multiple terms can be separated by pipes_



URI: [MIXS:0001111](https://w3id.org/mixs/0001111)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| drip irrigation process [AGRO:00000056] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: plant_water_method
description: Description of the equipment or method used to distribute water to crops.
  This field accepts termed listed under irrigation process (http://purl.obolibrary.org/obo/AGRO_00000006).
  Multiple terms can be separated by pipes
title: plant water delivery method
notes:
- delivery
- method
- plant
- water
examples:
- value: drip irrigation process [AGRO:00000056]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001111
multivalued: false
alias: plant_water_method
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
recommended: true
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>