# Slot: samp_md


_In non deviated well, measured depth is equal to the true vertical depth, TVD (TVD=TVDSS plus the reference or datum it refers to). In deviated wells, the MD is the length of trajectory of the borehole measured from the same reference or datum. Common datums used are ground level (GL), drilling rig floor (DF), rotary table (RT), kelly bushing (KB) and mean sea level (MSL). If "other" is specified, please propose entry in "additional info" field_



URI: [MIXS:0000413](https://w3id.org/mixs/0000413)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 1534 meter;MSL |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value;enumeration || Preferred_unit | meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_md
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value;enumeration
  Preferred_unit:
    tag: Preferred_unit
    value: meter
description: In non deviated well, measured depth is equal to the true vertical depth,
  TVD (TVD=TVDSS plus the reference or datum it refers to). In deviated wells, the
  MD is the length of trajectory of the borehole measured from the same reference
  or datum. Common datums used are ground level (GL), drilling rig floor (DF), rotary
  table (RT), kelly bushing (KB) and mean sea level (MSL). If "other" is specified,
  please propose entry in "additional info" field
title: sample measured depth
notes:
- depth
- measurement
- sample
examples:
- value: 1534 meter;MSL
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float} {unit};[GL|DF|RT|KB|MSL|other]'
slot_uri: MIXS:0000413
multivalued: false
alias: samp_md
domain_of:
- HydrocarbonResourcesCores
range: string
required: false
recommended: false

```
</details>