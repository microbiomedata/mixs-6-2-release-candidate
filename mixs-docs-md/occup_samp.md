# Slot: occup_samp


_Number of occupants present at time of sample within the given space_



URI: [MIXS:0000772](https://w3id.org/mixs/0000772)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [Float](Float.md)

* Required: True






## Examples

| Value |
| --- |
| 10 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: occup_samp
description: Number of occupants present at time of sample within the given space
title: occupancy at sampling
examples:
- value: '10'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000772
alias: occup_samp
domain_of:
- BuiltEnvironment
range: float
required: true

```
</details>