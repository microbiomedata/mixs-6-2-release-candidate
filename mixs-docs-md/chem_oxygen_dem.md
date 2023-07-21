# Slot: chem_oxygen_dem


_A measure of the capacity of water to consume oxygen during the decomposition of organic matter and the oxidation of inorganic chemicals such as ammonia and nitrite_



URI: [MIXS:0000656](https://w3id.org/mixs/0000656)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: chem_oxygen_dem
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: A measure of the capacity of water to consume oxygen during the decomposition
  of organic matter and the oxidation of inorganic chemicals such as ammonia and nitrite
title: chemical oxygen demand
notes:
- oxygen
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000656
multivalued: false
alias: chem_oxygen_dem
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>