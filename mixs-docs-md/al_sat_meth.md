# Slot: al_sat_meth


_Reference or method used in determining Al saturation_



URI: [MIXS:0000324](https://w3id.org/mixs/0000324)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Soil](Soil.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: al_sat_meth
description: Reference or method used in determining Al saturation
title: extreme_unusual_properties/Al saturation method
notes:
- extreme
- method
- properties
- saturation
- unusual
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000324
multivalued: false
alias: al_sat_meth
domain_of:
- Soil
range: string
required: false
recommended: false
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}'
  interpolated: true
  partial_match: true

```
</details>