# Slot: samp_time_out


_The recent and long term history of outside sampling_



URI: [MIXS:0000196](https://w3id.org/mixs/0000196)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | time || Preferred_unit | hour |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_time_out
annotations:
  Expected_value:
    tag: Expected_value
    value: time
  Preferred_unit:
    tag: Preferred_unit
    value: hour
description: The recent and long term history of outside sampling
title: sampling time outside
notes:
- time
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float}'
slot_uri: MIXS:0000196
multivalued: false
alias: samp_time_out
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>