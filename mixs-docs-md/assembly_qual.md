# Slot: assembly_qual


_The assembly quality category is based on sets of criteria outlined for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities with a consensus error rate equivalent to Q50 or better. High Quality Draft:Multiple fragments where gaps span repetitive regions. Presence of the 23S, 16S and 5S rRNA genes and at least 18 tRNAs. Medium Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Low Quality Draft:Many fragments with little to no review of assembly other than reporting of standard assembly statistics. Assembly statistics include, but are not limited to total assembly size, number of contigs, contig N50/L50, and maximum contig length. For MIUVIG; Finished: Single, validated, contiguous sequence per replicon without gaps or ambiguities, with extensive manual review and editing to annotate putative gene functions and transcriptional units. High-quality draft genome: One or multiple fragments, totaling  90% of the expected genome or replicon sequence or predicted complete. Genome fragment(s): One or multiple fragments, totalling < 90% of the expected genome or replicon sequence, or for which no genome size could be estimated_



URI: [MIXS:0000056](https://w3id.org/mixs/0000056)



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
[Mims](Mims.md) |  |  yes  |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |
[MimsSoil](MimsSoil.md) |  |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| High-quality draft genome |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| Expected_value | enumeration |



### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: assembly_qual
annotations:
  Expected_value:
    tag: Expected_value
    value: enumeration
description: 'The assembly quality category is based on sets of criteria outlined
  for each assembly quality category. For MISAG/MIMAG; Finished: Single, validated,
  contiguous sequence per replicon without gaps or ambiguities with a consensus error
  rate equivalent to Q50 or better. High Quality Draft:Multiple fragments where gaps
  span repetitive regions. Presence of the 23S, 16S and 5S rRNA genes and at least
  18 tRNAs. Medium Quality Draft:Many fragments with little to no review of assembly
  other than reporting of standard assembly statistics. Low Quality Draft:Many fragments
  with little to no review of assembly other than reporting of standard assembly statistics.
  Assembly statistics include, but are not limited to total assembly size, number
  of contigs, contig N50/L50, and maximum contig length. For MIUVIG; Finished: Single,
  validated, contiguous sequence per replicon without gaps or ambiguities, with extensive
  manual review and editing to annotate putative gene functions and transcriptional
  units. High-quality draft genome: One or multiple fragments, totaling  90% of the
  expected genome or replicon sequence or predicted complete. Genome fragment(s):
  One or multiple fragments, totalling < 90% of the expected genome or replicon sequence,
  or for which no genome size could be estimated'
title: assembly quality
notes:
- quality
examples:
- value: High-quality draft genome
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
string_serialization: '[Finished genome|High-quality draft genome|Medium-quality draft
  genome|Low-quality draft genome|Genome fragment(s)]'
slot_uri: MIXS:0000056
multivalued: false
alias: assembly_qual
domain_of:
- Agriculture
- MigsBa
- MigsEu
- MigsOrg
- MigsPl
- MigsVi
- Mimag
- Mims
- Misag
- Miuvig
range: string

```
</details>