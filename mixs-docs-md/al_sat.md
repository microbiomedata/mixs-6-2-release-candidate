# Slot: al_sat


_Aluminum saturation (esp. For tropical soils)_



URI: [MIXS:0000607](https://w3id.org/mixs/0000607)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Soil](Soil.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: al_sat
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: Aluminum saturation (esp. For tropical soils)
title: extreme_unusual_properties/Al saturation
notes:
- extreme
- properties
- saturation
- unusual
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000607
multivalued: false
alias: al_sat
domain_of:
- Soil
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>