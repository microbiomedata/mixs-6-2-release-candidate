# Slot: water_cont_soil_meth


_Reference or method used in determining the water content of soil_



URI: [MIXS:0000323](https://w3id.org/mixs/0000323)



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


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: water_cont_soil_meth
description: Reference or method used in determining the water content of soil
title: water content method
notes:
- content
- method
- water
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000323
multivalued: false
alias: water_cont_soil_meth
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