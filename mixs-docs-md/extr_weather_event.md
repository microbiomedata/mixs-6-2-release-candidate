# Slot: extr_weather_event


_Unusual weather events that may have affected microbial populations. Multiple terms can be separated by pipes, listed in reverse chronological order_



URI: [MIXS:0001141](https://w3id.org/mixs/0001141)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [EXTRWEATHEREVENTENUM](EXTRWEATHEREVENTENUM.md)

* Multivalued: True






## Examples

| Value |
| --- |
| hail |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: extr_weather_event
description: Unusual weather events that may have affected microbial populations.
  Multiple terms can be separated by pipes, listed in reverse chronological order
title: extreme weather event
notes:
- event
- extreme
- weather
examples:
- value: hail
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001141
multivalued: true
alias: extr_weather_event
domain_of:
- FoodFarmEnvironment
range: EXTR_WEATHER_EVENT_ENUM
required: false
recommended: false

```
</details>