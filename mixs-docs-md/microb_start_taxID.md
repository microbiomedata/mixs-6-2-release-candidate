# Slot: microb_start_taxID


_Please include Genus species and strain ID, if known of microorganisms used in food production. For complex communities, pipes can be used to separate two or more microbes_



URI: [MIXS:0001222](https://w3id.org/mixs/0001222)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Lactobacillus rhamnosus [NCIT:C123495] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | NCIT:C14250 or NCBI taxid |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: microb_start_taxID
annotations:
  Expected_value:
    tag: Expected_value
    value: NCIT:C14250 or NCBI taxid
description: Please include Genus species and strain ID, if known of microorganisms
  used in food production. For complex communities, pipes can be used to separate
  two or more microbes
title: microbial starter NCBI taxonomy ID
notes:
- identifier
- microbial
- ncbi
- taxon
examples:
- value: Lactobacillus rhamnosus [NCIT:C123495]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}]|{integer}'
slot_uri: MIXS:0001222
multivalued: false
alias: microb_start_taxID
domain_of:
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>