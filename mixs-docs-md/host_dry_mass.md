# Slot: host_dry_mass


_Measurement of dry mass_



URI: [MIXS:0000257](https://w3id.org/mixs/0000257)



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
| 500 gram |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | kilogram, gram |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_dry_mass
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: kilogram, gram
description: Measurement of dry mass
title: host dry mass
notes:
- dry
- host
- host.
- mass
examples:
- value: 500 gram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000257
multivalued: false
alias: host_dry_mass
domain_of:
- Agriculture
- FoodFarmEnvironment
- HostAssociated
- PlantAssociated
- SymbiontAssociated
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>