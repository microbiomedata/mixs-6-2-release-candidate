# Slot: sort_tech


_Method used to sort/isolate cells or particles of interest_



URI: [MIXS:0000075](https://w3id.org/mixs/0000075)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Misag](Misag.md) |  |  yes  |
[Miuvig](Miuvig.md) |  |  yes  |







## Properties

* Range: [SORTTECHENUM](SORTTECHENUM.md)






## Examples

| Value |
| --- |
| optical manipulation |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: sort_tech
description: Method used to sort/isolate cells or particles of interest
title: sorting technology
examples:
- value: optical manipulation
in_subset:
- sequencing
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0000075
multivalued: false
alias: sort_tech
domain_of:
- Misag
- Miuvig
range: SORT_TECH_ENUM

```
</details>