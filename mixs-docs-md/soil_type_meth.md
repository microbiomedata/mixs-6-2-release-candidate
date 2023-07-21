# Slot: soil_type_meth


_Reference or method used in determining soil series name or other lower-level classification_



URI: [MIXS:0000334](https://w3id.org/mixs/0000334)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Frederick series; Weikert series |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: soil_type_meth
description: Reference or method used in determining soil series name or other lower-level
  classification
title: soil type method
notes:
- method
- soil
- type
examples:
- value: Frederick series; Weikert series
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000334
multivalued: false
alias: soil_type_meth
domain_of:
- Agriculture
- FoodFarmEnvironment
- Soil
range: string
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}'
  interpolated: true
  partial_match: true

```
</details>