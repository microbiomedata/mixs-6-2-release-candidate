# Slot: fertilizer_date


_Date of administration of soil amendment or fertilizer. Multiple terms may apply and can be separated by pipes, listing in reverse chronological order_



URI: [MIXS:0001128](https://w3id.org/mixs/0001128)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)






## Examples

| Value |
| --- |
| 2018-05-11T10:00:00+01:00 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: fertilizer_date
description: Date of administration of soil amendment or fertilizer. Multiple terms
  may apply and can be separated by pipes, listing in reverse chronological order
title: fertilizer administration date
notes:
- administration
- date
examples:
- value: '2018-05-11T10:00:00+01:00'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001128
multivalued: false
alias: fertilizer_date
domain_of:
- FoodFarmEnvironment
range: datetime
required: false
recommended: false

```
</details>