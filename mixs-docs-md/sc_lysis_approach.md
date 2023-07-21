# Slot: sc_lysis_approach


_Method used to free DNA from interior of the cell(s) or particle(s)_



URI: [MIXS:0000076](https://w3id.org/mixs/0000076)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [SCLYSISAPPROACHENUM](SCLYSISAPPROACHENUM.md)






## Examples

| Value |
| --- |
| enzymatic |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sc_lysis_approach
description: Method used to free DNA from interior of the cell(s) or particle(s)
title: single cell or viral particle lysis approach
notes:
- particle
- single
examples:
- value: enzymatic
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000076
multivalued: false
alias: sc_lysis_approach
domain_of:
- Misag
- Miuvig
range: SC_LYSIS_APPROACH_ENUM

```
</details>