# Slot: enrichment_protocol


_The microbiological workflow or protocol followed to test for the presence or enumeration of the target microbial analyte(s). Please provide a PubMed or DOI reference for published protocols_



URI: [MIXS:0001177](https://w3id.org/mixs/0001177)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| BAM Chapter 4: Enumeration of Escherichia coli and the Coliform Bacteria |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: enrichment_protocol
description: The microbiological workflow or protocol followed to test for the presence
  or enumeration of the target microbial analyte(s). Please provide a PubMed or DOI
  reference for published protocols
title: enrichment protocol
notes:
- enrichment
- protocol
examples:
- value: 'BAM Chapter 4: Enumeration of Escherichia coli and the Coliform Bacteria'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001177
multivalued: false
alias: enrichment_protocol
domain_of:
- Agriculture
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
range: string
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}|{text}'
  interpolated: true
  partial_match: true

```
</details>