# Slot: non_min_nutr_regm


_Information about treatment involving the exposure of plant to non-mineral nutrient such as oxygen, hydrogen or carbon; should include the name of non-mineral nutrient, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple non-mineral nutrient regimens_



URI: [MIXS:0000571](https://w3id.org/mixs/0000571)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| carbon dioxide;10 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram, mole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: non_min_nutr_regm
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram, mole per liter, milligram per liter
description: Information about treatment involving the exposure of plant to non-mineral
  nutrient such as oxygen, hydrogen or carbon; should include the name of non-mineral
  nutrient, amount administered, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple non-mineral nutrient regimens
title: non-mineral nutrient regimen
notes:
- non-mineral
- nutrient
- regimen
examples:
- value: carbon dioxide;10 mole per liter;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000571
multivalued: true
alias: non_min_nutr_regm
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>