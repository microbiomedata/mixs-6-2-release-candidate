# Slot: host_pred_appr


_Tool or approach used for host prediction_



URI: [MIXS:0000088](https://w3id.org/mixs/0000088)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [HOSTPREDAPPRENUM](HOSTPREDAPPRENUM.md)






## Examples

| Value |
| --- |
| CRISPR spacer match |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6




## LinkML Source

<details>
```yaml
name: host_pred_appr
description: Tool or approach used for host prediction
title: host prediction approach
notes:
- host
- host.
- predict
examples:
- value: CRISPR spacer match
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//GSC_MIxS_6
rank: 1000
slot_uri: MIXS:0000088
multivalued: false
alias: host_pred_appr
domain_of:
- Miuvig
range: HOST_PRED_APPR_ENUM

```
</details>