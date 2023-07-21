# Slot: host_pred_est_acc


_For each tool or approach used for host prediction, estimated false discovery rates should be included, either computed de novo or from the literature_



URI: [MIXS:0000089](https://w3id.org/mixs/0000089)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| CRISPR spacer match: 0 or 1 mismatches, estimated 8% FDR at the host genus rank (Edwards et al. 2016 doi:10.1093/femsre/fuv048) |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_pred_est_acc
description: For each tool or approach used for host prediction, estimated false discovery
  rates should be included, either computed de novo or from the literature
title: host prediction estimated accuracy
notes:
- host
- host.
- predict
examples:
- value: 'CRISPR spacer match: 0 or 1 mismatches, estimated 8% FDR at the host genus
    rank (Edwards et al. 2016 doi:10.1093/femsre/fuv048)'
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000089
multivalued: false
alias: host_pred_est_acc
domain_of:
- Miuvig
range: string

```
</details>