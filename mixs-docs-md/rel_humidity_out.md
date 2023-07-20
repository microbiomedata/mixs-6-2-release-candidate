# Slot: rel_humidity_out


_The recorded outside relative humidity value at the time of sampling_



URI: [MIXS:0000188](https://w3id.org/mixs/0000188)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 12 per kilogram of air |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | gram of air, kilogram of air |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: rel_humidity_out
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: gram of air, kilogram of air
description: The recorded outside relative humidity value at the time of sampling
title: outside relative humidity
notes:
- humidity
- relative
examples:
- value: 12 per kilogram of air
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000188
multivalued: false
alias: rel_humidity_out
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>