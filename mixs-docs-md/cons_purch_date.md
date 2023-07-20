# Slot: cons_purch_date


_The date a food product was purchased by consumer_



URI: [MIXS:0001197](https://w3id.org/mixs/0001197)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)






## Examples

| Value |
| --- |
| 2013-03-25T12:42:31+00:32 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: cons_purch_date
description: The date a food product was purchased by consumer
title: purchase date
notes:
- date
examples:
- value: '2013-03-25T12:42:31+00:32'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001197
multivalued: false
alias: cons_purch_date
domain_of:
- FoodAnimalAndAnimalFeed
- FoodHumanFoods
range: datetime
required: false
recommended: false

```
</details>