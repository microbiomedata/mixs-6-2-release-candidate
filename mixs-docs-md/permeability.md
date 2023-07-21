# Slot: permeability


_Measure of the ability of a hydrocarbon resource to allow fluids to pass through it. (Additional information: https://en.wikipedia.org/wiki/Permeability_(earth_sciences))_



URI: [MIXS:0000404](https://w3id.org/mixs/0000404)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value range || Preferred_unit | mD |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: permeability
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value range
  Preferred_unit:
    tag: Preferred_unit
    value: mD
description: 'Measure of the ability of a hydrocarbon resource to allow fluids to
  pass through it. (Additional information: https://en.wikipedia.org/wiki/Permeability_(earth_sciences))'
title: permeability
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{integer} - {integer} {unit}'
slot_uri: MIXS:0000404
multivalued: false
alias: permeability
domain_of:
- HydrocarbonResourcesCores
range: string
required: false
recommended: false

```
</details>