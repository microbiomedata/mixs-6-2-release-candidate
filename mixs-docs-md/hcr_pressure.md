# Slot: hcr_pressure


_Original pressure of the hydrocarbon resource_



URI: [MIXS:0000395](https://w3id.org/mixs/0000395)



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
| Preferred_unit | atmosphere, kilopascal |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: hcr_pressure
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: atmosphere, kilopascal
description: Original pressure of the hydrocarbon resource
title: hydrocarbon resource original pressure
notes:
- hydrocarbon
- pressure
- resource
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000395
multivalued: false
alias: hcr_pressure
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false
structured_pattern:
  syntax: '{float} - {float} {unit}'
  interpolated: true
  partial_match: true

```
</details>