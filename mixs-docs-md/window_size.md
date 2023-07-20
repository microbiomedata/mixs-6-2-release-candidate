# Slot: window_size


_The window's length and width_



URI: [MIXS:0000224](https://w3id.org/mixs/0000224)



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
| Expected_value | measurement value || Preferred_unit | inch, meter |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: window_size
annotations:
  Expected_value:
    tag: Expected_value
    value: measurement value
  Preferred_unit:
    tag: Preferred_unit
    value: inch, meter
description: The window's length and width
title: window area/size
notes:
- window
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{float} {unit} x {float} {unit}'
slot_uri: MIXS:0000224
multivalued: false
alias: window_size
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>