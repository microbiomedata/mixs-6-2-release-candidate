# Slot: prod_start_date


_Date of field's first production_



URI: [MIXS:0001008](https://w3id.org/mixs/0001008)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Recommended: True






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
name: prod_start_date
description: Date of field's first production
title: production start date
notes:
- date
- production
- start
examples:
- value: '2013-03-25T12:42:31+00:32'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001008
multivalued: false
alias: prod_start_date
domain_of:
- HydrocarbonResourcesFluidsSwabs
range: datetime
recommended: true

```
</details>