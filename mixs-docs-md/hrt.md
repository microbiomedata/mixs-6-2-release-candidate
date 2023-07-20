# Slot: hrt


_Whether subject had hormone replacement theraphy, and if yes start date_



URI: [MIXS:0000969](https://w3id.org/mixs/0000969)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HumanVaginal](HumanVaginal.md) |  |  no  |







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
name: hrt
description: Whether subject had hormone replacement theraphy, and if yes start date
title: HRT
examples:
- value: '2013-03-25T12:42:31+00:32'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000969
multivalued: false
alias: hrt
domain_of:
- HumanVaginal
range: datetime
required: false
recommended: false

```
</details>