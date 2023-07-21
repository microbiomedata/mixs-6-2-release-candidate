# Slot: local_class


_Soil classification based on local soil classification system_



URI: [MIXS:0000330](https://w3id.org/mixs/0000330)



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
| Expected_value | local classification name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: local_class
annotations:
  Expected_value:
    tag: Expected_value
    value: local classification name
description: Soil classification based on local soil classification system
title: soil_taxonomic/local classification
notes:
- classification
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000330
multivalued: false
alias: local_class
domain_of:
- Agriculture
- Soil
range: string

```
</details>