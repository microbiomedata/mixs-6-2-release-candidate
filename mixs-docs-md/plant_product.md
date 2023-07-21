# Slot: plant_product


_Substance produced by the plant, where the sample was obtained from_



URI: [MIXS:0001058](https://w3id.org/mixs/0001058)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| xylem sap [PO:0025539] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | product name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: plant_product
annotations:
  Expected_value:
    tag: Expected_value
    value: product name
description: Substance produced by the plant, where the sample was obtained from
title: plant product
notes:
- plant
- product
examples:
- value: xylem sap [PO:0025539]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0001058
multivalued: false
alias: plant_product
domain_of:
- Agriculture
- PlantAssociated
range: string

```
</details>