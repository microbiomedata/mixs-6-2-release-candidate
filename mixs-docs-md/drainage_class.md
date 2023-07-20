# Slot: drainage_class


_Drainage classification from a standard system such as the USDA system_



URI: [MIXS:0001085](https://w3id.org/mixs/0001085)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[Soil](Soil.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [DRAINAGECLASSENUM](DRAINAGECLASSENUM.md)






## Examples

| Value |
| --- |
| well |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: drainage_class
description: Drainage classification from a standard system such as the USDA system
title: drainage classification
notes:
- classification
examples:
- value: well
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0001085
multivalued: false
alias: drainage_class
domain_of:
- Agriculture
- Soil
range: DRAINAGE_CLASS_ENUM

```
</details>