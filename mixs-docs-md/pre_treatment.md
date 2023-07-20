# Slot: pre_treatment


_The process of pre-treatment removes materials that can be easily collected from the raw wastewater_



URI: [MIXS:0000348](https://w3id.org/mixs/0000348)



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
| Expected_value | pre-treatment type |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pre_treatment
annotations:
  Expected_value:
    tag: Expected_value
    value: pre-treatment type
description: The process of pre-treatment removes materials that can be easily collected
  from the raw wastewater
title: pre-treatment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000348
multivalued: false
alias: pre_treatment
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>