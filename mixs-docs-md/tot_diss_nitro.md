# Slot: tot_diss_nitro


_Total dissolved nitrogen concentration, reported as nitrogen, measured by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen_



URI: [MIXS:0000744](https://w3id.org/mixs/0000744)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 40 microgram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | microgram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: tot_diss_nitro
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per liter
description: 'Total dissolved nitrogen concentration, reported as nitrogen, measured
  by: total dissolved nitrogen = NH4 + NO3NO2 + dissolved organic nitrogen'
title: total dissolved nitrogen
notes:
- dissolved
- nitrogen
- total
examples:
- value: 40 microgram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000744
multivalued: false
alias: tot_diss_nitro
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>