# Slot: ventilation_type


_Ventilation system used in the sampled premises_



URI: [MIXS:0000756](https://w3id.org/mixs/0000756)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  yes  |
[BuiltEnvironment](BuiltEnvironment.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Operable windows |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | ventilation type name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: ventilation_type
annotations:
  Expected_value:
    tag: Expected_value
    value: ventilation type name
description: Ventilation system used in the sampled premises
title: ventilation type
notes:
- type
examples:
- value: Operable windows
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000756
alias: ventilation_type
domain_of:
- Air
- BuiltEnvironment
- FoodFarmEnvironment
range: string

```
</details>