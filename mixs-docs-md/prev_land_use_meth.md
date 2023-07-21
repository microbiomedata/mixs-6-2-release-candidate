# Slot: prev_land_use_meth


_Reference or method used in determining previous land use and dates_



URI: [MIXS:0000316](https://w3id.org/mixs/0000316)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: prev_land_use_meth
description: Reference or method used in determining previous land use and dates
title: history/previous land use method
notes:
- history
- land
- method
- use
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000316
multivalued: false
alias: prev_land_use_meth
domain_of:
- Agriculture
- Soil
range: string
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}'
  interpolated: true
  partial_match: true

```
</details>