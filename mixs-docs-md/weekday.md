# Slot: weekday


_The day of the week when sampling occurred_



URI: [MIXS:0000848](https://w3id.org/mixs/0000848)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [WEEKDAYENUM](WEEKDAYENUM.md)






## Examples

| Value |
| --- |
| Sunday |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: weekday
description: The day of the week when sampling occurred
title: weekday
examples:
- value: Sunday
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000848
multivalued: false
alias: weekday
domain_of:
- BuiltEnvironment
range: WEEKDAY_ENUM
required: false
recommended: false

```
</details>