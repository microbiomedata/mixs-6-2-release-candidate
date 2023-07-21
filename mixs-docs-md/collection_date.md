# Slot: collection_date


_The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant_



URI: [MIXS:0000011](https://w3id.org/mixs/0000011)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodAnimalAndAnimalFeed](FoodAnimalAndAnimalFeed.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[FoodHumanFoods](FoodHumanFoods.md) |  |  no  |
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
[Miuvig](Miuvig.md) |  |  no  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  no  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [Datetime](Datetime.md)

* Required: True






## Examples

| Value |
| --- |
| 2013-03-25T12:42:31+00:32 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: collection_date
description: 'The time of sampling, either as an instance (single point in time) or
  interval. In case no exact time is available, the date/time can be right truncated
  i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10;
  2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant'
title: collection date
notes:
- date
examples:
- value: '2013-03-25T12:42:31+00:32'
in_subset:
- environment
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000011
multivalued: false
alias: collection_date
domain_of:
- FoodAnimalAndAnimalFeed
- FoodFarmEnvironment
- FoodFoodProductionFacility
- FoodHumanFoods
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
- Miuvig
- SymbiontAssociated
range: datetime
required: true

```
</details>