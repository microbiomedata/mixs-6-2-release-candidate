# Slot: samp_transport_cond


_Sample transport duration (in days or hrs) and temperature the sample was exposed to (e.g. 5.5 days; 20 C)_



URI: [MIXS:0000410](https://w3id.org/mixs/0000410)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 5 days;-20 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | measurement value;measurement value || Preferred_unit | days;degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_transport_cond
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: days;degree Celsius
description: Sample transport duration (in days or hrs) and temperature the sample
  was exposed to (e.g. 5.5 days; 20 C)
title: sample transport conditions
notes:
- condition
- sample
- transport
examples:
- value: 5 days;-20 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {unit};{float} {unit}'
slot_uri: MIXS:0000410
multivalued: false
alias: samp_transport_cond
domain_of:
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
required: false
recommended: false

```
</details>