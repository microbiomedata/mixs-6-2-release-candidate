# Slot: host_growth_cond


_Literature reference giving growth conditions of the host_



URI: [MIXS:0000871](https://w3id.org/mixs/0000871)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[HostAssociated](HostAssociated.md) |  |  yes  |
[SymbiontAssociated](SymbiontAssociated.md) |  |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| https://academic.oup.com/icesjms/article/68/2/349/617247 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: host_growth_cond
description: Literature reference giving growth conditions of the host
title: host growth conditions
notes:
- condition
- growth
- host
- host.
examples:
- value: https://academic.oup.com/icesjms/article/68/2/349/617247
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000871
multivalued: false
alias: host_growth_cond
domain_of:
- HostAssociated
- SymbiontAssociated
range: string
required: false
recommended: false
structured_pattern:
  syntax: '{PMID}|{DOI}|{URL}|{text}'
  interpolated: true
  partial_match: true

```
</details>