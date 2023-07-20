# Slot: ph_meth

URI: [MIXS:0001106](https://w3id.org/mixs/0001106)



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
| https://www.epa.gov/sites/production/files/2015-12/documents/9040c.pdf |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ph_meth
title: pH method
notes:
- method
- ph
examples:
- value: https://www.epa.gov/sites/production/files/2015-12/documents/9040c.pdf
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001106
multivalued: false
alias: ph_meth
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