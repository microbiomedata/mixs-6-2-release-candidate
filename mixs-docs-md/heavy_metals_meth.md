# Slot: heavy_metals_meth


_Reference or method used in determining heavy metals_



URI: [MIXS:0000343](https://w3id.org/mixs/0000343)



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
name: heavy_metals_meth
description: Reference or method used in determining heavy metals
title: extreme_unusual_properties/heavy metals method
notes:
- extreme
- method
- properties
- unusual
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000343
multivalued: false
alias: heavy_metals_meth
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