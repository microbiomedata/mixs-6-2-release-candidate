# Slot: tot_nitro_cont_meth


_Reference or method used in determining the total nitrogen_



URI: [MIXS:0000338](https://w3id.org/mixs/0000338)



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
| https://currentprotocols.onlinelibrary.wiley.com/doi/abs/10.1002/0471142913.fab0102s00 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: tot_nitro_cont_meth
description: Reference or method used in determining the total nitrogen
title: total nitrogen content method
notes:
- content
- method
- nitrogen
- total
examples:
- value: https://currentprotocols.onlinelibrary.wiley.com/doi/abs/10.1002/0471142913.fab0102s00
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000338
multivalued: false
alias: tot_nitro_cont_meth
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