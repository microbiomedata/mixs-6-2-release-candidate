# Slot: size_frac_up


_Refers to the mesh/pore size used to retain the sample. Materials smaller than the size threshold are excluded from the sample_



URI: [MIXS:0000736](https://w3id.org/mixs/0000736)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 20 micrometer |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micrometer |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: size_frac_up
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micrometer
description: Refers to the mesh/pore size used to retain the sample. Materials smaller
  than the size threshold are excluded from the sample
title: size-fraction upper threshold
notes:
- upper
examples:
- value: 20 micrometer
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000736
multivalued: false
alias: size_frac_up
domain_of:
- Agriculture
- FoodFarmEnvironment
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>