# Slot: tot_inorg_nitro


_Total inorganic nitrogen content_



URI: [MIXS:0000745](https://w3id.org/mixs/0000745)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 40 microgram per liter |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | microgram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: tot_inorg_nitro
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: microgram per liter
description: Total inorganic nitrogen content
title: total inorganic nitrogen
notes:
- inorganic
- nitrogen
- total
examples:
- value: 40 microgram per liter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000745
multivalued: false
alias: tot_inorg_nitro
domain_of:
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>