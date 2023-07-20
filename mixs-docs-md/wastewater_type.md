# Slot: wastewater_type


_The origin of wastewater such as human waste, rainfall, storm drains, etc_



URI: [MIXS:0000353](https://w3id.org/mixs/0000353)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | wastewater type name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: wastewater_type
annotations:
  Expected_value:
    tag: Expected_value
    value: wastewater type name
description: The origin of wastewater such as human waste, rainfall, storm drains,
  etc
title: wastewater type
notes:
- type
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000353
multivalued: false
alias: wastewater_type
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>