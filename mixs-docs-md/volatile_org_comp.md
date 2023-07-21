# Slot: volatile_org_comp


_Concentration of carbon-based chemicals that easily evaporate at room temperature; can report multiple volatile organic compounds by entering numeric values preceded by name of compound_



URI: [MIXS:0000115](https://w3id.org/mixs/0000115)



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
| formaldehyde;500 nanogram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | volatile organic compound name;measurement value || Preferred_unit | microgram per cubic meter, parts per million, nanogram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: volatile_org_comp
annotations:
  Expected_value:
    tag: Expected_value
    value: volatile organic compound name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per cubic meter, parts per million, nanogram per liter
description: Concentration of carbon-based chemicals that easily evaporate at room
  temperature; can report multiple volatile organic compounds by entering numeric
  values preceded by name of compound
title: volatile organic compounds
notes:
- organic
examples:
- value: formaldehyde;500 nanogram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000115
multivalued: true
alias: volatile_org_comp
domain_of:
- Air
range: string
required: false
recommended: false

```
</details>