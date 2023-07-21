# Slot: soil_cover


_Material covering the sampled soil. This field accepts terms under ENVO:00010483, environmental material_



URI: [MIXS:0001159](https://w3id.org/mixs/0001159)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| bare soil [ENVO01001616] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | subclass of 'environmental material', http://purl.obolibrary.org/obo/ENVO_00010483 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: soil_cover
annotations:
  Expected_value:
    tag: Expected_value
    value: subclass of 'environmental material', http://purl.obolibrary.org/obo/ENVO_00010483
description: Material covering the sampled soil. This field accepts terms under ENVO:00010483,
  environmental material
title: soil cover
notes:
- soil
examples:
- value: bare soil [ENVO01001616]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: bare soil [ENVO:01001616]
slot_uri: MIXS:0001159
multivalued: false
alias: soil_cover
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string

```
</details>