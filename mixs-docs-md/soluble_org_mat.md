# Slot: soluble_org_mat


_Concentration of substances such as urea, fruit sugars, soluble proteins, drugs, pharmaceuticals, etc_



URI: [MIXS:0000673](https://w3id.org/mixs/0000673)



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
| Expected_value | soluble organic material name;measurement value || Preferred_unit | gram, microgram, mole per liter, gram per liter, parts per million |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: soluble_org_mat
annotations:
  Expected_value:
    tag: Expected_value
    value: soluble organic material name;measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: gram, microgram, mole per liter, gram per liter, parts per million
description: Concentration of substances such as urea, fruit sugars, soluble proteins,
  drugs, pharmaceuticals, etc
title: soluble organic material
notes:
- material
- organic
- soluble
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000673
multivalued: true
alias: soluble_org_mat
domain_of:
- WastewaterSludge
range: string
required: false
recommended: false

```
</details>