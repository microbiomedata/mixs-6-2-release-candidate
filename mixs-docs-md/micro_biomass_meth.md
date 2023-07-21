# Slot: micro_biomass_meth


_Reference or method used in determining microbial biomass_



URI: [MIXS:0000339](https://w3id.org/mixs/0000339)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| http://dx.doi.org/10.1016/j.soilbio.2005.01.021 |

## Comments

* slot name/scn was microbial_biomass_meth

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: micro_biomass_meth
description: Reference or method used in determining microbial biomass
title: microbial biomass method
notes:
- biomass
- method
- microbial
comments:
- slot name/scn was microbial_biomass_meth
examples:
- value: http://dx.doi.org/10.1016/j.soilbio.2005.01.021
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000339
alias: micro_biomass_meth
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