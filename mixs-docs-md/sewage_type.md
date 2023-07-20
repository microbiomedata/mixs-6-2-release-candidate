# Slot: sewage_type


_Type of wastewater treatment plant as municipial or industrial_



URI: [MIXS:0000215](https://w3id.org/mixs/0000215)



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
| Expected_value | sewage type name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: sewage_type
annotations:
  Expected_value:
    tag: Expected_value
    value: sewage type name
description: Type of wastewater treatment plant as municipial or industrial
title: sewage type
notes:
- type
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000215
multivalued: false
alias: sewage_type
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>