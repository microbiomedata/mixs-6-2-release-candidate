# Slot: biochem_oxygen_dem


_Amount of dissolved oxygen needed by aerobic biological organisms in a body of water to break down organic material present in a given water sample at certain temperature over a specific time period_



URI: [MIXS:0000653](https://w3id.org/mixs/0000653)



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
name: biochem_oxygen_dem
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: milligram per liter
description: Amount of dissolved oxygen needed by aerobic biological organisms in
  a body of water to break down organic material present in a given water sample at
  certain temperature over a specific time period
title: biochemical oxygen demand
notes:
- oxygen
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000653
multivalued: false
alias: biochem_oxygen_dem
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>