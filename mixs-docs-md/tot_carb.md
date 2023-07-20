# Slot: tot_carb


_Total carbon content_



URI: [MIXS:0000525](https://w3id.org/mixs/0000525)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MicrobialMatBiofilm](MicrobialMatBiofilm.md) |  |  yes  |
[Sediment](Sediment.md) |  |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: tot_carb
description: Total carbon content
title: total carbon
notes:
- carbon
- total
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000525
multivalued: false
alias: tot_carb
domain_of:
- Agriculture
- MicrobialMatBiofilm
- Sediment
range: string
pattern: ^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)? \S.*\S$

```
</details>