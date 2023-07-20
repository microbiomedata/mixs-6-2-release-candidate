# Slot: date_last_rain


_The date of the last time it rained_



URI: [MIXS:0000786](https://w3id.org/mixs/0000786)



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


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: date_last_rain
description: The date of the last time it rained
title: date last rain
notes:
- date
- rain
examples:
- value: '2013-03-25T12:42:31+00:32'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000786
multivalued: false
alias: date_last_rain
domain_of:
- BuiltEnvironment
range: datetime
required: false
recommended: false

```
</details>