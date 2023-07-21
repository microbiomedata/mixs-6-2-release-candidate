# Slot: samp_tvdss


_Depth of the sample i.e. The vertical distance between the sea level and the sampled position in the subsurface. Depth can be reported as an interval for subsurface samples e.g. 1325.75-1362.25 m_



URI: [MIXS:0000409](https://w3id.org/mixs/0000409)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Recommended: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value or measurement value range || Preferred_unit | meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_tvdss
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value or measurement value range
  Preferred_unit:
    tag: Preferred_unit
    value: meter
description: Depth of the sample i.e. The vertical distance between the sea level
  and the sampled position in the subsurface. Depth can be reported as an interval
  for subsurface samples e.g. 1325.75-1362.25 m
title: sample true vertical depth subsea
notes:
- depth
- sample
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{float}-{float} {unit}'
slot_uri: MIXS:0000409
multivalued: false
alias: samp_tvdss
domain_of:
- HydrocarbonResourcesCores
range: string
recommended: true

```
</details>