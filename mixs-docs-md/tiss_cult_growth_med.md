# Slot: tiss_cult_growth_med


_Description of plant tissue culture growth media used_



URI: [MIXS:0001070](https://w3id.org/mixs/0001070)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PlantAssociated](PlantAssociated.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| https://link.springer.com/content/pdf/10.1007/BF02796489.pdf |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: tiss_cult_growth_med
description: Description of plant tissue culture growth media used
title: tissue culture growth media
notes:
- culture
- growth
examples:
- value: https://link.springer.com/content/pdf/10.1007/BF02796489.pdf
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001070
multivalued: false
alias: tiss_cult_growth_med
domain_of:
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