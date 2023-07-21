# Slot: number_plants


_The number of plant(s) in the sampling space_



URI: [MIXS:0000230](https://w3id.org/mixs/0000230)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[1-9][0-9]* \S.*\S+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: number_plants
description: The number of plant(s) in the sampling space
title: number of houseplants
notes:
- number
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000230
multivalued: false
alias: number_plants
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[1-9][0-9]* \S.*\S+$

```
</details>