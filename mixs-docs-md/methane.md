# Slot: methane


_Methane (gas) amount or concentration at the time of sampling_



URI: [MIXS:0000101](https://w3id.org/mixs/0000101)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  yes  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micromole per liter, parts per billion, parts per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: methane
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter, parts per billion, parts per million
description: Methane (gas) amount or concentration at the time of sampling
title: methane
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000101
multivalued: false
alias: methane
domain_of:
- Air
- MicrobialMatBiofilm
- Sediment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>