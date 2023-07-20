# Slot: efficiency_percent


_Percentage of volatile solids removed from the anaerobic digestor_



URI: [MIXS:0000657](https://w3id.org/mixs/0000657)



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
| Preferred_unit | micromole per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: efficiency_percent
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter
description: Percentage of volatile solids removed from the anaerobic digestor
title: efficiency percent
notes:
- percent
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000657
multivalued: false
alias: efficiency_percent
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>