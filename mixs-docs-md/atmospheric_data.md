# Slot: atmospheric_data


_Measurement of atmospheric data; can include multiple data_



URI: [MIXS:0001097](https://w3id.org/mixs/0001097)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| wind speed;9 knots |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | atmospheric data name;measurement value |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: atmospheric_data
annotations:
  Expected_value:
    tag: Expected_value
    value: atmospheric data name;measurement value
description: Measurement of atmospheric data; can include multiple data
title: atmospheric data
examples:
- value: wind speed;9 knots
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0001097
multivalued: true
alias: atmospheric_data
domain_of:
- Water
range: string
required: false
recommended: false

```
</details>