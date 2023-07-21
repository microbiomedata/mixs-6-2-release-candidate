# Slot: ceil_thermal_mass


_The ability of the ceiling to provide inertia against temperature fluctuations. Generally this means concrete that is exposed. A metal deck that supports a concrete slab will act thermally as long as it is exposed to room air flow_



URI: [MIXS:0000143](https://w3id.org/mixs/0000143)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | joule per degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: ceil_thermal_mass
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: joule per degree Celsius
description: The ability of the ceiling to provide inertia against temperature fluctuations.
  Generally this means concrete that is exposed. A metal deck that supports a concrete
  slab will act thermally as long as it is exposed to room air flow
title: ceiling thermal mass
notes:
- ceiling
- mass
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000143
multivalued: false
alias: ceil_thermal_mass
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>