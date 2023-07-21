# Slot: viscosity


_A measure of oil's resistanceto gradual deformation byshear stressortensile stress (e.g. 3.5 cp; 100 C)_



URI: [MIXS:0000126](https://w3id.org/mixs/0000126)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value;measurement value || Preferred_unit | cP at degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: viscosity
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: cP at degree Celsius
description: A measure of oil's resistanceto gradual deformation byshear stressortensile
  stress (e.g. 3.5 cp; 100 C)
title: viscosity
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} {unit};{float} {unit}'
slot_uri: MIXS:0000126
multivalued: false
alias: viscosity
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false

```
</details>