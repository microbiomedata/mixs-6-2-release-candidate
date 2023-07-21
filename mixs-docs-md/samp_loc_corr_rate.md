# Slot: samp_loc_corr_rate


_Metal corrosion rate is the speed of metal deterioration due to environmental conditions. As environmental conditions change corrosion rates change accordingly. Therefore, long term corrosion rates are generally more informative than short term rates and for that reason they are preferred during reporting. In the case of suspected MIC, corrosion rate measurements at the time of sampling might provide insights into the involvement of certain microbial community members in MIC as well as potential microbial interplays_



URI: [MIXS:0000136](https://w3id.org/mixs/0000136)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | millimeter per year |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_loc_corr_rate
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: millimeter per year
description: Metal corrosion rate is the speed of metal deterioration due to environmental
  conditions. As environmental conditions change corrosion rates change accordingly.
  Therefore, long term corrosion rates are generally more informative than short term
  rates and for that reason they are preferred during reporting. In the case of suspected
  MIC, corrosion rate measurements at the time of sampling might provide insights
  into the involvement of certain microbial community members in MIC as well as potential
  microbial interplays
title: corrosion rate at sample location
notes:
- location
- rate
- sample
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000136
multivalued: false
alias: samp_loc_corr_rate
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: string
recommended: true
structured_pattern:
  syntax: '{float} - {float} {unit}'
  interpolated: true
  partial_match: true

```
</details>