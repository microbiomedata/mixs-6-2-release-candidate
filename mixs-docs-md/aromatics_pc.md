# Slot: aromatics_pc


_Saturate, Aromatic, Resin and Asphaltene(SARA) is an analysis method that dividescrude oilcomponents according to their polarizability and polarity. There are three main methods to obtain SARA results. The most popular one is known as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)_



URI: [MIXS:0000133](https://w3id.org/mixs/0000133)



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


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: aromatics_pc
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percent
description: 'Saturate, Aromatic, Resin and Asphaltene(SARA) is an analysis method
  that dividescrude oilcomponents according to their polarizability and polarity.
  There are three main methods to obtain SARA results. The most popular one is known
  as the Iatroscan TLC-FID and is referred to as IP-143 (source: https://en.wikipedia.org/wiki/Saturate,_aromatic,_resin_and_asphaltene)'
title: aromatics wt%
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000133
multivalued: false
alias: aromatics_pc
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