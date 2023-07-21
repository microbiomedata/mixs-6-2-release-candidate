# Slot: shading_device_mat


_The material the shading device is composed of_



URI: [MIXS:0000245](https://w3id.org/mixs/0000245)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | material name |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: shading_device_mat
annotations:
  Expected_value:
    tag: Expected_value
    value: material name
description: The material the shading device is composed of
title: shading device material
notes:
- device
- material
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000245
multivalued: false
alias: shading_device_mat
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>