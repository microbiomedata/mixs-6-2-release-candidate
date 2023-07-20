# Slot: pollutants


_Pollutant types and, amount or concentrations measured at the time of sampling; can report multiple pollutants by entering numeric values preceded by name of pollutant_



URI: [MIXS:0000107](https://w3id.org/mixs/0000107)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| lead;0.15 microgram per cubic meter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | pollutant name;measurement value || Preferred_unit | gram, mole per liter, milligram per liter, microgram per cubic meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pollutants
annotations:
  Expected_value:
    tag: Expected_value
    value: pollutant name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: gram, mole per liter, milligram per liter, microgram per cubic meter
description: Pollutant types and, amount or concentrations measured at the time of
  sampling; can report multiple pollutants by entering numeric values preceded by
  name of pollutant
title: pollutants
examples:
- value: lead;0.15 microgram per cubic meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000107
multivalued: true
alias: pollutants
domain_of:
- Air
range: string
required: false
recommended: false

```
</details>