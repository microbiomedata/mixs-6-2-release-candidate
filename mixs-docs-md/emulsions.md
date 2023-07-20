# Slot: emulsions


_Amount or concentration of substances such as paints, adhesives, mayonnaise, hair colorants, emulsified oils, etc.; can include multiple emulsion types_



URI: [MIXS:0000660](https://w3id.org/mixs/0000660)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | emulsion name;measurement value || Preferred_unit | gram per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: emulsions
annotations:
  Expected_value:
    tag: Expected_value
    value: emulsion name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: gram per liter
description: Amount or concentration of substances such as paints, adhesives, mayonnaise,
  hair colorants, emulsified oils, etc.; can include multiple emulsion types
title: emulsions
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000660
multivalued: true
alias: emulsions
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>