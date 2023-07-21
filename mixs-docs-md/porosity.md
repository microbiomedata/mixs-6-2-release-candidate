# Slot: porosity


_Porosity of deposited sediment is volume of voids divided by the total volume of sample_



URI: [MIXS:0000211](https://w3id.org/mixs/0000211)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value or range || Preferred_unit | percentage |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: porosity
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value or range
  Preferred_unit:
    tag: Preferred_unit
    value: percentage
description: Porosity of deposited sediment is volume of voids divided by the total
  volume of sample
title: porosity
notes:
- porosity
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} - {float} {unit}'
slot_uri: MIXS:0000211
multivalued: false
alias: porosity
domain_of:
- Agriculture
- HydrocarbonResourcesCores
- Sediment
range: string
required: false
recommended: false

```
</details>