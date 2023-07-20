# Slot: virus_enrich_appr


_List of approaches used to enrich the sample for viruses, if any_



URI: [MIXS:0000036](https://w3id.org/mixs/0000036)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MigsVi](MigsVi.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [VIRUSENRICHAPPRENUM](VIRUSENRICHAPPRENUM.md)






## Examples

| Value |
| --- |
| filtration |
| FeCl Precipitation |
| ultracentrifugation |
| DNAse |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: virus_enrich_appr
description: List of approaches used to enrich the sample for viruses, if any
title: virus enrichment approach
notes:
- enrichment
examples:
- value: filtration
  description: was filtration + FeCl Precipitation + ultracentrifugation + DNAse
- value: FeCl Precipitation
  description: was filtration + FeCl Precipitation + ultracentrifugation + DNAse
- value: ultracentrifugation
  description: was filtration + FeCl Precipitation + ultracentrifugation + DNAse
- value: DNAse
  description: was filtration + FeCl Precipitation + ultracentrifugation + DNAse
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000036
alias: virus_enrich_appr
domain_of:
- MigsVi
- Miuvig
range: VIRUS_ENRICH_APPR_ENUM

```
</details>