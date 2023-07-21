# Slot: particle_class


_Particles are classified, based on their size, into six general categories:clay, silt, sand, gravel, cobbles, and boulders; should include amount of particle preceded by the name of the particle type; can include multiple values_



URI: [MIXS:0000206](https://w3id.org/mixs/0000206)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Sediment](Sediment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | particle name;measurement value || Preferred_unit | micrometer |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: particle_class
annotations:
  Expected_value:
    tag: Expected_value
    value: particle name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: micrometer
description: Particles are classified, based on their size, into six general categories:clay,
  silt, sand, gravel, cobbles, and boulders; should include amount of particle preceded
  by the name of the particle type; can include multiple values
title: particle classification
notes:
- classification
- particle
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000206
multivalued: true
alias: particle_class
domain_of:
- Sediment
range: string
required: false
recommended: false

```
</details>