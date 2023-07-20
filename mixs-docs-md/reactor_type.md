# Slot: reactor_type


_Anaerobic digesters can be designed and engineered to operate using a number of different process configurations, as batch or continuous, mesophilic, high solid or low solid, and single stage or multistage_



URI: [MIXS:0000350](https://w3id.org/mixs/0000350)



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
| Expected_value | reactor type name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: reactor_type
annotations:
  Expected_value:
    tag: Expected_value
    value: reactor type name
description: Anaerobic digesters can be designed and engineered to operate using a
  number of different process configurations, as batch or continuous, mesophilic,
  high solid or low solid, and single stage or multistage
title: reactor type
notes:
- type
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000350
multivalued: false
alias: reactor_type
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>