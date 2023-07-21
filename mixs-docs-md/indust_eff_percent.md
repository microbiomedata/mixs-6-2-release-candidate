# Slot: indust_eff_percent


_Percentage of industrial effluents received by wastewater treatment plant_



URI: [MIXS:0000662](https://w3id.org/mixs/0000662)



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
| Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: indust_eff_percent
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: Percentage of industrial effluents received by wastewater treatment plant
title: industrial effluent percent
notes:
- percent
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000662
multivalued: false
alias: indust_eff_percent
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>