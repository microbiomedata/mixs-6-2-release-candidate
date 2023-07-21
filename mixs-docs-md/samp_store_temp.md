# Slot: samp_store_temp


_Temperature at which sample was stored, e.g. -80 degree Celsius_



URI: [MIXS:0000110](https://w3id.org/mixs/0000110)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[Air](Air.md) |  |  no  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |
[HostAssociated](HostAssociated.md) |  |  no  |
[HumanAssociated](HumanAssociated.md) |  |  no  |
[HumanGut](HumanGut.md) |  |  no  |
[HumanOral](HumanOral.md) |  |  no  |
[HumanSkin](HumanSkin.md) |  |  no  |
[HumanVaginal](HumanVaginal.md) |  |  no  |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  no  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |
[Water](Water.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`






## Examples

| Value |
| --- |
| -80 degree Celsius |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Preferred_unit | degree Celsius |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: samp_store_temp
annotations:
  Preferred_unit:
    tag: Preferred_unit
    value: degree Celsius
description: Temperature at which sample was stored, e.g. -80 degree Celsius
title: sample storage temperature
notes:
- sample
- storage
- temperature
examples:
- value: -80 degree Celsius
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000110
multivalued: false
alias: samp_store_temp
domain_of:
- Agriculture
- Air
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
- HostAssociated
- HumanAssociated
- HumanGut
- HumanOral
- HumanSkin
- HumanVaginal
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
- MicrobialMatBiofilm
- MiscellaneousNaturalOrArtificialEnvironment
- PlantAssociated
- Sediment
- SymbiontAssociated
- WastewaterSludge
- Water
range: string
required: false
recommended: false
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>