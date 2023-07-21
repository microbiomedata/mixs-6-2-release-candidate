# Slot: source_mat_id


_A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2)_



URI: [MIXS:0000026](https://w3id.org/mixs/0000026)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  yes  |
[MigsBa](MigsBa.md) |  |  yes  |
[MigsEu](MigsEu.md) |  |  yes  |
[MigsOrg](MigsOrg.md) |  |  yes  |
[MigsPl](MigsPl.md) |  |  yes  |
[MigsVi](MigsVi.md) |  |  yes  |
[Mimag](Mimag.md) |  |  yes  |
[MimarksC](MimarksC.md) |  |  yes  |
[MimarksS](MimarksS.md) |  |  yes  |
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| MPI012345 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | for cultures of microorganisms: identifiers for two culture collections; for other material a unique arbitrary identifer |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: source_mat_id
annotations:
  Expected_value:
    tag: Expected_value
    value: 'for cultures of microorganisms: identifiers for two culture collections;
      for other material a unique arbitrary identifer'
description: A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID,
  and as opposed to a particular digital record of a material sample) used for extracting
  nucleic acids, and subsequent sequencing. The identifier can refer either to the
  original material collected or to any derived sub-samples. The INSDC qualifiers
  /specimen_voucher, /bio_material, or /culture_collection may or may not share the
  same value as the source_mat_id field. For instance, the /specimen_voucher qualifier
  and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen
  voucher and sampled tissue with the same identifier. However, the /culture_collection
  qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id
  would refer to an identifier from some derived culture from which the nucleic acids
  were extracted (e.g. xatc123 or ark:/2154/R2)
title: source material identifiers
notes:
- identifier
- material
- source
examples:
- value: MPI012345
in_subset:
- nucleic acid sequence source
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '{text}'
slot_uri: MIXS:0000026
multivalued: true
alias: source_mat_id
domain_of:
- Agriculture
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
range: string

```
</details>