# Slot: microb_start


_Any type of microorganisms used in food production.  This field accepts terms listed under live organisms for food production (http://purl.obolibrary.org/obo/FOODON_0344453)_



URI: [MIXS:0001217](https://w3id.org/mixs/0001217)



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
| starter cultures [FOODON:03544454] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | FOODON:03544453 |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: microb_start
annotations:
  Expected_value:
    tag: Expected_value
    value: FOODON:03544453
description: Any type of microorganisms used in food production.  This field accepts
  terms listed under live organisms for food production (http://purl.obolibrary.org/obo/FOODON_0344453)
title: microbial starter
notes:
- microbial
examples:
- value: starter cultures [FOODON:03544454]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{term label} [{termID}]|{text}'
slot_uri: MIXS:0001217
multivalued: false
alias: microb_start
domain_of:
- FoodHumanFoods
range: string
required: false
recommended: false

```
</details>