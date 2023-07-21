# Slot: misc_param


_Any other measurement performed or parameter collected, that is not listed here_



URI: [MIXS:0000752](https://w3id.org/mixs/0000752)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Air](Air.md) |  |  yes  |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  yes  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  yes  |
[HostAssociated](HostAssociated.md) |  |  yes  |
[HumanAssociated](HumanAssociated.md) |  |  yes  |
[HumanGut](HumanGut.md) |  |  yes  |
[HumanOral](HumanOral.md) |  |  yes  |
[HumanSkin](HumanSkin.md) |  |  yes  |
[HumanVaginal](HumanVaginal.md) |  |  yes  |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  yes  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  yes  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |
[WastewaterSludge](WastewaterSludge.md) |  |  yes  |
[Water](Water.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| Bicarbonate ion concentration;2075 micromole per kilogram |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: misc_param
description: Any other measurement performed or parameter collected, that is not listed
  here
title: miscellaneous parameter
notes:
- parameter
examples:
- value: Bicarbonate ion concentration;2075 micromole per kilogram
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text};{float} {unit}'
slot_uri: MIXS:0000752
multivalued: true
alias: misc_param
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
- Soil
- SymbiontAssociated
- WastewaterSludge
- Water
range: string
required: false
recommended: false

```
</details>