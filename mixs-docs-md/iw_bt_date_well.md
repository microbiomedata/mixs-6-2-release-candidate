# Slot: iw_bt_date_well


_Injection water breakthrough date per well following a secondary and/or tertiary recovery_



URI: [MIXS:0001010](https://w3id.org/mixs/0001010)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







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
name: iw_bt_date_well
description: Injection water breakthrough date per well following a secondary and/or
  tertiary recovery
title: injection water breakthrough date of specific well
notes:
- date
- water
examples:
- value: '2013-03-25T12:42:31+00:32'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001010
multivalued: false
alias: iw_bt_date_well
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: datetime
required: false
recommended: false

```
</details>