# Slot: glucosidase_act


_Measurement of glucosidase activity_



URI: [MIXS:0000137](https://w3id.org/mixs/0000137)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 5 mol per liter per hour |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | mol per liter per hour |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: glucosidase_act
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: mol per liter per hour
description: Measurement of glucosidase activity
title: glucosidase activity
examples:
- value: 5 mol per liter per hour
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000137
multivalued: false
alias: glucosidase_act
domain_of:
- MicrobialMatBiofilm
- Sediment
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>