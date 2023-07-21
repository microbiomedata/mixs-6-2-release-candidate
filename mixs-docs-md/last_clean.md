# Slot: last_clean


_The last time the floor was cleaned (swept, mopped, vacuumed)_



URI: [MIXS:0000814](https://w3id.org/mixs/0000814)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)






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
name: last_clean
description: The last time the floor was cleaned (swept, mopped, vacuumed)
title: last time swept/mopped/vacuumed
notes:
- time
examples:
- value: '2013-03-25T12:42:31+00:32'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000814
multivalued: false
alias: last_clean
domain_of:
- BuiltEnvironment
range: datetime
required: false
recommended: false

```
</details>