# Slot: air_PM_concen


_Concentration of substances that remain suspended in the air, and comprise mixtures of organic and inorganic substances (PM10 and PM2.5); can report multiple PM's by entering numeric values preceded by name of PM_



URI: [MIXS:0000108](https://w3id.org/mixs/0000108)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| PM2.5;10 microgram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | particulate matter name;measurement value |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: air_PM_concen
annotations:
  Expected_value:
    tag: Expected_value
    value: particulate matter name;measurement value
description: Concentration of substances that remain suspended in the air, and comprise
  mixtures of organic and inorganic substances (PM10 and PM2.5); can report multiple
  PM's by entering numeric values preceded by name of PM
title: air particulate matter concentration
notes:
- air
- concentration
- particle
- particulate
examples:
- value: PM2.5;10 microgram per cubic meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000108
multivalued: true
alias: air_PM_concen
domain_of:
- Air
- FoodFarmEnvironment
range: string
required: false
recommended: false

```
</details>