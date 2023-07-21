# Slot: root_cond


_Relevant rooting conditions such as field plot size, sowing density, container dimensions, number of plants per container_



URI: [MIXS:0001061](https://w3id.org/mixs/0001061)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| http://himedialabs.com/TD/PT158.pdf |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: root_cond
description: Relevant rooting conditions such as field plot size, sowing density,
  container dimensions, number of plants per container
title: rooting conditions
notes:
- condition
examples:
- value: http://himedialabs.com/TD/PT158.pdf
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001061
multivalued: false
alias: root_cond
domain_of:
- FoodFarmEnvironment
- PlantAssociated
range: string
required: false
recommended: false
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}|{text}'
  interpolated: true
  partial_match: true

```
</details>