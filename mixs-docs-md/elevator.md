# Slot: elevator


_The number of elevators within the built structure_



URI: [MIXS:0000799](https://w3id.org/mixs/0000799)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [Integer](Integer.md)






## Examples

| Value |
| --- |
| 2 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: elevator
description: The number of elevators within the built structure
title: elevator count
notes:
- count
examples:
- value: '2'
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000799
multivalued: false
alias: elevator
domain_of:
- BuiltEnvironment
range: integer
required: false
recommended: false

```
</details>