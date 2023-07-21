# Slot: date_extr_weath


_Date of unusual weather events that may have affected microbial populations. Multiple terms can be separated by pipes, listed in reverse chronological order_



URI: [MIXS:0001142](https://w3id.org/mixs/0001142)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Multivalued: True






## Examples

| Value |
| --- |
| 2013-03-25T12:42:31+00:32 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: date_extr_weath
description: Date of unusual weather events that may have affected microbial populations.
  Multiple terms can be separated by pipes, listed in reverse chronological order
title: extreme weather date
notes:
- date
- extreme
- weather
examples:
- value: '2013-03-25T12:42:31+00:32'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001142
multivalued: true
alias: date_extr_weath
domain_of:
- FoodFarmEnvironment
range: datetime
required: false
recommended: false

```
</details>