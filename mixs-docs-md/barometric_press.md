# Slot: barometric_press


_Force per unit area exerted against a surface by the weight of air above that surface_



URI: [MIXS:0000096](https://w3id.org/mixs/0000096)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 5 millibar |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | millibar |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: barometric_press
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: millibar
description: Force per unit area exerted against a surface by the weight of air above
  that surface
title: barometric pressure
notes:
- pressure
examples:
- value: 5 millibar
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000096
multivalued: false
alias: barometric_press
domain_of:
- Air
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>