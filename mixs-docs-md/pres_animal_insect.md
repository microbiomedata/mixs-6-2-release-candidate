# Slot: pres_animal_insect


_The type and number of animals or insects present in the sampling space_



URI: [MIXS:0000819](https://w3id.org/mixs/0000819)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| cat;5 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration;count |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: pres_animal_insect
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration;count
description: The type and number of animals or insects present in the sampling space
title: presence of pets, animals, or insects
notes:
- animal
- presence
examples:
- value: cat;5
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '[cat|dog|rodent|snake|other];{integer}'
slot_uri: MIXS:0000819
multivalued: false
alias: pres_animal_insect
domain_of:
- Agriculture
- BuiltEnvironment
range: string
required: false
recommended: false

```
</details>