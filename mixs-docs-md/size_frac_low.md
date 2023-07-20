# Slot: size_frac_low


_Refers to the mesh/pore size used to pre-filter/pre-sort the sample. Materials larger than the size threshold are excluded from the sample_



URI: [MIXS:0000735](https://w3id.org/mixs/0000735)



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
| 0.2 micrometer |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | micrometer |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: size_frac_low
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: micrometer
description: Refers to the mesh/pore size used to pre-filter/pre-sort the sample.
  Materials larger than the size threshold are excluded from the sample
title: size-fraction lower threshold
notes:
- lower
examples:
- value: 0.2 micrometer
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000735
multivalued: false
alias: size_frac_low
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