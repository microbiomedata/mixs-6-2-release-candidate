# Slot: built_struc_age


_The age of the built structure since construction_



URI: [MIXS:0000145](https://w3id.org/mixs/0000145)



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
| 15 years |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | year |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: built_struc_age
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: year
description: The age of the built structure since construction
title: built structure age
notes:
- age
examples:
- value: 15 years
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000145
multivalued: false
alias: built_struc_age
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>