# Slot: soluble_inorg_mat


_Concentration of substances such as ammonia, road-salt, sea-salt, cyanide, hydrogen sulfide, thiocyanates, thiosulfates, etc_



URI: [MIXS:0000672](https://w3id.org/mixs/0000672)



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
| Expected_value | soluble inorganic material name;measurement value || Preferred_unit | gram, microgram, mole per liter, gram per liter, parts per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: soluble_inorg_mat
annotations:
  Expected_value:
    tag: Expected_value
    value: soluble inorganic material name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: gram, microgram, mole per liter, gram per liter, parts per million
description: Concentration of substances such as ammonia, road-salt, sea-salt, cyanide,
  hydrogen sulfide, thiocyanates, thiosulfates, etc
title: soluble inorganic material
notes:
- inorganic
- material
- soluble
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000672
multivalued: true
alias: soluble_inorg_mat
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>