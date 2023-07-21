# Slot: tot_org_c_meth


_Reference or method used in determining total organic carbon_



URI: [MIXS:0000337](https://w3id.org/mixs/0000337)



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
| https://www.epa.gov/sites/production/files/2015-12/documents/9060a.pdf |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: tot_org_c_meth
description: Reference or method used in determining total organic carbon
title: total organic carbon method
notes:
- carbon
- method
- organic
- total
examples:
- value: https://www.epa.gov/sites/production/files/2015-12/documents/9060a.pdf
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000337
multivalued: false
alias: tot_org_c_meth
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