# Slot: plant_growth_med


_Specification of the media for growing the plants or tissue cultured samples, e.g. soil, aeroponic, hydroponic, in vitro solid culture medium, in vitro liquid culture medium. Recommended value is a specific value from EO:plant growth medium (follow this link for terms http://purl.obolibrary.org/obo/EO_0007147) or other controlled vocabulary_



URI: [MIXS:0001057](https://w3id.org/mixs/0001057)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[PlantAssociated](PlantAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | EO or enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: plant_growth_med
annotations:
  Expected_value:
    tag: Expected_value
    value: EO or enumeration
description: Specification of the media for growing the plants or tissue cultured
  samples, e.g. soil, aeroponic, hydroponic, in vitro solid culture medium, in vitro
  liquid culture medium. Recommended value is a specific value from EO:plant growth
  medium (follow this link for terms http://purl.obolibrary.org/obo/EO_0007147) or
  other controlled vocabulary
title: plant growth medium
notes:
- growth
- plant
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
string_serialization: '{termLabel} [{termID}] or [husk|other artificial liquid medium|other
  artificial solid medium|peat moss|perlite|pumice|sand|soil|vermiculite|water]'
slot_uri: MIXS:0001057
alias: plant_growth_med
domain_of:
- Agriculture
- FoodFarmEnvironment
- PlantAssociated
range: string
required: false
recommended: false

```
</details>