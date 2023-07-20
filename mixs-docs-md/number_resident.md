# Slot: number_resident


_The number of individuals currently occupying in the sampling location_



URI: [MIXS:0000232](https://w3id.org/mixs/0000232)



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


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: number_resident
description: The number of individuals currently occupying in the sampling location
title: number of residents
notes:
- number
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000232
multivalued: false
alias: number_resident
domain_of:
- BuiltEnvironment
range: string
required: false
recommended: false
pattern: ^[1-9][0-9]* \S.*\S+$

```
</details>