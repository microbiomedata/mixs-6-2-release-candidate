# Slot: host_length


_The length of subject_



URI: [MIXS:0000256](https://w3id.org/mixs/0000256)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[HostAssociated](HostAssociated.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| 1 meter |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_length
description: The length of subject
title: host length
notes:
- host
- host.
- length
examples:
- value: 1 meter
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000256
multivalued: false
alias: host_length
domain_of:
- Agriculture
- FoodFarmEnvironment
- HostAssociated
- PlantAssociated
- SymbiontAssociated
range: string
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>