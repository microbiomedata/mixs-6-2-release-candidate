# Slot: ances_data


_Information about either pedigree or other ancestral information description (e.g. parental variety in case of mutant or selection), e.g. A/3*B (meaning [(A x B) x B] x B)_



URI: [MIXS:0000247](https://w3id.org/mixs/0000247)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[HostAssociated](HostAssociated.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| A/3*B |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: ances_data
description: Information about either pedigree or other ancestral information description
  (e.g. parental variety in case of mutant or selection), e.g. A/3*B (meaning [(A
  x B) x B] x B)
title: ancestral data
examples:
- value: A/3*B
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000247
multivalued: false
alias: ances_data
domain_of:
- Agriculture
- FoodFarmEnvironment
- HostAssociated
- PlantAssociated
range: string
required: false
recommended: false

```
</details>