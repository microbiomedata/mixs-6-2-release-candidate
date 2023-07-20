# Slot: slope_aspect


_The direction a slope faces. While looking down a slope use a compass to record the direction you are facing (direction or degrees); e.g., nw or 315 degrees. This measure provides an indication of sun and wind exposure that will influence soil temperature and evapotranspiration_



URI: [MIXS:0000647](https://w3id.org/mixs/0000647)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: slope_aspect
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree
description: The direction a slope faces. While looking down a slope use a compass
  to record the direction you are facing (direction or degrees); e.g., nw or 315 degrees.
  This measure provides an indication of sun and wind exposure that will influence
  soil temperature and evapotranspiration
title: slope aspect
notes:
- slope
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000647
multivalued: false
alias: slope_aspect
domain_of:
- Agriculture
- Soil
range: string
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>