# Slot: soil_texture_meth

URI: [MIXS:0000336](https://w3id.org/mixs/0000336)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| https://uwlab.soils.wisc.edu/wp-content/uploads/sites/17/2015/09/particle_size.pdf (hydrometer method) |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: soil_texture_meth
notes:
- method
- soil
- texture
examples:
- value: https://uwlab.soils.wisc.edu/wp-content/uploads/sites/17/2015/09/particle_size.pdf
    (hydrometer method)
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000336
multivalued: false
alias: soil_texture_meth
domain_of:
- Agriculture
- FoodFarmEnvironment
- Soil
range: string
required: false
recommended: false
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}'
  interpolated: true
  partial_match: true

```
</details>