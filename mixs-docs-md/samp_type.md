# Slot: samp_type


_The type of material from which the sample was obtained. For the Hydrocarbon package, samples include types like core, rock trimmings, drill cuttings, piping section, coupon, pigging debris, solid deposit, produced fluid, produced water, injected water, swabs, etc. For the Food Package, samples are usually categorized as food, body products or tissues, or environmental material. This field accepts terms listed under environmental specimen (http://purl.obolibrary.org/obo/GENEPIO_0001246)_



URI: [MIXS:0000998](https://w3id.org/mixs/0000998)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |
[FoodFoodProductionFacility](FoodFoodProductionFacility.md) |  |  no  |
[HydrocarbonResourcesCores](HydrocarbonResourcesCores.md) |  |  no  |
[HydrocarbonResourcesFluidsSwabs](HydrocarbonResourcesFluidsSwabs.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| built environment sample [GENEPIO:0001248] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: samp_type
description: The type of material from which the sample was obtained. For the Hydrocarbon
  package, samples include types like core, rock trimmings, drill cuttings, piping
  section, coupon, pigging debris, solid deposit, produced fluid, produced water,
  injected water, swabs, etc. For the Food Package, samples are usually categorized
  as food, body products or tissues, or environmental material. This field accepts
  terms listed under environmental specimen (http://purl.obolibrary.org/obo/GENEPIO_0001246)
title: sample type
notes:
- sample
- type
examples:
- value: built environment sample [GENEPIO:0001248]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000998
multivalued: false
alias: samp_type
domain_of:
- FoodFarmEnvironment
- FoodFoodProductionFacility
- HydrocarbonResourcesCores
- HydrocarbonResourcesFluidsSwabs
range: string
required: true
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>