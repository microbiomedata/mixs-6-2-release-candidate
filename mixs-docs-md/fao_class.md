# Slot: fao_class


_Soil classification from the FAO World Reference Database for Soil Resources. The list can be found at http://www.fao.org/nr/land/sols/soil/wrb-soil-maps/reference-groups_



URI: [MIXS:0001083](https://w3id.org/mixs/0001083)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [FAOCLASSENUM](FAOCLASSENUM.md)






## Examples

| Value |
| --- |
| Luvisols |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: fao_class
description: Soil classification from the FAO World Reference Database for Soil Resources.
  The list can be found at http://www.fao.org/nr/land/sols/soil/wrb-soil-maps/reference-groups
title: soil_taxonomic/FAO classification
notes:
- classification
examples:
- value: Luvisols
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001083
multivalued: false
alias: fao_class
domain_of:
- Agriculture
- Soil
range: FAO_CLASS_ENUM

```
</details>