# Slot: samp_name


_A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. Use of a globally unique identifier for the field source_mat_id is recommended in addition to sample_name_



URI: [MIXS:0001107](https://w3id.org/mixs/0001107)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Air](Air.md) |  |  no  |
[BuiltEnvironment](BuiltEnvironment.md) |  |  no  |
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
[MigsBa](MigsBa.md) |  |  no  |
[MigsEu](MigsEu.md) |  |  no  |
[MigsOrg](MigsOrg.md) |  |  no  |
[MigsPl](MigsPl.md) |  |  no  |
[MigsVi](MigsVi.md) |  |  no  |
[Mimag](Mimag.md) |  |  no  |
[MimarksC](MimarksC.md) |  |  no  |
[MimarksS](MimarksS.md) |  |  no  |
[Mims](Mims.md) |  |  no  |
[Misag](Misag.md) |  |  no  |
[MiscellaneousNaturalOrArtificialEnvironment](MiscellaneousNaturalOrArtificialEnvironment.md) |  |  no  |
[Miuvig](Miuvig.md) |  |  no  |
[PlantAssociated](PlantAssociated.md) |  |  no  |
[Sediment](Sediment.md) |  |  no  |
[Soil](Soil.md) |  |  no  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |
[WastewaterSludge](WastewaterSludge.md) |  |  no  |
[Water](Water.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True






## Examples

| Value |
| --- |
| ISDsoil1 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_name
description: A local identifier or name that for the material sample used for extracting
  nucleic acids, and subsequent sequencing. It can refer either to the original material
  collected or to any derived sub-samples. It can have any format, but we suggest
  that you make it concise, unique and consistent within your lab, and as informative
  as possible. INSDC requires every sample name from a single Submitter to be unique.
  Use of a globally unique identifier for the field source_mat_id is recommended in
  addition to sample_name
title: sample name
notes:
- sample
examples:
- value: ISDsoil1
in_subset:
- investigation
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001107
multivalued: false
alias: samp_name
domain_of:
- Air
- BuiltEnvironment
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
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- MimarksC
- MimarksS
- Mims
- Misag
- MiscellaneousNaturalOrArtificialEnvironment
- Miuvig
- PlantAssociated
- Sediment
- Soil
- SymbiontAssociated
- WastewaterSludge
- Water
range: string
required: true

```
</details>