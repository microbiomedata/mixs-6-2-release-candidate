# Slot: diss_oxygen_fluid


_Concentration of dissolved oxygen in the oil field produced fluids as it contributes to oxgen-corrosion and microbial activity (e.g. Mic)_



URI: [MIXS:0000438](https://w3id.org/mixs/0000438)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micromole per kilogram, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: diss_oxygen_fluid
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per kilogram, milligram per liter
description: Concentration of dissolved oxygen in the oil field produced fluids as
  it contributes to oxgen-corrosion and microbial activity (e.g. Mic)
title: dissolved oxygen in fluids
notes:
- dissolved
- oxygen
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000438
multivalued: false
alias: diss_oxygen_fluid
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>