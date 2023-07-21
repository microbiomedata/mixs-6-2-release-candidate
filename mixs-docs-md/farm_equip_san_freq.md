# Slot: farm_equip_san_freq


_The number of times farm equipment is cleaned. Frequency of cleaning might be on a Daily basis, Weekly, Monthly, Quarterly or Annually_



URI: [MIXS:0001125](https://w3id.org/mixs/0001125)



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
| Biweekly |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: farm_equip_san_freq
description: The number of times farm equipment is cleaned. Frequency of cleaning
  might be on a Daily basis, Weekly, Monthly, Quarterly or Annually
title: farm equipment sanitization frequency
notes:
- equipment
- farm
- frequency
examples:
- value: Biweekly
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001125
multivalued: false
alias: farm_equip_san_freq
domain_of:
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>