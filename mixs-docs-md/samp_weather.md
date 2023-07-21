# Slot: samp_weather


_The weather on the sampling day_



URI: [MIXS:0000827](https://w3id.org/mixs/0000827)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [SAMPWEATHERENUM](SAMPWEATHERENUM.md)






## Examples

| Value |
| --- |
| foggy |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_weather
description: The weather on the sampling day
title: sampling day weather
notes:
- day
- weather
examples:
- value: foggy
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000827
multivalued: false
alias: samp_weather
domain_of:
- BuiltEnvironment
range: SAMP_WEATHER_ENUM
required: false
recommended: false

```
</details>