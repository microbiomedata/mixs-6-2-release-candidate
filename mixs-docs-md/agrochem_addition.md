# Slot: agrochem_addition


_Addition of fertilizers, pesticides, etc. - amount and time of applications_



URI: [MIXS:0000639](https://w3id.org/mixs/0000639)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[Soil](Soil.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| roundup;5 milligram per liter;2018-06-21 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | agrochemical name;agrochemical amount;timestamp || Preferred_unit | gram, mole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: agrochem_addition
annotations:
  Expected_value:
    tag: Expected_value
    value: agrochemical name;agrochemical amount;timestamp
  Preferred_unit:
    tag: Preferred_unit
    value: gram, mole per liter, milligram per liter
description: Addition of fertilizers, pesticides, etc. - amount and time of applications
title: history/agrochemical additions
notes:
- history
examples:
- value: roundup;5 milligram per liter;2018-06-21
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit};{timestamp}'
slot_uri: MIXS:0000639
multivalued: true
alias: agrochem_addition
domain_of:
- Agriculture
- Soil
range: string
required: false
recommended: false

```
</details>