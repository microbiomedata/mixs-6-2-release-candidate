# Slot: tot_nitro


_Total nitrogen concentration of water samples, calculated by: total nitrogen = total dissolved nitrogen + particulate nitrogen. Can also be measured without filtering, reported as nitrogen_



URI: [MIXS:0000102](https://w3id.org/mixs/0000102)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 50 micromole per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | microgram per liter, micromole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: tot_nitro
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per liter, micromole per liter, milligram per liter
description: 'Total nitrogen concentration of water samples, calculated by: total
  nitrogen = total dissolved nitrogen + particulate nitrogen. Can also be measured
  without filtering, reported as nitrogen'
title: total nitrogen concentration
notes:
- concentration
- nitrogen
- total
examples:
- value: 50 micromole per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000102
multivalued: false
alias: tot_nitro
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
- WastewaterSludge
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>