# Slot: gaseous_substances


_Amount or concentration of substances such as hydrogen sulfide, carbon dioxide, methane, etc.; can include multiple substances_



URI: [MIXS:0000661](https://w3id.org/mixs/0000661)



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
| Expected_value | gaseous substance name;measurement value || Preferred_unit | micromole per liter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: gaseous_substances
annotations:
  Expected_value:
    tag: Expected_value
    value: gaseous substance name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: micromole per liter
description: Amount or concentration of substances such as hydrogen sulfide, carbon
  dioxide, methane, etc.; can include multiple substances
title: gaseous substances
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000661
multivalued: true
alias: gaseous_substances
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>