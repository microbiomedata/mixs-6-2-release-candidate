# Slot: cur_vegetation


_Vegetation classification from one or more standard classification systems, or agricultural crop_



URI: [MIXS:0000312](https://w3id.org/mixs/0000312)



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





### Annotations

| property | value |
| --- | --- |
| Expected_value | current vegetation type |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: cur_vegetation
annotations:
  Expected_value:
    tag: Expected_value
    value: current vegetation type
description: Vegetation classification from one or more standard classification systems,
  or agricultural crop
title: current vegetation
notes:
- vegetation
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000312
multivalued: false
alias: cur_vegetation
domain_of:
- Agriculture
- Soil
range: string

```
</details>