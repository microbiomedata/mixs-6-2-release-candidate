# Slot: suspend_solids


_Concentration of substances including a wide variety of material, such as silt, decaying plant and animal matter; can include multiple substances_



URI: [MIXS:0000150](https://w3id.org/mixs/0000150)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | suspended solid name;measurement value || Preferred_unit | gram, microgram, milligram per liter, mole per liter, gram per liter, part per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: suspend_solids
annotations:
  Expected_value:
    tag: Expected_value
    value: suspended solid name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: gram, microgram, milligram per liter, mole per liter, gram per liter, part
      per million
description: Concentration of substances including a wide variety of material, such
  as silt, decaying plant and animal matter; can include multiple substances
title: suspended solids
notes:
- solids
- suspended
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000150
multivalued: true
alias: suspend_solids
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>