# Slot: annual_precpt


_The average of all annual precipitation values known, or an estimated equivalent value derived by such methods as regional indexes or Isohyetal maps_



URI: [MIXS:0000644](https://w3id.org/mixs/0000644)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[Soil](Soil.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | millimeter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: annual_precpt
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: millimeter
description: The average of all annual precipitation values known, or an estimated
  equivalent value derived by such methods as regional indexes or Isohyetal maps
title: mean annual precipitation
notes:
- mean
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000644
multivalued: false
alias: annual_precpt
domain_of:
- Agriculture
- Soil
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>