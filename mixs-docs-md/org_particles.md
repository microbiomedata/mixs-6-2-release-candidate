# Slot: org_particles


_Concentration of particles such as faeces, hairs, food, vomit, paper fibers, plant material, humus, etc_



URI: [MIXS:0000665](https://w3id.org/mixs/0000665)



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
| Expected_value | particle name;measurement value || Preferred_unit | gram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: org_particles
annotations:
  Expected_value:
    tag: Expected_value
    value: particle name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: gram per liter
description: Concentration of particles such as faeces, hairs, food, vomit, paper
  fibers, plant material, humus, etc
title: organic particles
notes:
- organic
- particle
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000665
multivalued: true
alias: org_particles
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>