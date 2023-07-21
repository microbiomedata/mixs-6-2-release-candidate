# Slot: mineral_nutr_regm


_Information about treatment involving the use of mineral supplements; should include the name of mineral nutrient, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple mineral nutrient regimens_



URI: [MIXS:0000570](https://w3id.org/mixs/0000570)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| potassium;15 gram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | mineral nutrient name;mineral nutrient amount;treatment interval and duration || Preferred_unit | gram, mole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: mineral_nutr_regm
annotations:
  Expected_value:
    tag: Expected_value
    value: mineral nutrient name;mineral nutrient amount;treatment interval and duration
  Preferred_unit:
    tag: Preferred_unit
    value: gram, mole per liter, milligram per liter
description: Information about treatment involving the use of mineral supplements;
  should include the name of mineral nutrient, amount administered, treatment regimen
  including how many times the treatment was repeated, how long each treatment lasted,
  and the start and end time of the entire treatment; can include multiple mineral
  nutrient regimens
title: mineral nutrient regimen
notes:
- mineral
- nutrient
- regimen
examples:
- value: potassium;15 gram;R2/2018-05-11T14:30/2018-05-11T19:30/P1H30M
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit};{Rn/start_time/end_time/duration}'
slot_uri: MIXS:0000570
multivalued: true
alias: mineral_nutr_regm
domain_of:
- PlantAssociated
range: string
required: false
recommended: false

```
</details>