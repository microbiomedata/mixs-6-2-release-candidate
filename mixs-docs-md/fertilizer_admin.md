# Slot: fertilizer_admin


_Type of fertilizer or amendment added to the soil or water for the purpose of improving substrate health and quality for plant growth. This field accepts terms listed under agronomic fertilizer (http://purl.obolibrary.org/obo/AGRO_00002062). Multiple terms may apply and can be separated by pipes, listing in reverse chronological order_



URI: [MIXS:0001127](https://w3id.org/mixs/0001127)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agriculture](Agriculture.md) |  |  no  |
[FoodFarmEnvironment](FoodFarmEnvironment.md) |  |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$`






## Examples

| Value |
| --- |
| fish emulsion [AGRO:00000082] |

## Identifier and Mapping Information







### Schema Source


* from schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal




## LinkML Source

<details>
```yaml
name: fertilizer_admin
description: Type of fertilizer or amendment added to the soil or water for the purpose
  of improving substrate health and quality for plant growth. This field accepts terms
  listed under agronomic fertilizer (http://purl.obolibrary.org/obo/AGRO_00002062).
  Multiple terms may apply and can be separated by pipes, listing in reverse chronological
  order
title: fertilizer administration
notes:
- administration
examples:
- value: fish emulsion [AGRO:00000082]
from_schema: https://turbomam.github.io/mixs-envo-struct-knowl-extraction//mixs_6_2_proposal
rank: 1000
slot_uri: MIXS:0001127
multivalued: false
alias: fertilizer_admin
domain_of:
- Agriculture
- FoodFarmEnvironment
range: string
required: false
recommended: false
pattern: ^\S+.*\S+ \[[a-zA-Z]{2,}:\d+\]$

```
</details>