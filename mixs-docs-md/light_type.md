# Slot: light_type


_Application of light to achieve some practical or aesthetic effect. Lighting includes the use of both artificial light sources such as lamps and light fixtures, as well as natural illumination by capturing daylight. Can also include absence of light_



URI: [MIXS:0000769](https://w3id.org/mixs/0000769)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [LIGHTTYPEENUM](LIGHTTYPEENUM.md)

* Multivalued: True

* Required: True






## Examples

| Value |
| --- |
| desk lamp |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: light_type
description: Application of light to achieve some practical or aesthetic effect. Lighting
  includes the use of both artificial light sources such as lamps and light fixtures,
  as well as natural illumination by capturing daylight. Can also include absence
  of light
title: light type
notes:
- light
- type
examples:
- value: desk lamp
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000769
multivalued: true
alias: light_type
domain_of:
- BuiltEnvironment
range: LIGHT_TYPE_ENUM
required: true

```
</details>