# Slot: inorg_particles


_Concentration of particles such as sand, grit, metal particles, ceramics, etc.; can include multiple particles_



URI: [MIXS:0000664](https://w3id.org/mixs/0000664)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | inorganic particle name;measurement value || Preferred_unit | mole per liter, milligram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: inorg_particles
annotations:
  Expected_value:
    tag: Expected_value
    value: inorganic particle name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: mole per liter, milligram per liter
description: Concentration of particles such as sand, grit, metal particles, ceramics,
  etc.; can include multiple particles
title: inorganic particles
notes:
- inorganic
- particle
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000664
multivalued: true
alias: inorg_particles
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>