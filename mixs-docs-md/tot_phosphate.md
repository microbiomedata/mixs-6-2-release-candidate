# Slot: tot_phosphate


_Total amount or concentration of phosphate_



URI: [MIXS:0000689](https://w3id.org/mixs/0000689)



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
| Preferred_unit | microgram per liter, micromole per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: tot_phosphate
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per liter, micromole per liter
description: Total amount or concentration of phosphate
title: total phosphate
notes:
- phosphate
- total
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000689
multivalued: false
alias: tot_phosphate
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>