# Slot: store_cond


_Explain how and for how long the soil sample was stored before DNA extraction (fresh/frozen/other)_



URI: [MIXS:0000327](https://w3id.org/mixs/0000327)



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
| -20 degree Celsius freezer;P2Y10D |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | storage condition type;duration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: store_cond
annotations:
  Expected_value:
    tag: Expected_value
    value: storage condition type;duration
description: Explain how and for how long the soil sample was stored before DNA extraction
  (fresh/frozen/other)
title: storage conditions
notes:
- condition
- storage
examples:
- value: -20 degree Celsius freezer;P2Y10D
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{period}'
slot_uri: MIXS:0000327
multivalued: false
alias: store_cond
domain_of:
- Agriculture
- Soil
range: string

```
</details>