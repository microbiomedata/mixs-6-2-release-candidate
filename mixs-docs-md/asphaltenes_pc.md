# Slot: asphaltenes_pc


_Saturate, Aromatic, Resin and Asphaltene(SARA) is an analysis method that dividescrude oilcomponents according to their polarizability and polarity. There are three main methods to obtain SARA results. The most popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)_



URI: [MIXS:0000135](https://w3id.org/mixs/0000135)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | percent |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: asphaltenes_pc
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percent
description: 'Saturate, Aromatic, Resin and Asphaltene(SARA) is an analysis method
  that dividescrude oilcomponents according to their polarizability and polarity.
  There are three main methods to obtain SARA results. The most popular one is known
  as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)'
title: asphaltenes wt%
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000135
multivalued: false
alias: asphaltenes_pc
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
recommended: true
structured_pattern:
  syntax: '{name};{float} {unit}'
  interpolated: true
  partial_match: true

```
</details>